# Copyright Dexory 2023 (c)
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


if __name__ == "__main__":
    name = "leaky_node"
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
        time.sleep(sleep_for)
