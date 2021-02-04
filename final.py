import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt
import math
from math import cos, pi


def S10(x):
    return -4*cos(x)/pi - 4*cos(3*x)/(9*pi) - 4*cos(5*x)/(25*pi) - 4*cos(7*x)/(49*pi) - 4*cos(9*x)/(81*pi) - 4*cos(11*x)/(121*pi) - 4*cos(13*x)/(169*pi) - 4*cos(15*x)/(225*pi) - 4*cos(17*x)/(289*pi) + pi/2

def S2(x):
    return -4*cos(x)/pi + pi/2

dlistx = []
dlistwy = []
dlistf = []
dlistg = []

counter = -2000*pi

max_value = 0

min_value = 0

while counter<=2000*pi:
    dlistx.append(counter/2000.)
    value = S10(counter/2000.)
    value2 = S2(counter/2000.)
    dlistg.append(value2)
    dlistwy.append(value)
    dlistf.append(abs(counter/2000.))
    if value > max_value:
        max_value = value
    else:
      if value < min_value:
        min_value = value
    if counter % 100 == 0:
        print(counter)
    counter += 5

max_value = 1.1*max_value
min_value = min_value - 0.1*min_value
print(len(dlistx))
fix, ax = plt.subplots()
ax.plot(dlistx, dlistg, 'g.', label = 'S2(f,x)')
ax.plot(dlistx, dlistwy, 'r.', label = 'S10(f,x)')
ax.plot(dlistx, dlistf, 'b.', label = '|x|')
ax.set_ylim(min_value,max_value)

ax.legend(ncol=1, loc = 'upper left')
plt.xlabel = ('x')
plt.ylabel = ('f(x)')
plt.title("Problem 5")
plt.savefig('final_5_zoom.png')
plt.show()
