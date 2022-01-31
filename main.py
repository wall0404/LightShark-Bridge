from ServerHandler import ServerHandler
from LightSharkBridge import LightSharkBridge
from OSCHandler import OSCHandler
from MidiHandler import MidiHandler


initial_conf = {
    "fader": [
        {"fader_id": 1, "cc": 1, "name": "Fader1"},
        {"fader_id": 2, "cc": 2, "name": "Fader2"},
        {"fader_id": 3, "cc": 3, "name": "Fader3"},
        {"fader_id": 4, "cc": 4, "name": "Fader4"},
        {"fader_id": 5, "cc": 5, "name": "Fader5"},
        {"fader_id": 6, "cc": 6, "name": "Fader6"},
        {"fader_id": 7, "cc": 7, "name": "Fader7"},
        {"fader_id": 8, "cc": 8, "name": "Fader8"},
        {"fader_id": 9, "cc": None, "name": "Fader9"},
        {"fader_id": 10, "cc": None, "name": "Fader10"},
        {"fader_id": 11, "cc": 28, "name": "Fader11"},
        {"fader_id": 12, "cc": 29, "name": "Fader12"},
        {"fader_id": 13, "cc": 30, "name": "Fader13"},
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
