import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 100)
y = np.cos(x)

plt.plot(x, y, ':g')
plt.plot(y, x, '-.r')
plt.plot(x, x, 'b')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.axis('equal')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(True)
plt.title('y=cos(x)')

plt.show()