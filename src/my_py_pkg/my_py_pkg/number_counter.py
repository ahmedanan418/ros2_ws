#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool




#Write your code inside this class always
class NumberCounter(Node): #Change MyNode 
    def __init__(self):
        super().__init__("number_counter") #change test as you want your node 
        self.counter=0
        self.number_counter_publisher=self.create_publisher(Int64,"final_number",10)
        self.number_subscriber=self.create_subscription(Int64, "number_publisher",self.callback_number, 10)
        self.reset_counter_service= self.create_service(SetBool, "reset_counter", self.callback_reset_counter)
        self._logger.info("Number Counter started")

    def callback_number(self,msg):
        self.counter+=msg.data
        new_msg=Int64()
        new_msg.data=self.counter
        self.number_counter_publisher.publish(new_msg)

    def callback_reset_counter(self, request, response):
        if request.data:
            self.counter= 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Failed"
        return response

        

#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()