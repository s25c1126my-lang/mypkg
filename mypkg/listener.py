import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("listener")


def cb(msg):                                           #メッセージが届くたびに呼ばれる
    node.get_logger().info("Listen: %d" % msg.data)    #msgの中身をログとして表示


def main():
    sub = node.create_subscription(Int16, "countup", cb, 10)  #型、トピック名、コールバック、キュー長
    rclpy.spin(node)