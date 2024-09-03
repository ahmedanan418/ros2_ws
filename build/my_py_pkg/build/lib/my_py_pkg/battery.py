#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#Write your code inside this class always
class BatteryNode(Node): #Change MyNode 
    def __init__(self):
        super().__init__("battery") 
        self.battery_state="full"
        self.last_time_battery_has_changed= self.get_current_time_seconds()
        self.battery_timer=self.create_timer(0.1,self.check_battery_state)

    def get_current_time_seconds(self):
        secs, nsecs= self.get_clock().now().seconds_nanoseconds()
        return secs+nsecs/1000000000.0

    def check_battery_state(self):
        time_now= self.get_current_time_seconds()
        if self.battery_state == "full":
            if time_now-self.last_time_battery_has_changed>4.0:
                self.battery_state="empty"
                self.get_logger().info("Battery is empty! Charging ...")
                self.last_time_battery_has_changed=time_now
        else:
            if time_now-self.last_time_battery_has_changed>6.0:
                self.battery_state="full"
                self.get_logger().info("Battery charged successfully")
                self.last_time_battery_has_changed=time_now

    
#This main function will always be the same 
def main(args=None):
    rclpy.init(args=args)
    node=BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

