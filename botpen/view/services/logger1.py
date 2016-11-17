import json
import numpy as np
from math import pi

class Counter(dict):
    def __missing__(self,key):
        return 0

class Logger:
    config = None

    def setup(self, config):
        self.config = config

    def log(self, view):
        output_path = self.config.get("output_path")

        #process data and calculate errors
        logData = {}

        errDict = {}
        for strategy in view['estimates']:
            print("strategy = ", strategy)
            estimates = (
                view['estimates']['Formation']['estimates']
                if(strategy == "Formation")
                else view['estimates'][strategy])

            errXY = []
            errZ = 0
            errTheta = 0

            for agent in estimates:
                print(estimates[agent])
                print(view['agents'][int(agent)-1])
                errXY.append(estimates[agent].x - view['agents'][int(agent)-1].x)
                errXY.append(estimates[agent].y - view['agents'][int(agent)-1].y)
                errZ += np.sqrt(np.sum(np.power(errXY,2)))
                errTheta += estimates[agent].theta - view['agents'][int(agent)-1].theta
            errDict[strategy] = {}
            errDict[strategy]['distance'] = errZ
            errDict[strategy]['theta'] = errTheta%pi

        logData[view['time']] = errDict

        #logData[view['time']] = view['estimates']
        f = open('logData.txt',"a")
        logStr = json.dumps(logData)
        logStr += '\n'
        f.write(logStr)

        print("in logger: {0}".format(output_path))
