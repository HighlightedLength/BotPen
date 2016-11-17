from collections import namedtuple

class ParametricBehaviorRepo:
    def __init__(self):
        self.behaviors = {}
        self.time_cache = {}

    def add_behavior(self, agent_id, behavior):
        if not (agent_id in self.behaviors):
            self.behaviors[agent_id] = []
            self.time_cache[agent_id] = (0, behavior)
        self.behaviors[agent_id].append(behavior)

    def get(self, agent_id, time):
        (index, value) = self.time_cache[agent_id]

        result = value
        behavior_total = len(self.behaviors[agent_id])

        #check if need to search from beginning
        before_current = time < value.time
        if before_current:
            index = 0
            value = self.behaviors[agent_id][0]

        while ( index + 1 < behavior_total and
                time >= self.behaviors[agent_id][index + 1].time):
            index += 1
            result = self.behaviors[agent_id][index]
        self.time_cache[agent_id] = (index, result)

        return result
