from rtmidi import NoDevicesError
from rtmidi.midiutil import open_midiinput, open_midioutput
from rtmidi.midiconstants import CONTROL_CHANGE
import time
from threading import Thread


class MidiHandler:
    midi_in_port = None
    midi_out_port = None
    ls_bridge = None

    def __init__(self, ls_bridge):
        self.ls_bridge = ls_bridge
        self.connect_midi_console()

        thread = Thread(target=listen, args=(self.midi_in_port, self.handle_midi_input,))
        thread.start()

    def connect_midi_console(self):
        try:
            self.midi_in_port, port_name = open_midiinput(1)
            self.midi_out_port, port_name = open_midioutput(1)
        except NoDevicesError:
            print("Midi Console not connected")

    def send_midi_message(self, cc_number, value):
        # only if console is connected:
        if self.midi_out_port is not None:
            self.midi_out_port.send_message([CONTROL_CHANGE, cc_number, value/2])

    def handle_midi_input(self, cc_number, value):
        function = self.ls_bridge.find_function_by_cc(cc_number)
        if function:
            function.set_value(value*2)

    def sync_midi_console(self):
        # sync faders
        for x in range(len(self.ls_bridge.fader)):
            value = self.ls_bridge.faders[x].get_value()
            self.ls_bridge.faders[x].set_value(value)

        # sync master
        value = self.ls_bridge.master.get_fader()
        self.ls_bridge.master.set_fader(value)

        # TODO: sync encoder wheels


def listen(midi_in_port, callback):
    while midi_in_port is not None:
        msg = midi_in_port.get_message()

        if msg:
            cc_number = msg[0][1]
            value = msg[0][2]

            callback(cc_number, value)

