L = 0.1
R = L/5
evalTime = 750
popSize = 10
numGens = 200
numEnvs = 4

# ----------- Neural network parameters ------------

SENSOR_NEURON = 0

AUDITORY_NEURON = 1

HIDDEN_NEURON = 2

MOTOR_NEURON = 3

NUM_HIDDEN_NEURONS = 5

TAU_MAX = 0.5

TAU_MIN = 0.1

# ------------------ Robot parameters --------------

maximizeLight = 0
maximizePos = 1
evaluationTime = 1500

JOINT_ANGLE_MAX = -3.14159 / 2.0 # 4.0 # 8.0

MAX_HEAD_ROTATION = 3.14159 / 2.0

maxDepth = 4

maxChildren = 2

length = 1.5 * (0.5 / 4.0)

radius = 1.5 * (0.05 / 4.0)

eyeRadius = radius * 2

pupilRadius = eyeRadius * 0.5

deathAge = 5 #In Days

minimumAmountOf3Dness = 0.0

maximumAmountOf3Dness = 2.0

newRobotInitial3Dness = 0.0

newRobotFinal3Dness   = 0.5




#visual
swarmPositionOffsets = {
    0: [0, 0, 0],
    1: [-10, 10, 0],
    2: [-20, 20, 0],
    3: [-30, 30, 0],
    4: [-40, 40, 0],
    5: [-50, 50, 0],
    6: [-60, 60, 0],
    7: [-70, 70, 0],
    8: [-80, 80, 0],
    9: [-90, 90, 0]
}
# Minimal occlusion
swarmDrawOffsets = {
    0: [0 + 0, 0 + 0, 0],
    1: [10 - 1, -10 + 1, 0],
    2: [20 - 2, -20 + 2, 0],
    3: [30 - 3, -30 + 3, 0],
    4: [40 - 3, -40 + 1, 0],
    5: [50 + 0, -50 + 2, 0],
    6: [60 - 1, -60 + 3, 0],
    7: [70 + 0, -70 + 4, 0],
    8: [80 - 2, -80 + 4, 0],
    9: [90 + 0.5, -90 + 1, 0]
}

ACCURACY = 1

SPEED = 2
