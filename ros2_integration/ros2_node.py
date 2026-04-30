import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AAMOptimusNode(Node):
    def __init__(self):
        super().__init__('aam_optimus_node')
        self.subscriber = self.create_subscription(String, 'sensor_topic', self.sensor_callback, 10)
        self.publisher = self.create_publisher(String, 'control_commands', 10)
        self.get_logger().info('AAM Optimus Node has been created.')

    def sensor_callback(self, msg):
        self.get_logger().info(f'Received sensor data: {msg.data}')
        control_command = self.process_sensor_data(msg.data)
        self.publisher.publish(String(data=control_command))

    def process_sensor_data(self, data):
        # Processing sensor data and generating control command
        # Placeholder implementation - replace with actual logic
        return 'control_command_based_on_' + data

def main(args=None):
    rclpy.init(args=args)
    aam_optimus_node = AAMOptimusNode()
    rclpy.spin(aam_optimus_node)
    aam_optimus_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()