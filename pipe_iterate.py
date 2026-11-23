import numpy as np
from solver import *
from inputs import *

"""
This file includes the base code for solving for the waters temperatures profiles along the pipe gradient axially


"""

def pipe_iterate(solver, step_size, pipe_length, hi, ho, Di, Do , kw , mdot, cp, T_f, T_am):

    # Calculate total resistance of the heat circuit
    R_tot = 1 / (hi * np.pi * Di) + np.log(Do / Di) / (2 * np.pi * kw) + 1 / (ho * np.pi * Do)

    # Unchanged constants

    def temp_along_x(x, T_f):
        dT_dx = -(T_f - T_am) / (mdot * cp * R_tot)
        return dT_dx

    temps = solver(temp_along_x, 0, step_size, [T_f], pipe_length)

    return temps













