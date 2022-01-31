class Function:
    name = ""
    value = None
    osc_client = None
    cc_number = None
    osc_url = None

    max_value = 1
    min_value = 0

    mode = "push"

    def __init__(self, osc_client, midi_client, name, cc_number):
        self.value = 0
        self.name = name
        self.osc_client = osc_client
        self.midi_client = midi_client
        self.cc_number = cc_number

    def set_value(self, value):
        if self.mode == "toggle" and self.value == value:
            return

        if type(value) is int:
            if Fader.min_value <= value <= Fader.max_value:
                self.value = value

                self.update_osc()
                self.update_midi()
            else:
                return TypeError("value is not between " + str(self.min_value) + " and " + str(self.max_value))
        else:
            return TypeError("value is not an int")

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def update_midi(self):
        if self.cc_number is not None:
            self.midi_client.send_midi_message(self.cc_number, self.value)

    def update_osc(self):
        if self.mode == "toggle":
            value = 0
        else:
            value = self.value
        self.osc_client.send_osc_message(self.osc_url, value)


class Fader(Function):
    max_value = 255
    min_value = 0

    def __init__(self, fader_id, osc_client, midi_client, name, cc_number):
        super().__init__(osc_client, midi_client, name, cc_number)
        self.fader_id = fader_id
        self.osc_client = osc_client
        self.osc_url = "/LS/Level/PB/" + str(self.fader_id)


class MasterFader(Function):
    max_value = 255
    min_value = 0

    def __init__(self, osc_client, midi_client, cc_number):
        super().__init__(osc_client, midi_client, "", cc_number)
        self.osc_url = "/LS/Level/GM"


class Executor(Function):

    mode = "toggle"

    def __init__(self, executor_x, executor_y, executor_z, osc_client, midi_client, cc_number, mode="toggle"):
        super().__init__(osc_client, midi_client, "master", cc_number)

        self.executor_x = executor_x
        self.executor_y = executor_y
        self.executor_z = executor_z
        self.mode = mode
        self.osc_url = "/LS/Executor/" + str(self.executor_x) + "/" + str(self.executor_y) + "/" + str(self.executor_z)
