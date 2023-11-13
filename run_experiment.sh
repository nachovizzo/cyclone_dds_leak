#!/bin/bash

# build just in case :)
colcon build

# First stop, try with CycloneDDS
unset RMW_IMPLEMENTATION
RMW_IMPLEMENTATION=rmw_cyclonedds_cpp tmuxinator start project mapping -p cyclonedds.yaml
