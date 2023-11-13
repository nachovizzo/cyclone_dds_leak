## How to generate the leak?

1. `colcon build`
2. `ros2 run leaky_node leaky_node`
3. `python3 memreport.py`
4. `bash ./leak.sh`
