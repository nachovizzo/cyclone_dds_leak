import matplotlib.pyplot as plt
import numpy as np


def main():
    cyclonedds = np.genfromtxt("cyclonedds.csv", delimiter=",")
    plt.figure("Cyclone DDS")
    plt.plot(cyclonedds)
    plt.xlabel("time")
    plt.title("CycloneDDS")
    plt.ylabel("memory usage in MiB")

    plt.figure("FastDDS")
    fastdds = np.genfromtxt("fastdds.csv", delimiter=",")
    plt.xlabel("time")
    plt.ylabel("memory usage in MiB")
    plt.title("FastDDS")
    plt.plot(fastdds)
    plt.show()


if __name__ == "__main__":
    main()
