import json

from Functions import Fader, MasterFader, Executor


def encode_ls_bridge(ls_bridge):
    fader_count = len(ls_bridge.faders)

    return_obj = {'fader': [], 'executor':[], 'master':0}
    for x in range(fader_count):
        return_obj['fader'].append(ls_bridge.get_fader_value(x + 1))

    for x in range(len(ls_bridge.executors)):
        return_obj['executor'].append([])
        for y in range(len(ls_bridge.executors[x])):
            return_obj['executor'][x].append([])
            for z in range(len(ls_bridge.executors[x][y])):
                return_obj['executor'][x][y].append(ls_bridge.get_executor_state(x+1, y+1, z+1))

    return_obj['master'] = ls_bridge.get_master_value()

    return json.dumps(return_obj)


class LightSharkBridge:
    faders = []
    executors = []
    osc_client = None
    master = None

    def __init__(self, osc_client):
        self.osc_client = osc_client

    def init_functions(self, fader_count, executor_matrix, midi_client):
        for x in range(fader_count):
            fader = Fader(x + 1, self.osc_client, midi_client, None)
            self.faders.append(fader)

        for x in range(executor_matrix[0]):
            self.executors.append([])
            for y in range(executor_matrix[1]):
                self.executors[x].append([])
                for z in range(executor_matrix[2]):
                    self.executors[x][y].append(Executor(x+1, y+1, z+1, self.osc_client, midi_client, None))

        self.master = MasterFader(self.osc_client, midi_client, 33)

    def set_fader_value(self, fader_id, value):
        self.faders[fader_id - 1].set_value(value)

    def get_fader_value(self, fader_id):
        return self.faders[fader_id - 1].get_value()

    def set_executor_state(self, x, y, z, value):
        self.executors[x-1][y-1][z-1].set_value(value)

    def get_executor_state(self, x, y, z):
        return self.executors[x-1][y-1][z-1].get_value()

    def set_master_value(self, value):
        self.master.set_value(value)

    def get_master_value(self):
        return self.master.get_value()

    def get_state(self):
        return encode_ls_bridge(self)
