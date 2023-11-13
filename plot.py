import matplotlib.pyplot as plt
import numpy as np


def main():
    # Extract the column you want to plot
    cyclonedds = np.genfromtxt("cyclonedds.csv", delimiter=",")
    fastdds = np.genfromtxt("fastdds.csv", delimiter=",")

    # Plot the data
    plt.plot(cyclonedds)
    plt.plot(fastdds)

    # Add labels and title
    plt.xlabel("time")
    plt.ylabel("memory usage in MiB")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
