#!/usr/bin/env python3      # start the shebang line
import rclpy
from rclpy import client		        # import ROS2 client library for python
from rclpy.node import Node # import Node class
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClientNode(Node): # MODIFY NAME, create a node sub class based on the parent Node in rclpy
    def __init__(self): #Initializing the node class Constructor  
        super().__init__("add_two_ints_client") # MODIFY NAME, use super() function and pass the "node_name"
        self.call_add_two_ints_server(7, 9)
        self.call_add_two_ints_server(5, 10)
        self.call_add_two_ints_server(20, 50)


    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the Server to add two ints..")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_add_two_ints, a=a, b=b))

    def callback_add_two_ints (self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + "+" + str(b) + "=" + str(response.sum))
        except Exception as e:
            self.get_logger().error("service all faild %r" %(e,))

def main(args=None):
    rclpy.init(args=args) # init communication
    node = AddTwoIntsClientNode() # MODIFY NAME, create the node object from the node class
    rclpy.spin(node)      # spin the node, so the callback is alive
    rclpy.shutdown()      # stop the communication


if __name__ == "__main__": # call the main function
    main()
