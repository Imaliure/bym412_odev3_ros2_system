import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class CommandServer(Node):
    def __init__(self):
        super().__init__('command_server')

        self.subscription = self.create_subscription(
            Int32,
            'processed_data',
            self.listener_callback,
            10)

        self.publisher_ = self.create_publisher(String, 'command_output', 10)

    def listener_callback(self, msg):
        value = msg.data
        command = "HIGH" if value > 500 else "LOW"

        out_msg = String()
        out_msg.data = command
        self.publisher_.publish(out_msg)

        self.get_logger().info(f'Processed {value} -> Command: {command}')

def main(args=None):
    rclpy.init(args=args)
    node = CommandServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
