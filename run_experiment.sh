#!/bin/bash

export NODE=tf2_leaky_node
# export NODE=leaky_node

# build just in case :)
# cleanup, sorry!
rm *.csv 2>/dev/null

# Kill ros2cli to avoid DDS crazyness
kill -9 $(pgrep -f '/usr/bin/python3 -c from ros2cli.daemon.daemonize') 2>/dev/null

# build just in case :)
colcon build

# First stop, try with CycloneDDS
unset RMW_IMPLEMENTATION
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
tmuxinator start project mapping -p cyclonedds.yaml

# Kill ros2cli to avoid DDS crazyness
kill -9 $(pgrep -f '/usr/bin/python3 -c from ros2cli.daemon.daemonize') 2>/dev/null

# Now go with FastDDS
unset RMW_IMPLEMENTATION
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
tmuxinator start project mapping -p fastdds.yaml

## Plot results
python3 ./plot.py
