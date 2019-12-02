import constants as c

from positionSensor import POSITION_SENSOR
from raySensor import RAY_SENSOR



class HEAD:

    def __init__(self, x, y, z, objectToAttachEyesTo):
        self.x = x
        self.leftEyeX = x - c.eyeRadius * 0.67
        self.rightEyeX = x + c.eyeRadius * 0.67
        self.y = y
        self.pupilY = y - c.eyeRadius * 0.67
        self.beamY = self.pupilY - c.pupilRadius
        self.z = z # + c.eyeRadius
        self.objectToAttachEyesTo = objectToAttachEyesTo
        self.lo = 0  # -0.1
        self.hi = 0  # +0.1
        self.Initialize_Sensors()

    def Add_Neurons(self, neurons):
        neurons.Add_Sensor_Neuron(self.leftRaySensor, c.SENSOR_NEURON)
        neurons.Add_Sensor_Neuron(self.rightRaySensor, c.SENSOR_NEURON)
        # neurons.Add_Sensor_Neuron(sensor=None, type=c.AUDITORY_NEURON)
        neurons.Add_Motor_Neuron(self)

    def Initialize_Sensors(self):
        self.leftRaySensor = RAY_SENSOR()
        self.rightRaySensor = RAY_SENSOR()
        self.rightEyePositionSensor = POSITION_SENSOR()
        self.leftEyePositionSensor = POSITION_SENSOR()

    def Get_Sensor_Data_From_Simulator(self, simulator):
        self.rightEyePositionSensor.Get_Data_From_Simulator(simulator)
        self.leftEyePositionSensor.Get_Data_From_Simulator(simulator)

    # def Get_Head_Positions(self):
    #     return self.rightEyePositionSensor.Get_Values()
    #
    # def Get_Eye_Positions(self):
    #     return (self.leftEyePositionSensor.Get_Values(), self.rightEyePositionSensor.Get_Values())

    def Send_Joints_To_Simulator(self, simulator):
        # # x = self.leftEyeX + positionOffset[0]
        # x = self.x + positionOffset[0]
        # y = self.y + positionOffset[1]
        # z = self.z + positionOffset[2]

        x = self.x
        y = self.y
        z = self.z

    def Send_Objects_To_Simulator(self, simulator):
        # x = self.leftEyeX + positionOffset[0]
        # y = self.y + positionOffset[1]
        # z = self.z + positionOffset[2]
        x = self.leftEyeX
        y = self.y
        z = self.z

    def Send_Sensors_To_Simulator(self, simulator):
        # x = self.leftEyeX + positionOffset[0]
        # x = positionOffset[0]
        # y = self.beamY + positionOffset[1]
        # z = self.z + positionOffset[2]
        x = self.leftEyeX
        y = self.beamY
        z = self.z

        # x = self.rightEyeX + positionOffset[0]
