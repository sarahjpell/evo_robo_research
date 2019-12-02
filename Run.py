import sys
sys.path.insert(0, '../../')
import pyrosim

from individual import INDIVIDUAL
import random
import copy
import pickle

for i in range(5):
    test = INDIVIDUAL()
    test.Evaluate(True)


# parent = INDIVIDUAL()
# parent.Evaluate(True)
# print(parent.fitness)

# for g in range(1):
#     child = copy.deepcopy(parent)
#     child.Mutate()
#     child.Evaluate(True)


    # print(parent.fitness, child.fitness)
    # if(child.fitness > parent.fitness):
    #     parent = child
    #     parent.Evaluate(False)
    #
    # print("g: ", g, "[p:", parent.fitness, " ]", " [c: ", child.fitness, "]")


# f = open('robot.p', 'wb')
# pickle.dump(parent, f)
# f.close()


#playback
# f = open('robot.p', 'rb')
# best = pickle.load(f)
# f.close()
