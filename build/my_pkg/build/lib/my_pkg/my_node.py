"""Basic ROS 2 Python node for my_pkg."""

import rclpy
from rclpy.node import Node


class MyNode(Node):
    """A minimal node that periodically logs a message."""

    def __init__(self) -> None:
        super().__init__('my_node')
        self._timer = self.create_timer(1.0, self._on_timer)
        self._count = 0

    def _on_timer(self) -> None:
        self._count += 1
        self.get_logger().info(f'Hello from my_pkg! Count: {self._count}')


def main(args=None) -> None:
    """Initialize and spin the node."""
    rclpy.init(args=args)
    node = MyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
