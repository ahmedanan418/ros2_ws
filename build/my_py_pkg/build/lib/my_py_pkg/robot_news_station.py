
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.publisher_=self.create_publisher(String, "robot_news", 10)
        self.create_timer(0.5,self.publish_news)
        self.get_logger().info("News Station has started")
        
            
    def publish_news(self):
        msg= String()
        msg.data="H"
        self.publisher_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node=RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()