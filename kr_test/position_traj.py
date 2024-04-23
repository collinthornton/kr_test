import numpy as np
from kr_msgs.msg import FollowJoint, SystemState

from gen_traj import TrajGenerator


class PositionTrajGenerator(TrajGenerator):
    def __init__(self, amplitude, period, publish_period):
        super().__init__('position_test', FollowJoint, "/kr/motion/follow_joint", publish_period)

        self.amplitude = amplitude
        self.period = period
        self.publish_period = publish_period

        self.start_position = None
        self.start_time = None
        self.subscriber = self.create_subscription(SystemState, "/kr/system/state", self.__handle_system_state, 1)

    def get_next_point(self):
        if self.start_position is None:
            raise ValueError("Haven't received starting position")

        elapsed_time = self._ros_duration_to_float(self._get_time(), self.start_time)

        output = self.amplitude*(np.cos(((2*np.pi)/self.period)*elapsed_time) - 1) + self.start_position

        msg = FollowJoint()
        msg.btype = FollowJoint.BT_TIME
        msg.bpoint = FollowJoint.BP_VIA
        msg.ttype = FollowJoint.TT_TIME

        msg.bvalue = self.publish_period
        msg.tvalue = 2. * self.publish_period

        msg.jsconf = np.degrees(output).tolist()

        return msg

    def __handle_system_state(self, msg: SystemState):
        self.start_position = np.array(msg.pos.data)
        self.start_time = self._get_time()
