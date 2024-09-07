#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs .msg import Twist 


#Write your code inside this class always
class TurtleControllerNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("turtle_controller") #change test as you want your node 

        self.target_x = 8.0
        self.target_y = 4.0
        self.pose=None

        self.cmd_vel_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer= self.create_timer(0.01, self.control_loop)



    def callback_turtle_pose(self, msg):
        self.pose= msg

    def control_loop(self ):
        if self.pose == None:
            return
        
        dist_x = self.target_x - self.pose.x
        dist_y = self.target_y - self.pose.y
        distance= math.sqrt(dist_x*dist_x + dist_y*dist_y)

        msg = Twist()

        if distance > 0.5:
            # position
            msg.linear.x = 2*distance

            # orientation
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose.theta
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi

            msg.angular.z = 6*diff
        else:
            # target reached!
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.cmd_vel_publisher.publish(msg)
    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

