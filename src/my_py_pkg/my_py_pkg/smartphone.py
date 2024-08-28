#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


#Write your code inside this class always
class SmartPhone(Node):
    def __init__(self):
        super().__init__("smartphone")
        self.subscriber=self.create_subscription(String,"robot_news",self.callback_robot_news,10)
        self._logger.info("Smart phone initialized")

    def callback_robot_news(self,msg):
        self.get_logger().info(msg.data)


#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=SmartPhone()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()



