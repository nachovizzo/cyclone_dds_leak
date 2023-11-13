import argparse

import matplotlib.pyplot as plt
import numpy as np


def main(filename):
    # Extract the column you want to plot
    data = np.genfromtxt(filename, delimiter=",")

    # Plot the data
    plt.plot(data)

    # Add labels and title
    plt.xlabel("time")
    plt.ylabel("memory usage in MiB")
    plt.title(filename)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple script to log memory consumption based on process name",
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="results.csv",
        help="Specify the input filename",
    )

    args = parser.parse_args()
    main(args.filename)
