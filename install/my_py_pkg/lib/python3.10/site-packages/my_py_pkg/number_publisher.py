#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.msg import Int64

#Write your code inside this class always
class NumberPublisher(Node): #Change MyNode 
    def __init__(self):
        super().__init__("number_publisher") #change test as you want your node 
        self.number=2
        self.number_publisher=self.create_publisher(Int64, "number_publisher", 10)
        self.create_timer(1.0,self.publish_number)
        self.get_logger().info("Number Publisher started")

    def publish_number(self):
        msg=Int64()
        msg.data=self.number
        self.number_publisher.publish(msg)



#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()


