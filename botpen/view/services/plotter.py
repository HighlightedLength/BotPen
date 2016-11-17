import matplotlib.pyplot as plt
import numpy as np


def drawGraph():
    #line1
    x1 = []
    y1 = []

    #line2
    x2 = []
    y2 = []

    """
    with open('logData.txt','r') as myfile:
        plots = csv.reader(myfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
    """

    

    x, y = np.loadtxt('logData.txt', delimiter = ',', unpack = True)


    plt.plot(x1,y1, label='First Line', color='b')
    plt.plot(x2, y2, label='Second Line', color='g')

    plt.xlabel('Time')
    plt.ylabel('Error')

    plt.title('Error Graph')
    plt.legend()

    plt.show()
