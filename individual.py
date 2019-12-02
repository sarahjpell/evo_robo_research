import sys
sys.path.insert(0, '../../')
import pyrosim

from robot import ROBOT
from simulation import SIMULATION
import constants as c
import random
import math

class INDIVIDUAL:
    def __init__(self):

        self.genome = random.random()*2-1
        self.fitness = 0


    def Evaluate(self, pb):
        self.sim = SIMULATION(False, True, self.fitness)

        self.sim.Start()

        self.sim.End()

    def Mutate(self):
        self.genome = random.gauss( self.genome , math.fabs(self.genome) )


