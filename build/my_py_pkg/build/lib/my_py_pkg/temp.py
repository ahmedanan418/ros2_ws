#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#Write your code inside this class always
class MyNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("test") #change test as you want your node 
    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

