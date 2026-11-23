#Code for the functions for the Euler, Improved_Euler, and Runge-Kutta 4 methods

# file where our methods are defined
import numpy as np

'''
Parsing Instructions:
Code is designed for ODEs to be inputted as an array of first order ODEs; This is so we can iterate multi-order ODEs
through a system of reduced order equations.
Inputs:
f --> The ODE to be solved. format wise, this function should return an array of length n for ODE of order n.
      The returned array will have n derivatives in ascending order, i.e. y', y'', ..., y^(n+1).

t0 --> The initial time point. Parsed as a float.

h --> The time step. Parsed as a float.

y0 --> The array of initial values needed to iterate on our ODE. This should be parsed as an array of length of n for 
       ODE of order n.

num_steps --> number of steps; I think that we could change this to be the range of time, but this works to test.


'''

def euler(f, t0, h, y0, time):

    #initializing arrays for time and 0th to nth derivative
    num_steps = int(time/h)
    tlist = np.array([t0 + i * h for i in range(num_steps)])
    y = np.zeros([num_steps, len(y0)])


    #recompute h becuase it got changed due to rounding
    h = tlist[1]-tlist[0]


    # initialize y array
    y[0, :] = y0

    # iterate through each column; f depending on order of the DE
    for i in range(1, num_steps):
        dydt = np.array(f(tlist[i - 1], y[i - 1]))
        y[i, :] = y[i - 1, :] + dydt * h

    return tlist, y



def improved_euler(f, t0, h, y0, time):


    num_steps = int(time/h)
    tlist = np.array([t0 + i *h for i in range(num_steps)])
    y = np.zeros([num_steps, len(y0)])

    y[0, :] = y0

    for i in range(1, num_steps):
        dydt1 = np.array(f(tlist[i-1], y[i-1]))
        y[i, :] = y[i-1] + dydt1*h
        dydt2 = np.array(f(tlist[i], y[i]))
        dydt = (dydt1 + dydt2)/2
        y[i, :] = y[i-1] + dydt*h
    return tlist, y



def runge_kutta(f, t0, h , y0, time):

    num_steps = int(time/h)
    tlist = np.array([t0 + i *h for i in range(num_steps)])


    y = np.zeros([num_steps, len(y0)])

    y[0, :] = y0

    for ii in range(1, num_steps):
        t_prev = tlist[ii-1]
        y_prev = y[ii-1, :]

        k1= np.array(f(t_prev, y_prev))
        k2 = np.array(f(t_prev +h/2, y_prev + (h/2)*k1))
        k3 = np.array(f(t_prev +h/2, y_prev + (h/2)*k2))
        k4 = np.array(f(t_prev +h, y_prev + h*k3))

        y[ii, :] = y_prev + (h/6)*(k1 +2*k2 + 2*k3 +k4)

    return tlist, y




