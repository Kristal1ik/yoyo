import numpy as np
import matplotlib.pyplot as plt
from math import pi

g = 9.8
L = 1.0
m = 0.5
M = 1.0
b = m / (m + M)

dt = 0.05
Tmax = 20
t = np.arange(0.0, Tmax, dt)

y = 0
th = pi / 3 
x = -
z = 0

state = np.array([th, y, x, z])
