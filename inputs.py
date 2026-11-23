import numpy as np

"""
This file includes all the inputs

    hi: Convective heat transfer coefficient of water
    ho: Convection heat transfer coefficient of ambient air
    Di: Pipe internal diameter
    Do: Pipe external diameter
    kw: Wall conductivity
    mdot: Mass flow rate
    cp: Specific heat of water
    T_f: Inlet temperature
    T_am: Ambient temperature
    pipe_length: Pipe distance
    R_tot: Total resistance per unit length
    x: iteration position, starts a 0
    step_size: Step size (also denoted as h)


"""

# Inputs that can be modified for each sim configuration
hi = 1000           # W/m^2-K; currently estimated
ho = 15             # W/m^2-K; currently estimated
Di = 1.097 * .0254  # m
Do = 1.315 * .0254  # m
kw = 17             # W/m-K
mdot = 4            # kg/s
cp = 4184           # J/kg-K
T_f = 350           # K
T_am =  298.15      # K
pipe_length = 100     # m
step_size = 0.01    # m








