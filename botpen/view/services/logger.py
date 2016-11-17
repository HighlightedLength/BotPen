import json
import numpy as np

class Logger:
    config = None

    def setup(self, config):
        self.config = config

    def log(self, view):
        output_path = self.config.get("output_path")

        #process data and calculate errors
        logData = {}

        errDict = {}
        """
        for strategy in view['estimates']:
            if(strategy == "Formation"):
                continue
            errXY = []
            for agent in view['estimates'][strategy]:
                errXY[0] = agent[1] - view['agents'][agent][1]
                errXY[1] = agent[2] - view['agents'][agent][2]

                #odoErrZ += np.sqrt(np.sum(np.pow(odoErr,2)))
            errDict[strategy][0] = np.sqrt(np.sum(np.pow(errXY,2)))
            errDict[strategy]
        """

        logData[view['time']] = view['estimates']
        f = open('logData.txt',"a")
        logStr = json.dumps(logData)
        logStr += '\n'
        f.write(logStr)

        print("in logger: {0}".format(output_path))
