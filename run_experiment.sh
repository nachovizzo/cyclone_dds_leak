#!/bin/bash

# build just in case :)
# cleanup, sorry!
rm *.csv

# build just in case :)
colcon build

# First stop, try with CycloneDDS
unset RMW_IMPLEMENTATION
RMW_IMPLEMENTATION=rmw_cyclonedds_cpp tmuxinator start project mapping -p cyclonedds.yaml

# Now go with FastDDS
unset RMW_IMPLEMENTATION
RMW_IMPLEMENTATION=rmw_fastrtps_cpp tmuxinator start project mapping -p fastdds.yaml

## Plot results
python3 ./plot.py
