#!/usr/bin/env python3      # start the shebang line
import rclpy		        # import ROS2 client library for python
from rclpy.node import Node # import Node class
from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node): # MODIFY NAME, create a node sub class based on the parent Node in rclpy
    def __init__(self): #Initializing the node class Constructor  
        super().__init__("add_two_ints_server") # MODIFY NAME, use super() function and pass the "node_name"
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("the Add Two Ints server has been started")

    def callback_add_two_ints (self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + "+" + str(request.b) + "=" + str(response.sum))
        return response

def main(args=None):
    rclpy.init(args=args) # init communication
    node = AddTwoIntsServerNode() # MODIFY NAME, create the node object from the node class
    rclpy.spin(node)      # spin the node, so the callback is alive
    rclpy.shutdown()      # stop the communication


if __name__ == "__main__": # call the main function
    main()
