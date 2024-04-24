import rclpy
from kr_test import PositionTrajGenerator


def main(args=None):
    rclpy.init(args=args)

    traj = PositionTrajGenerator(amplitude=0.1, period=10, publish_period=0.01)
    rclpy.spin(traj)
    traj.destroy_node()
    rclpy.shutdown()
    return 0


if __name__ == '__main__':
    main()
