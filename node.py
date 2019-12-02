import math
import random

from joint import JOINT
from object import OBJECT

import constants

class NODE:

    def __init__(self, parent, myDepth, maxDepth, numChildren, myAngle1, myAngle2, x, y, z):
        self.myDepth = myDepth
        # self.numChildren = numChildren
        self.numChildren = random.randint(1, numChildren)
        self.object = None
        self.joint = None
        self.myAngle1 = myAngle1
        self.myAngle2 = myAngle2
        self.x = x
        self.y = y
        self.z = z
        self.children = {}

        if (self.myDepth < maxDepth):
            self.Create_Children(maxDepth)
        else:
            self.numChildren = 0

    def First_Object(self):
        return self.children[0].object

    def Add_Joints(self, parent, grandParent):
        if(len(self.children)>1):
            if (self.myDepth == 0):
                print("MY DEPTH = 0", self.children)
                firstNode = self.children[0]
                secondNode = self.children[1]
                nodeContainingJointPosition = self
                q = self.children[0]
                p = self
                r = self.children[1]

                self.joint = JOINT(firstNode, secondNode, nodeContainingJointPosition, q, p, r)

            elif (self.myDepth == 1):
                firstNode = self.children[0]
                secondNode = self.children[1]
                nodeContainingJointPosition = self
                self.joint = None
            else:
                firstNode = self.children[0]
                secondNode = self.children[1]
                nodeContainingJointPosition = self
                firstNode = parent
                secondNode = self
                nodeContainingJointPosition = parent

                q = self
                p = parent
                r = grandParent

                self.joint = JOINT(firstNode, secondNode, nodeContainingJointPosition, q, p, r)

        for c in self.children:
            self.children[c].Add_Joints(self, parent)
    def Add_Objects(self, parent):
        if (self.myDepth == 0):
            self.object = None
        else:
            self.object = OBJECT(parent, self)

        for c in self.children:
            self.children[c].Add_Objects(self)

    def Add_Neurons(self, neurons):
        if (self.object):
            self.object.Add_Neurons(neurons)

        if (self.joint):
            self.joint.Add_Neurons(neurons)

        for c in self.children:
            self.children[c].Add_Neurons(neurons)

    def Add_Sensors(self):
        if (self.object):
            self.object.Add_Sensors()

        if (self.joint):
            self.joint.Add_Sensors()

        for c in self.children:
            self.children[c].Add_Sensors()

    def Create_Children(self, maxDepth):
        for c in range(0, self.numChildren):
            hisAngle1 = self.myAngle1 + random.random() * 2.0 * 3.14159 - 3.14159

            hisAngle2 = math.pi / 2.0

            hisX = self.x + constants.length * math.sin(hisAngle1)

            hisY = self.y + constants.length * math.cos(hisAngle1)

            hisZ = self.z

            self.children[c] = NODE(self, self.myDepth + 1, maxDepth, constants.maxChildren, hisAngle1, hisAngle2, hisX,
                                    hisY, hisZ)

    def Get_Sensor_Data_From_Simulator(self, simulator):
        if (self.object):
            self.object.Get_Sensor_Data_From_Simulator(simulator)

        for c in range(0, self.numChildren):
            self.children[c].Get_Sensor_Data_From_Simulator(simulator)

    def Number_Of_Nodes(self):
        numNodes = 1

        for c in range(0, self.numChildren):
            numNodes = numNodes + self.children[c].Number_Of_Nodes()

        return numNodes

    def Count_Sensors(self):
        numSensors = 0

        if (self.object):
            numSensors = numSensors + self.object.Num_Sensors()

        if (self.joint):
            numSensors = numSensors + self.joint.Num_Sensors()

        for c in range(0, self.numChildren):
            numSensors = numSensors + self.children[c].Count_Sensors()

        return numSensors

    def Find_Lowest_Point(self, lowestPoint):
        if (self.z < lowestPoint[0]):
            lowestPoint[0] = self.z

        for c in range(0, self.numChildren):
            self.children[c].Find_Lowest_Point(lowestPoint)

    def Move(self, x, y, z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z

        for c in range(0, self.numChildren):
            self.children[c].Move(x, y, z)

    def Send_Objects_To_Simulator(self, simulator):
        if (self.object):
            self.object.Send_To_Simulator(simulator)

        for c in self.children:
            self.children[c].Send_Objects_To_Simulator(simulator)

    def Send_Position_Sensors_To_Simulator(self, simulator):
        if (self.object):
            self.object.Send_Position_Sensor_To_Simulator(simulator)

        for c in self.children:
            self.children[c].Send_Position_Sensors_To_Simulator(simulator)

    def Send_Joints_To_Simulator(self, simulator):
        if (self.joint):
            self.joint.Send_To_Simulator(simulator)

        for c in self.children:
            self.children[c].Send_Joints_To_Simulator(simulator)

