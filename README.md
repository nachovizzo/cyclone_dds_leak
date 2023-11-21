## How to run?

`colcon build` and

- `ros2 run leaky_node leaky_node`
- `ros2 run leaky_node tf2_leaky_node`

And then observe how the memory of tf2_leaky_node increase unbounded

## Optional running trhough `heaptrack` or `massif`

Just run the `tf2_leaky_ndoe` through such tools and observe the leak:

- `ros2 run --prefix 'heaptrack' leaky_node tf2_eaky_node`

## Related Issues

- https://github.com/ros2/geometry2/pull/630
- https://github.com/ros2/rmw_cyclonedds/issues/471
- https://github.com/ksuszka/cyclonedds_iceoryx_memory_leak
