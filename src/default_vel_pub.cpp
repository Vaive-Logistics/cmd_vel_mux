#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using namespace std::chrono_literals;

class CmdVelPublisher : public rclcpp::Node
{
public:
  CmdVelPublisher()
  : Node("default_cmd_vel_publisher")
  {
    // Create publisher
    cmd_vel_pub_ = this->create_publisher<geometry_msgs::msg::Twist>(
      "cmd_vel", 10);

    // Create timer (10 Hz)
    timer_ = this->create_wall_timer(
      100ms,
      std::bind(&CmdVelPublisher::timer_callback, this));

    RCLCPP_INFO(this->get_logger(), "Default CmdVel publisher node started");
  }

private:
  void timer_callback()
  {
    geometry_msgs::msg::Twist msg;

    cmd_vel_pub_->publish(msg);
  }

  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_pub_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<CmdVelPublisher>());
  rclcpp::shutdown();
  return 0;
}