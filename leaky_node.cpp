#include <tf2_ros/tf2_ros/transform_broadcaster.h>

#include <cstdio>
#include <memory>
#include <rclcpp/executors.hpp>
#include <rclcpp/logger.hpp>
#include <rclcpp/node.hpp>
#include <string>

class LeakyNode : public rclcpp::Node {
public:
    explicit LeakyNode(const std::string &name) : Node(name) {
        // Capture the moment where the node is created
        fixed_timestamp = this->get_clock()->now();
        // Create a tf broadcaster to send over the wire dummy transformations
        tf_broadcaster_ = std::make_unique<tf2_ros::TransformBroadcaster>(*this);
        // Control the publishing with a timer, do it fast to observe the "leak" right away
        timer_ = create_wall_timer(std::chrono::duration<double>(1.0 / publish_rate_),
                                   std::bind(&LeakyNode::timerCallback, this));
    }

    void timerCallback() {
        geometry_msgs::msg::TransformStamped dummy_pose;
        dummy_pose.header.stamp = fixed_timestamp;  // does not change (application error)
        dummy_pose.child_frame_id = "jose";
        dummy_pose.header.frame_id = "pepe";
        tf_broadcaster_->sendTransform(dummy_pose);
    }

    std::unique_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
    rclcpp::TimerBase::SharedPtr timer_;
    double publish_rate_ = 1000.0;
    rclcpp::Time fixed_timestamp;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);

    auto node = std::make_shared<LeakyNode>("leaky_node");
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}
