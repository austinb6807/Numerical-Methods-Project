from inputs import *
from pipe_iterate import pipe_iterate
from solver import *
import numpy as np
import matplotlib.pyplot as plt




euler_steps, euler_temps = pipe_iterate(euler, step_size, pipe_length, hi, ho, Di, Do , kw , mdot, cp, T_f, T_am)
meuler_steps, meuler_temps = pipe_iterate(improved_euler, step_size, pipe_length, hi, ho, Di, Do , kw , mdot, cp, T_f, T_am)
rk4_steps, rk4_temps = pipe_iterate(runge_kutta, step_size, pipe_length, hi, ho, Di, Do , kw , mdot, cp, T_f, T_am)


print(euler_temps)


fig, axes = plt.subplots(3, 1, figsize=(8, 12), sharex=True, layout='constrained')
for ax in axes:
    ax.ticklabel_format(axis='y', useOffset=False, style='plain')

# Euler plots
axes[0].plot(euler_steps, euler_temps, 'b-', linewidth=1, label='Euler')
axes[0].set_ylabel('Temperature (K)', fontsize=10)
axes[0].set_title('Euler Method', fontsize=12)
axes[0].grid(True, alpha=0.3)
axes[0].legend(fontsize=9)

# Improved Euler plots
axes[1].plot(meuler_steps, meuler_temps, 'm-', linewidth=1, label='Improved Euler')
axes[1].set_ylabel('Temperature (K)', fontsize=10)
axes[1].set_title('Improved Euler Method', fontsize=12)
axes[1].grid(True, alpha=0.3)
axes[1].legend(fontsize=9)

# RK4 plots
axes[2].plot(rk4_steps, rk4_temps, 'g-', linewidth=1, label='RK4')
axes[2].set_ylabel('Temperature (K)', fontsize=10)
axes[2].set_xlabel('Distance Along Pipe (m)', fontsize=10)
axes[2].set_title('Runge-Kutta 4', fontsize=12)
axes[2].grid(True, alpha=0.3)
axes[2].legend(fontsize=9)

fig.suptitle(f'Water Temperature Along {pipe_length}m Long Pipe', fontsize=12)
plt.show()





