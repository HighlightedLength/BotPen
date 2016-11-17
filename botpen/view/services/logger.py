import json
import numpy as np
import math
from pprint import pprint
import os

class Logger:
    config = None

    def setup(self, config):
        self.config = config

    def log(self, view):
        output_path = self.config.get("output_path")

        agents = view['agents']
        agent_count = len(agents)
        result = {}

        for strategy in view['estimates']:
            estimates = (
                view['estimates'][strategy]['estimates']
                if strategy == 'Formation'
                else view['estimates'][strategy]
            )

            distance = 0
            angle = 0
            for agent in agents:
                dx_squared = math.pow(estimates[agent.id].x - agent.x,2)
                dy_squared = math.pow(estimates[agent.id].y - agent.y,2)
                abs_dtheta = abs(estimates[agent.id].theta%(2*math.pi) - agent.theta%(2*math.pi))

                distance += math.sqrt(dx_squared + dy_squared)
                angle += abs_dtheta%(2*math.pi)

            result[strategy] = {
                'distance' : distance/agent_count,
                'angle': angle/agent_count
            }

        dest = os.path.abspath(output_path)
        print(dest)
        with open(os.path.abspath(output_path), 'a') as f:
            f.write(json.dumps(result))
            f.write('\n')
