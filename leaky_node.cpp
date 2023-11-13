#include <cstdio>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

//
#include <rclcpp/executors/single_threaded_executor.hpp>
#include <rclcpp/node.hpp>

class LeakyNode : public rclcpp::Node {
public:
    explicit LeakyNode(const std::string &name) : Node(name) {
        this->declare_parameter("my_parameter", "world");
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);

    const size_t N_NODES = 10;
    std::vector<std::shared_ptr<LeakyNode>> nodes;
    std::cerr << "Creating " << N_NODES << " nodes" << std::endl;
    for (int i = 0; i < N_NODES; ++i) {
        nodes.push_back(std::make_shared<LeakyNode>(("leaky_node" + std::to_string(i))));
    }

    std::cerr << "Adding to executor now" << std::endl;
    rclcpp::executors::SingleThreadedExecutor exec;
    for (auto &node : nodes) exec.add_node(node);

    exec.spin();
    rclcpp::shutdown();
    return 0;
}
