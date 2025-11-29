import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(Int32, 'sensor_data', 10)
        self.timer = self.create_timer(0.5, self.publish_sensor_value)

    def publish_sensor_value(self):
        msg = Int32()
        msg.data = random.randint(0, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published sensor value: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
