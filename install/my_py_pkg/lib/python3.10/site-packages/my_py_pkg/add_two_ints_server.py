#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


#Write your code inside this class always
class AddTwoIntsServer(Node): #Change MyNode 
    def __init__(self):
        super().__init__("add_two_ints_server") #change test as you want your node 
        self.server=self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add ints")
    
    def callback_add_two_ints(self, request, response):
        response.sum = request.a+ request.b
        self.get_logger().info(str(request.a)+"+"+str(request.b)+"="+str(response.sum))
        return response
 
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=AddTwoIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()


