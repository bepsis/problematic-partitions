import tensorflow.contrib.learn as skflow
import matplotlib.pyplot as plt
import math

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
    for x in range(1, 22):
        partitionX.append(x)
    actualPartitionY = []
    approximatePartitionY = []
    for x in range(0, len(partitionX)):
        actualPartitionY.append(len(partition(partitionX[x])))
        approximatePartitionY.append(approximate_partition(partitionX[x]))


    plt.plot(partitionX, actualPartitionY)
    plt.plot(partitionX, approximatePartitionY)

    plt.show()

if __name__ == "__main__":
    main()
