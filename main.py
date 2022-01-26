from ServerHandler import ServerHandler
from LightSharkBridge import LightSharkBridge
from OSCHandler import OSCHandler
from MidiHandler import MidiHandler


osc_client = OSCHandler()
ls_bridge = LightSharkBridge(osc_client)
midi_client = MidiHandler(ls_bridge)
ls_bridge.init_functions(30, [2, 6, 8], midi_client)
ServerHandler(ls_bridge)
