from constants import *


def system(values, time):
    return [
        (values[1] + values[2] - U1(time)) / R2 / C1,
        ((R2 - R1) * (values[1] + values[2]) - R2 * U1(time) - R1 * values[0]) / (R1 * R2) / C2,
        ((((R2 - R1) * (values[1] + values[2]) - R2 * U1(time) - R1 * values[0]) / (R1 * R2)) - values[2] / R3) / C3
    ]
