import json

from Functions import Fader, MasterFader, Executor


def encode_ls_bridge(ls_bridge):
    fader_count = len(ls_bridge.faders)

    return_obj = {'fader': [], 'executor': [], 'master': 0}
    for x in range(fader_count):
        return_obj['fader'].append(ls_bridge.get_fader_value(x + 1))

    for x in range(len(ls_bridge.executors)):
        return_obj['executor'].append([])
        for y in range(len(ls_bridge.executors[x])):
            return_obj['executor'][x].append([])
            for z in range(len(ls_bridge.executors[x][y])):
                return_obj['executor'][x][y].append(ls_bridge.get_executor_state(x + 1, y + 1, z + 1))

    return_obj['master'] = ls_bridge.get_master_value()

    return json.dumps(return_obj)


class LightSharkBridge:
    faders = []
    executors = []
    osc_client = None
    master = None
    functions = []

    def __init__(self, osc_client):
        self.osc_client = osc_client

    def init_functions(self, midi_client, initial_conf):
        for x in range(len(initial_conf['fader'])):
            fader = Fader(initial_conf['fader'][x]['fader_id'], self.osc_client, midi_client, initial_conf['fader'][x]['cc'])
            self.faders.append(fader)
            self.functions.append(fader)

        executor_matrix = [2, 6, 8]
        for x in range(len(initial_conf['executor'])):
            self.executors.append([])
            for y in range(len(initial_conf['executor'][x])):
                self.executors[x].append([])
                for z in range(len(initial_conf['executor'][x][y])):
                    executor = Executor(x + 1, y + 1, z + 1, self.osc_client, midi_client, None)
                    self.executors[x][y].append(executor)
                    self.functions.append(executor)

        self.master = MasterFader(self.osc_client, midi_client, initial_conf['master_cc'])
        self.functions.append(self.master)

    def find_function_by_cc(self, cc_number):
        for x in range(len(self.functions)):
            if self.functions[x].cc_number == cc_number:
                return self.functions[x]

        return False

    def set_fader_value(self, fader_id, value):
        self.faders[fader_id - 1].set_value(value)

    def get_fader_value(self, fader_id):
        return self.faders[fader_id - 1].get_value()

    def set_executor_state(self, x, y, z, value):
        self.executors[x - 1][y - 1][z - 1].set_value(value)

    def get_executor_state(self, x, y, z):
        return self.executors[x - 1][y - 1][z - 1].get_value()

    def set_master_value(self, value):
        self.master.set_value(value)

    def get_master_value(self):
        return self.master.get_value()

    def get_state(self):
        return encode_ls_bridge(self)



