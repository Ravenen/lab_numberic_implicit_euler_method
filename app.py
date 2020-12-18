import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from constants import STEP, INTEGRATION_TIME
from equations import system


def implicit_euler_method(equation_system, initial_values, time_step, integration_time):
    intervals_quantity = int(integration_time / time_step)
    intervals = np.linspace(0, intervals_quantity * time_step, intervals_quantity + 1)
    values = np.zeros((intervals_quantity + 1, len(initial_values)))
    values[0] = np.array(initial_values)
    equation_system_ = lambda value, time: np.asarray(equation_system(value, time))

    def function(next_value, prev_value, time):
        return next_value - time_step * equation_system_(next_value, time) - prev_value

    for n in range(intervals_quantity):
        values[n+1] = optimize.fsolve(function, values[n], args=(values[n], intervals[n]))

    return values, intervals


if __name__ == '__main__':
    values_line, time_line = implicit_euler_method(system, [0., 0., 0.], STEP, INTEGRATION_TIME)
    output = values_line[:, 2]
    plt.plot(time_line, output)
    plt.show()
