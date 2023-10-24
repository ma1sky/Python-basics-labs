import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 25)
y1 = x
y2 = 1/x
y3 = 1/np.sqrt(x)

area1 = plt.subplot(2, 1, 1)
plt.plot(x, y1, ':ro')
plt.plot(x, y2, '-.c>')
plt.plot(x, y3, '--bo')
plt.grid(True)

area2 = plt.subplot(2, 1, 2)
plt.grid(True)
plt.loglog(x, y1, ':ro')
plt.loglog(x, y2, '-.c>')
plt.loglog(x, y3, '--bo')
plt.show()