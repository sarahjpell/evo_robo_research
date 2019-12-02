import random
import pickle
import sys
sys.path.insert(0, '../../')
import pyrosim


import constants as c

# from environment import ENVIRONMENT
# from visualization import VISUALIZATION
from evaluation import EVALUATION

class SIMULATION:

    def __init__(self, play_blind, silent_mode, wt):

        # self.positionsOfRobotsBeingSimulated = positionsOfRobotsBeingSimulated

        self.speed = c.SPEED

        #eval_time=c.evaluationTime * c.ACCURACY
        self.simulator = pyrosim.Simulator(play_blind=play_blind, play_paused=False, eval_time=50, dt = 0.05 / c.ACCURACY, window_size=(600, 600), xyz = [0.8317*2,-0.9817*2,0.8000*2], hpr = [121,-27.5*0.75,0.0])

        # self.environment = ENVIRONMENT( self.database , self.simulator )

        # self.visualization = VISUALIZATION(  )

        self.Initialize_Evaluations()

        # self.wt = 1

    def End(self):
        self.simulator.wait_to_finish()
        del self.simulator

    def Start(self):
        self.simulator.start()

    def Initialize_Evaluations(self):
        self.evaluation = EVALUATION(self.simulator, self.speed)

