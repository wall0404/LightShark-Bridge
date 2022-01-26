from pythonosc import udp_client


class OSCHandler:
    server_ip = "192.168.0.250"
    server_port = 7000
    osc_client = None

    def __init__(self):
        self.osc_client = udp_client.SimpleUDPClient(self.server_ip, self.server_port)

    def send_osc_message(self, path, value):
        self.osc_client.send_message(path, value)
