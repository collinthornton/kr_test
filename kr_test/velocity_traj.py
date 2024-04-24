import numpy as np

from kr_msgs.msg import JogJoint

from .gen_traj import TrajGenerator


class VelocityTrajGenerator(TrajGenerator):
    def __init__(self, amplitude, period, publish_period):
        super().__init__('velocity_test', JogJoint, '/kr/motion/jog_joint', publish_period)

        self.amplitude = amplitude
        self.period = period
        self.publish_period = publish_period

        self.start_time = self._get_time()

    def get_next_point(self):
        elapsed_time = self._ros_duration_to_float(self._get_time(), self.start_time)
        output = np.zeros((7,)) + self.amplitude * np.sin(((2*np.pi)/self.period)*elapsed_time)

        msg = JogJoint()
        msg.jsvel = np.degrees(output.tolist())

        return msg
