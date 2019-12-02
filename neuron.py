import math
import random

import constants as c


class NEURON:

    def __init__(self, type):
        self.type = type
        self.tau = c.TAU_MIN + random.random() * (c.TAU_MAX - c.TAU_MIN)
        self.tau = round(self.tau, 15)
        self.value = 0
        self.last_val = 0
        self.ID = None

    def Get_Tau(self):
        """
        getter method for the tau
        :return: the tau
        """
        return self.tau

    def Add_Joint_Pointer(self, joint):
        self.joint = joint

    def Add_Sensor_Pointer(self, sensor):
        self.sensor = sensor

    def Send_Sensor_Neuron_To_Simulator(self, simulator):
        self.ID = simulator.send_sensor_neuron(sensor_id=self.sensor.ID, svi=0)

    def Send_Hidden_Neuron_To_Simulator(self, simulator):
        """
        Sends the hidden neuron to the simulator with details about it's initial internal activation state.
        :param simulator: A pyrosim Simulator class
        :return: None
        """
        self.ID = simulator.send_hidden_neuron(tau=self.tau, last_value=self.last_val, value=self.value)

    def Send_Motor_Neuron_To_Simulator(self, simulator):
        self.ID = simulator.send_motor_neuron(joint_id=self.joint.ID, tau=self.tau)
