from abc import ABC, abstractmethod

from rclpy.node import Node
from rclpy.time import Time

class TrajGenerator(ABC, Node):
    def __init__(self, name, publisher_type, publisher_topic, publish_period):
        super().__init__(name)

        self.publisher = self.create_publisher(publisher_type, publisher_topic, 1)
        self.pub_timer = self.create_timer(publish_period, self.__handle_pub_timer)

    @abstractmethod
    def get_next_point(self):
        pass

    def _get_time(self):
        return self.get_clock().now()

    @classmethod
    def _ros_duration_to_float(cls, time_a: Time, time_b: Time) -> float:
        return (time_a - time_b).nanoseconds / 1e9

    def __handle_pub_timer(self):
        try:
            self.publisher.publish(self.get_next_point())
        except ValueError as e:
            self.get_logger().error(str(e), throttle_duration_sec=3.)
