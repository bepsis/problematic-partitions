import tensorflow.contrib.learn as skflow
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVR

# True partition function using recursive algorithm
def partition(n):
    answer = set()
    answer.add((n, ))
    for x in range(1, n):
        for y in partition(n - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

# Ramanujan's approximation of the partition function
def approximate_partition(n):
    answer = (1/(4*n*math.sqrt(3)))*math.exp(math.pi*math.sqrt(2*n/3))
    return answer

def main():
    print(len(partition(10)))
    print(approximate_partition(10))

    partitionX = []
    for x in range(1, 20):
        partitionX.append(x)
    actualPartitionY = []
    approximatePartitionY = []
    for x in range(0, len(partitionX)):
        actualPartitionY.append(len(partition(partitionX[x])))
        approximatePartitionY.append(approximate_partition(partitionX[x]))

    regressor = SVR(kernel='rbf', C=1e3, gamma=0.1)
    trainingX = []
    for x in range(0, len(partitionX)):
        tmp = []
        tmp.append(partitionX[x])
        trainingX.append(tmp)
    trainingY = []
    for x in range(0, len(partitionX)):
        tmp = []
        tmp.append(actualPartitionY[x])
        trainingY.append(tmp)

    print(trainingX)
    print(trainingY)
    regressor.fit(np.asarray(trainingX, dtype=np.int32), np.asarray(trainingY, dtype=np.int32))
    print(regressor.predict(np.asarray([10], dtype=np.int32)))

    estimatedRegressorY = []
    for x in range(0, len(partitionX)):
        tmp = []
        tmp.append(partitionX[x])
        estimatedRegressorY.append(regressor.predict(np.asarray(tmp, dtype=np.int32))[0])

    plt.plot(partitionX, actualPartitionY)
    plt.plot(partitionX, approximatePartitionY)
    plt.plot(partitionX, estimatedRegressorY)

    plt.show()

if __name__ == "__main__":
    main()
