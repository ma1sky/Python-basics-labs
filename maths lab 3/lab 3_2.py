import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.0 * np.pi ,2.0 * np.pi, 100)

handle1, = plt.plot(x, np.sin(x),'--dr', label='y=sin(x)')
handle2, = plt.plot(x, np.sin(x-3),'-.b*', label='y=sin(x-2)')
handle3, = plt.plot(x, np.sin(x+1),':yo', label='y=sin(x+1)')

plt.legend(handles=[handle1, handle2, handle3])

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.grid(linestyle='-.', color='pink')
plt.ylabel('y axis')
plt.xlabel('x axis')

plt.show()