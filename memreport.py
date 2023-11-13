# Copyright Dexory 2023 (c)
import argparse
import time
from typing import Dict

import psutil


def get_memory_usage(pname="leaky_node") -> float:
    memory_rss = 0.0
    __bytes_to_mbytes = 1 / (1024 * 1024)
    for process in psutil.process_iter(["name", "memory_info"]):
        try:
            name = f"{process.info['name']}"
            if pname not in name:
                continue
            memory_rss = process.info["memory_info"].rss * __bytes_to_mbytes
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return memory_rss


def main(filename, name, duration):
    # Your script logic here
    print(f"Processing file: {filename}")
    filename = "results.csv"
    sleep_for = 1.0  # seconds
    print(
        f"Logging memory consumption of pid: {name} to: {filename} every {sleep_for} seconds..."
    )
    f = open(filename, "w")
    print(f"{name},", file=f, end="")
    print("", file=f)
    f.close()
    while True:
        memory_usage = get_memory_usage(name)
        f = open(filename, "a")
        print(f"{memory_usage:.4f},", file=f, end="")
        print("", file=f)
        f.close()
        time.sleep(duration)


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
    parser.add_argument(
        "-d",
        "--duration",
        type=int,
        default=1,
        help="Time rate to control how fast we log (in seconds)",
    )
    parser.add_argument(
        "-p",
        "--process_name",
        default="leaky_node",
        help="Specify the process name to log",
    )

    args = parser.parse_args()
    main(
        args.filename,
        args.process_name,
        args.duration,
    )
