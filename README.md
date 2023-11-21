## How to run?

`colcon build` and

- `ros2 run leaky_node leaky_node`
- `ros2 run leaky_node tf2_leaky_node`


And then observe how the memory of tf2_leaky_node increase unbounded

## Related Issues

- https://github.com/ros2/geometry2/pull/630
- https://github.com/ros2/rmw_cyclonedds/issues/471
- https://github.com/ksuszka/cyclonedds_iceoryx_memory_leak
