#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64



#Write your code inside this class always
class NumberCounter(Node): #Change MyNode 
    def __init__(self):
        super().__init__("number_counter") #change test as you want your node 
        self.counter=0
        self.number_counter_publisher=self.create_publisher(Int64,"final_number",10)
        self.number_subscriber=self.create_subscription(Int64, "number_publisher",self.callback_number, 10)
        self._logger.info("Number Counter started")

    def callback_number(self,msg):
        self.counter+=msg.data
        new_msg=Int64()
        new_msg.data=self.counter
        self.number_counter_publisher.publish(new_msg)

        

#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()