import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class DataProcessor(Node):
    def __init__(self):
        super().__init__('data_processor')
        self.subscription = self.create_subscription(
            Int32,
            'sensor_data',
            self.listener_callback,
            10)

        self.publisher_ = self.create_publisher(Int32, 'processed_data', 10)

    def listener_callback(self, msg):
        processed = msg.data * 10
        out_msg = Int32()
        out_msg.data = processed
        self.publisher_.publish(out_msg)
        self.get_logger().info(f'Received {msg.data} -> Processed {processed}')

def main(args=None):
    rclpy.init(args=args)
    node = DataProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
