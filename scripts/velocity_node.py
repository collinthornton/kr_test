#! /usr/bin/env python3

import rclpy
from kr_test import VelocityTrajGenerator


def main(args=None):
    rclpy.init(args=args)

    traj = VelocityTrajGenerator(amplitude=0.5, period=5, publish_period=0.01)
    rclpy.spin(traj)
    traj.destroy_node()
    rclpy.shutdown()
    return 0


if __name__ == '__main__':
    main()
