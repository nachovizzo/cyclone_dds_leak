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
        tf_buffer = std::make_unique<tf2_ros::Buffer>(this->get_clock());
        tf_listener = std::make_unique<tf2_ros::TransformListener>(*tf_buffer);
    }
    std::unique_ptr<tf2_ros::TransformListener> tf_listener;
    std::unique_ptr<tf2_ros::Buffer> tf_buffer;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<LeakyNode>("tf2_leaky_node");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
