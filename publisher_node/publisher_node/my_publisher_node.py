import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')

        # Create publisher: message type, topic name, queue depth
        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        # Publish every 0.5 seconds
        self.timer_ = self.create_timer(0.5, self.publish_message)

        self.count_ = 0

    def publish_message(self):
        msg = String()
        msg.data = f'Hello ROS 2 #{self.count_}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.count_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()