# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:12:45 2016

@author: Charles
"""

import math
import matplotlib
import numpy

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    for step in range(num_steps + 1):
        angle = 2 * math.pi * step / (num_steps)
        x[step, 0] = moon_distance * math.cos(angle)
        x[step, 1] = moon_distance * math.sin(angle)
    
    return(x)

x = orbit()


def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()