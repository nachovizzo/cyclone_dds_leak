#!/bin/bash
# In 10 steps spit a string payload to the /parameter_events for each leaky node

# a big string
payload=$(printf 'X%.0s' {1..100000})

for step in {1..100}; do
    echo "Leaking step $step ..."
    for i in {0..9}; do
        ros2 param set /leaky_node${i} my_parameter ${payload} >/dev/null &
    done
    sleep 2
done
