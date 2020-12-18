import math

STEP = 0.00001
INTEGRATION_TIME = 0.2
C3 = 200 * 10 ** (-6)
C2 = 150 * 10 ** (-6)
C1 = 300 * 10 ** (-6)
R3 = 7
R2 = 4
R1 = 5
FREQUENCY = 50
Umax = 100


def U1(time):
    return Umax * math.sin(2 * math.pi * FREQUENCY * time)
