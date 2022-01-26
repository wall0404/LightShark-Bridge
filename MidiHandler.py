from rtmidi.midiutil import open_midiinput, open_midioutput
from rtmidi.midiconstants import CONTROL_CHANGE
import time
from threading import Thread


class MidiHandler:
    midi_in_port = None
    midi_out_port = None
    ls_bridge = None

    def __init__(self, ls_bridge):
        self.midi_in_port, port_name = open_midiinput(1)
        self.midi_out_port, port_name = open_midioutput(1)
        self.ls_bridge = ls_bridge

        thread = Thread(target=listen, args=(self.midi_in_port, self.handle_midi_input(),))
        thread.start()

    def send_midi_message(self, cc_number, value):
        self.midi_out_port.send_message([CONTROL_CHANGE, cc_number, value])

    def handle_midi_input(self, cc_number, value):
        # TODO: handle midi input
        pass

    def sync_midi_console(self):
        # sync faders
        for x in range(len(self.ls_bridge.fader)):
            value = self.ls_bridge.fader[x].get_fader()
            self.ls_bridge.fader[x].set_fader(value)

        # sync master
        value = self.ls_bridge.master.get_fader()
        self.ls_bridge.master.set_fader(value)

        # TODO: sync encoder wheels


def listen(midi_in_port, callback):
    while True:
        msg = midi_in_port.get_message()

        if msg:
            cc_number = msg[0][1]
            value = msg[0][2]

            callback(cc_number, value)

        time.sleep(0.01)
