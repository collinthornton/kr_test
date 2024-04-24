import numpy as np
from kr_msgs.msg import FollowJoint, SystemState

from .gen_traj import TrajGenerator


class PositionTrajGenerator(TrajGenerator):
    def __init__(self, amplitude, period, publish_period):
        super().__init__('position_test', FollowJoint, "/kr/motion/follow_joint", publish_period)

        self.__amplitude = amplitude
        self.__period = period
        self.__publish_period = publish_period

        self.__subscriber = self.create_subscription(SystemState, "/kr/system/state", self.__handle_system_state, 1)

    def get_next_point(self):
        if self._start_position is None:
            raise ValueError("Haven't received starting position")

        t = self._elapsed_time(self._start_time)
        output = self._start_position + self.__amplitude * (np.cos(((2*np.pi)/self.__period) * t) - 1.)

        msg = FollowJoint()
        msg.btype = FollowJoint.BT_TIME
        msg.bpoint = FollowJoint.BP_VIA
        msg.ttype = FollowJoint.TT_TIME

        msg.bvalue = self.__publish_period
        msg.tvalue = 2. * self.__publish_period

        msg.jsconf = np.degrees(output.tolist())

        return msg

    def __handle_system_state(self, msg: SystemState):
        self._start_position = np.radians(msg.sensed_pos.data)
        self._start_time = self._get_time()
        self.__subscriber.destroy()