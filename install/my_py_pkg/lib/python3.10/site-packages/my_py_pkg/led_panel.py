#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray


#Write your code inside this class always
class LedPanelNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("led_panel")
        self.led_states = [0,0,0]
        self.led_state_publisher=self.create_publisher(LedStateArray,"led_state",10)
        self.timer= self.create_timer(4.0,self.publish_led_states)
        self.get_logger().info("Led Panel Started!")



    def publish_led_states(self):
        msg=LedStateArray()
        msg.led_states= self.led_states
        self.led_state_publisher.publish(msg)

    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

