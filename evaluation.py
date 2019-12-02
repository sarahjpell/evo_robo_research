import sys

import sys
sys.path.insert(0, '../../')
import pyrosim


import constants as c
from robot import ROBOT
# from environment import ENVIRONMENT

class EVALUATION:

    def __init__(self,simulator,speed):
        self.sim = simulator

        # self.environment = environment

        self.robot = ROBOT(self.sim)

        self.speed = speed

    def Start(self):
        # self.environment.Send_To_Simulator(self.positionOffset, self.drawOffset, self.fadeStrategy)
        #
        # summedPositionOffset = tuple(map(sum, zip(self.environment.Get_Robot_Offset(), self.positionOffset)))

        self.robot.Send_To_Simulator(self.sim)
