import matplotlib.pyplot as plt
import numpy as np
import json

def drawGraph():

    distance = {"Kalman":[],"Odometry":[],"Formation":[]}
    theta = {"Kalman":[],"Odometry":[],"Formation":[]}
    x = []
    """
    #Odomoetry
    x1 = []
    y1 = []

    #Kalman
    x2 = []
    y2 = []

    #Formation
    x3 = []
    y3 = []
    """

    with open('logData.txt','r') as logfile:
        for line_terminated in logfile:
            line = line_terminated.rstrip('\n')
            logDict = json.loads(line)
            k, strategies = next(iter(logDict.items()))
            x.append(k)
            for strategy in strategies:
                distance[strategy].append(strategies[strategy]["distance"])
                theta[strategy].append(strategies[strategy]["theta"])


    #x, y = np.loadtxt('logData.txt', delimiter = ',', unpack = True)


    plt.plot(x, distance["Kalman"], label='Kalman', color='b')
    plt.plot(x, distance["Odometry"], label='Odometry', color='g')
    plt.plot(x, distance["Formation"], label='Formation', color ='r')

    plt.xlabel('Time')
    plt.ylabel('Error')

    plt.title('Error Graph')
    plt.legend()

    plt.show()


drawGraph()
