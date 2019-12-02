import numpy
import random
from body import BODY
from brain import BRAIN

class ROBOT:

    def __init__(self, sim):
        # self.Set_ID(ID)
        self.body = BODY()  #add hinges, objects
        self.brain = BRAIN(self.body)   #add neurons, synapses
        self.body.Add_Head()
        self.body.Send_To_Simulator(sim)

    def Set_ID(self, ID):
        self.ID = ID

    def Compute_Initial_State(self):

        # create 2d Matrix of synapses, and activation states
        synapses = self.Get_Hidden_Neuron_Synapses()
        synapses_transpose = synapses.transpose()  # We need to compute the transpose for calculating the dot product

        # get the tau values
        taus = self.Get_Hidden_Neuron_Tau()

        # get the alpha values. Currently these are all 1
        # Note: Multiplying two numpy 1D arrays will work if either one is a 1x1 array,
        # or if they are both the same shape. Either element-wise multiplication, or multiply the 1x1 element with all
        # elements in the other array.
        alphas = numpy.array([1])

        current_activations = numpy.zeros(5)
        last_activations = numpy.zeros(5)
        inputs = numpy.zeros(6)  # 5 hidden neurons + 1 auditory neuron for input to 5 hidden neurons.

    def Evaluate(self, simulator, whatToMaximize):
        self.body.Get_Sensor_Data_From_Simulator(simulator)

        return self.body.Compute_Fitness(whatToMaximize)

    def Get_Hidden_Neuron_Synapses(self):
        """
        :return: 6x5 matrix of the hidden synapses. Each row column represents a hidden neuron. Each row represents
                that specific hidden neuron's synapse weights to the other hidden neurons and the auditory neuron.
                The last row is the hidden neuron to auditory neuron synapse weights.
        """
        return self.brain.Get_Hidden_Neuron_Synapses()

    def Get_Hidden_Neuron_Tau(self):
        """
        :return: a 1x5 matrix of the hidden neuron tau values.
        """
        return self.brain.Get_Hidden_Neuron_Tau()

    # def Get_ID(self):
    #
    #     return self.ID

    def Mutate(self):
        mutType = random.randint(0, 1)

        if (mutType == 0):

            mutateBody = self.body.Mutate()

        else:
            self.brain.Mutate()
            mutateBody = False

        self.Reset()

        return mutateBody

    def Num_Body_Parts(self):
        return self.body.Num_Body_Parts()

    def Num_Joints(self):
        return self.body.numJoints

    def Num_Neurons(self):
        return self.brain.numNeurons

    def Num_Sensors(self):
        return self.body.numSensors

    # def Print(self):
    #     self.body.Print()
    #     self.brain.Print()

    def Reset(self):
        self.body.Reset()
        self.brain.Reset(self.body)

    def Set_Hidden_Neuron_State(self, last_vals, vals):
        """
        Sets the initial internal states of the hidden neurons to support speaking a command to the robot during prenatal
        development.
        :param vals: List of current activation of hidden neurons
        :param last_vals: List of last activation of hidden neurons
        :return: None
        """
        self.brain.Set_Hidden_Neuron_State(last_vals, vals)

    def Send_To_Simulator(self, simulator):
        """
        Takes a robot and a command, preforms the prenatal development of the robot using numpy and then sends the
        developed robot to the simulator to be simulated.
        :param simulator: A pyrosim simulation engine
        :type simulator: A pyrosim.Simulator
        :param positionOffset:
        :param drawOffset:
        :return: None
        """


        self.body.Send_To_Simulator(simulator)
        self.brain.Send_To_Simulator(simulator)

