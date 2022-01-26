from ServerHandler import ServerHandler
from LightSharkBridge import LightSharkBridge
from OSCHandler import OSCHandler
from MidiHandler import MidiHandler


initial_conf = {
    "fader": [
        {"fader_id": 1, "cc": 34},
        {"fader_id": 2, "cc": 35},
        {"fader_id": 3, "cc": 36},
        {"fader_id": 4, "cc": 37},
        {"fader_id": 5, "cc": 38},
        {"fader_id": 6, "cc": 39},
        {"fader_id": 7, "cc": 40},
        {"fader_id": 8, "cc": 41},
        {"fader_id": 9, "cc": None},
        {"fader_id": 10, "cc": None},
    ],
    "executor": [
        [
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}]
        ],
        [
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}],
            [{"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}, {"cc": None}]
        ]
    ],
    "master_cc": 33,
}

osc_client = OSCHandler()
ls_bridge = LightSharkBridge(osc_client)
midi_client = MidiHandler(ls_bridge)
ls_bridge.init_functions(midi_client, initial_conf)
ServerHandler(ls_bridge)
