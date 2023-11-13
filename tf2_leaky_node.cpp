#include <tf2_ros/buffer.h>
#include <tf2_ros/transform_listener.h>

#include <iostream>
#include <memory>
#include <rclcpp/node.hpp>
#include <string>
#include <vector>

class LeakyNode : public rclcpp::Node {
public:
    explicit LeakyNode(const std::string &name) : Node(name) {
        this->declare_parameter("my_parameter", "world");
        tf_buffer = std::make_unique<tf2_ros::Buffer>(this->get_clock());
        tf_listener = std::make_unique<tf2_ros::TransformListener>(*tf_buffer);
    }
    std::unique_ptr<tf2_ros::TransformListener> tf_listener;
    std::unique_ptr<tf2_ros::Buffer> tf_buffer;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::executors::SingleThreadedExecutor exec;

    std::vector<std::shared_ptr<LeakyNode>> nodes;
    const size_t N_NODES = 10;
    std::cerr << "Creating " << N_NODES << " nodes" << std::endl;
    for (int i = 0; i < N_NODES; ++i) {
        nodes.push_back(std::make_shared<LeakyNode>(("leaky_node" + std::to_string(i))));
    }

    std::cerr << "Adding to executor now" << std::endl;
    for (auto &node : nodes) exec.add_node(node);

    // spin and then shutdoun
    exec.spin();
    rclcpp::shutdown();
    return 0;
}
