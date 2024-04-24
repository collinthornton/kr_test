import numpy as np

from kr_msgs.msg import JogJoint

from .gen_traj import TrajGenerator


class VelocityTrajGenerator(TrajGenerator):
    def __init__(self, amplitude, period, publish_period):
        super().__init__('velocity_test', JogJoint, '/kr/motion/jog_joint', publish_period)

        self.__amplitude = amplitude
        self.__period = period
        self.__publish_period = publish_period

    def get_next_point(self):
        t = self._elapsed_time(self._start_time)
        output = np.zeros((7,)) + self.__amplitude * np.sin(((2*np.pi)/self.__period)*t)

        msg = JogJoint()
        msg.jsvel = np.degrees(output.tolist())

        return msg
