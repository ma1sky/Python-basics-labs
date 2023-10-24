import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.0*np.pi, 2.0*np.pi, 100)

handle1, = plt.plot(x, np.cos(x), ':ro', label='y=cos(x)')
handle2, = plt.plot(x, 2*np.cos(x), '-.k.', label='y=2cos(x)')
handle3, = plt.plot(x, 0.3*np.cos(x), '--c,', label='y=0.3cos(x)')
handle4, = plt.plot(x, -np.cos(x), '-bx', label='y=-cos(x)')
plt.legend(handles=[handle1, handle2, handle3, handle4])

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.grid(linestyle='-.', color='grey')

plt.ylabel('y axis')
plt.xlabel('x axis')

plt.show()