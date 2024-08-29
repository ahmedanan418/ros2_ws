#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#Write your code inside this class always
class BatteryNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("battery") 
        self.battery_state="full"
    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

