#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs .msg import Twist 


#Write your code inside this class always
class TurtleControllerNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("turtle_controller") #change test as you want your node 
        self.pose=None
        self.cmd_vel_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)



    def callback_turtle_pose(self, msg):
        self.pose= msg
    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

