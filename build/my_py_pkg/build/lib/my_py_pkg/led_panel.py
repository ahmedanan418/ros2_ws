#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed


#Write your code inside this class always
class LedPanelNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("led_panel")
        self.led_states = [0,0,0]
        self.led_state_publisher=self.create_publisher(LedStateArray,"led_panel_state",10)
        self.timer= self.create_timer(4.0,self.publish_led_states)
        self.set_led_service = self.create_service(SetLed,"set_led",self.callback_set_led)
        self.get_logger().info("Panel Started!")



    def publish_led_states(self):
        msg=LedStateArray()
        msg.led_states= self.led_states
        self.led_state_publisher.publish(msg)

    def callback_set_led(self, request, response):
        led_number=request.led_number
        state= request.state

        if led_number > len(self.led_states) or led_number <= 0:
            response.success= False
            self.get_logger().warn("Invalid")
            return response

        if state not in (0,1):
            response.success= False
            self.get_logger().warn("Enter 0 or 1 only")
            return response

        self.led_states[led_number-1] = state
        response.success = True
        self.publish_led_states()
        return response
    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

