#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import typer


def main(csv_file: Path, plot: bool = False):
    print("Eating memory leak results from", csv_file)
    df = pd.read_csv(csv_file)

    # Filter a bit the process
    ros2_process = df.filter(like="ros2", axis=1).columns
    unnamed_process = df.filter(like="Unnamed", axis=1).columns
    bash_process = df.filter(like="bash", axis=1).columns
    python3_process = df.filter(like="python3", axis=1).columns
    columns_with_nan = df.columns[df.isna().any()].tolist()

    columns_to_drop = list(
        set(ros2_process)
        | set(columns_with_nan)
        | set(unnamed_process)
        | set(python3_process)
        | set(bash_process)
    )

    df = df.drop(columns=columns_to_drop)

    # Computes an approximate derivate to filter out process with increasing memory consumption
    derivatives = df.diff().mean()

    # Filter columns where the mean of derivatives is greater than the threshold
    min_diff = 0.05
    increasing_columns = df.columns[derivatives >= min_diff]
    steady_columns = df.columns[derivatives < min_diff]

    # Select only the columns that meet the criteria
    increasing_processes = df[increasing_columns]
    steady_processes = df[steady_columns]

    print("Processes that seems to be leaking memory:")
    print("\t" + "\n\t".join(map(str, increasing_columns)))
    print("Processes that seems to have steady memory consumption:")
    print("\t" + "\n\t".join(map(str, steady_columns)))
    print("Processes that were skipped in this analysis:")
    print("\t" + "\n\t".join(map(str, columns_to_drop)))

    if plot:
        if not increasing_processes.empty:
            increasing_processes.plot(kind="line")
        if not steady_processes.empty:
            steady_processes.plot(kind="line")
        plt.show()


if __name__ == "__main__":
    typer.run(main)
