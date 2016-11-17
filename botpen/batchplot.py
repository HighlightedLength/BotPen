import botpen
import argparse, os
import matplotlib.pyplot as plt
import math
import numpy as np
import json

means = {"Kalman":[],"Odometry":[],"Formation":[]}
variances = {"Kalman":[],"Odometry":[],"Formation":[]}
normalizedKalman = []
normalizedFormation = []

def batch():
    argparser = argparse.ArgumentParser(prog = "batchplot")
    argparser.add_argument('directory', help='a format for the output path')
    argparser.add_argument('output_path', help='the output file')

    args = argparser.parse_args()

    logs = os.listdir(args.directory)

    print("output {0}".format(args.output_path))

    i = 0
    for log in logs:
        rel_path = os.path.join(args.directory,log)
        abs_path = os.path.abspath(rel_path)

        print(abs_path)

        #code for ploting the graph
        """
        # for horizontal time axis
        x = []
        x.append(i)
        i += 1
        """

        estimation_strategies = ["Kalman", "Odometry", "Formation"]

        distance = {"Kalman":[],"Odometry":[],"Formation":[]}
        theta = {"Kalman":[],"Odometry":[],"Formation":[]}
        with open(abs_path,'r') as logfile:
            for line_terminated in logfile:
                line = line_terminated.rstrip('\n')
                logDict = json.loads(line)
                #k, strategies = next(iter(logDict.items()))
                #x.append(k)
                for strategy in logDict:
                    distance[strategy].append(logDict[strategy]["distance"])
                    theta[strategy].append(logDict[strategy]["angle"])

            mean = 0
            variance = 0
            for strategy in estimation_strategies:
                mean = sum(distance[strategy])/float(len(distance[strategy]))
                means[strategy].append(mean)
                for value in distance[strategy]:
                    variance += np.power(value-mean, 2)
                variance = variance/float(len(distance))
                variances[strategy].append(variance)

            normalizedKalman.append(means["Kalman"][-1]/means["Odometry"][-1])
            normalizedFormation.append(means["Formation"][-1]/means["Odometry"][-1])




    #x, y = np.loadtxt('logData.txt', delimiter = ',', unpack = True)
    plt.figure(1)
    plt.plot(np.array(means["Kalman"]), label='Kalman mean', color='b')
    plt.plot(np.array(means["Odometry"]), label='Odometry mean', color='g')
    plt.plot(np.array(means["Formation"]), label='Formation mean', color ='r')

    plt.xlabel('Time')
    plt.ylabel('Error')

    plt.title('Graph of error(mean)')
    plt.legend()

    plt.figure(2)
    plt.plot(np.array(variances["Kalman"]), label='Kalman variance', color='b')
    plt.plot(np.array(variances["Odometry"]), label='Odometry variance', color='g')
    plt.plot(np.array(variances["Formation"]), label='Formation variance', color ='r')

    plt.xlabel('Time')
    plt.ylabel('Error')

    plt.title('Graph of error(variance)')
    plt.legend()

    plt.figure(3)
    plt.plot(np.array(normalizedKalman), label="Kalman mean normalized", color='b')
    plt.plot(np.array(normalizedFormation), label="Formation mean normalized", color='r')

    plt.xlabel('Time')
    plt.ylabel('Error')

    plt.title('Graph of mean normalized error')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    batch()
