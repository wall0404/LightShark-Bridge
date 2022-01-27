from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import ThreadingHTTPServer
from threading import Thread


class Routes:
    routes = []

    @staticmethod
    def matches_path(method, path):
        for x in range(len(Routes.routes)):
            func = Routes.routes[x].matches_path(method, path)
            if func:
                return func
        return -1


class Route:
    pattern = ""
    method = ""
    function_name = ""

    def __init__(self, method, pattern, function_name):
        self.pattern = pattern
        self.function_name = function_name
        self.method = method

    def matches_path(self, method, path):
        if self.method != method:
            return False

        pattern_parts = self.pattern.split("/")
        request_parts = path.split("/")

        # extracted parameters from path
        parameters = []

        if len(pattern_parts) != len(request_parts):
            return False

        for x in range(len(pattern_parts)):
            if pattern_parts[x] == "" and request_parts[x] == "":
                continue

            if pattern_parts[x][0] == '#':
                if pattern_parts[x][1:].isalpha():
                    if request_parts[x] == "":
                        raise ValueError("Parameter is missing in request")

                    if request_parts[x].isnumeric():
                        parameters.append(request_parts[x])
                    else:
                        parameters.append('"' + request_parts[x] + '"')
                    continue
                else:
                    raise AttributeError("Route is not defined correctly")
            else:
                if not pattern_parts[x].isalpha():
                    raise AttributeError("Route is not defined correctly")
                else:
                    if pattern_parts[x] == request_parts[x]:
                        continue
                    else:
                        return False

        return self.function_name + "(" + ', '.join(parameters) + ")"

    def get_function_name(self):
        return self.function_name


class RequestHandler(BaseHTTPRequestHandler):
    ls_bridge = None

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        try:
            func = Routes.matches_path("GET", self.path)

            if func != -1:
                response = eval("RequestHandler.ls_bridge." + func)
                if type(response) is int:
                    self.wfile.write(bytes(str(response), "utf-8"))
                else:
                    self.wfile.write(bytes(response, "utf-8"))

            else:
                self.wfile.write(bytes("route not defined", "utf-8"))
        except ValueError as e:
            self.wfile.write(bytes(str(e), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        try:
            func = Routes.matches_path("POST", self.path)

            if func != -1:
                eval("RequestHandler.ls_bridge." + func)
                self.wfile.write(bytes("success", "utf-8"))
            else:
                self.wfile.write(bytes("route not defined", "utf-8"))
        except ValueError as e:
            self.wfile.write(bytes(str(e), "utf-8"))
        except TypeError as e:
            self.wfile.write(bytes(str(e), "utf-8"))


class ServerHandler:
    webServer = None
    hostName = "localhost"
    serverPort = 8080
    httpd = None

    def __init__(self, ls_bridge):
        RequestHandler.ls_bridge = ls_bridge

        server_address = (self.hostName, self.serverPort)
        print("Start server at http://%s:%s" % (self.hostName, self.serverPort))
        self.httpd = ThreadingHTTPServer(server_address, RequestHandler)

        thread = Thread(target=serve, args=(self.httpd,))
        thread.start()


# define routes
Routes.routes = [
    Route("GET", "/state", "get_state"),

    Route("GET", "/fader/#id", "get_fader_value"),
    Route("POST", "/fader/#id/#value", "set_fader_value"),

    Route("GET", "/executor/#x/#y/#z", "get_executor_state"),
    Route("POST", "/executor/#x/#y/#z/#value", "set_executor_state"),

    Route("GET", "/master", "get_master_value"),
    Route("POST", "/master/#value", "set_master_value")
]


def serve(httpd):
    with httpd:
        httpd.serve_forever()
        print("Server stopped")
