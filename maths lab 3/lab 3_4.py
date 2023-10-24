import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 15)

plt.subplot(2,3,1)
plt.plot(x, np.abs(np.abs(x)-2), ':ro')
plt.grid(color='grey', linestyle='-.')
plt.title('y = ||x| - 2|')

plt.subplot(2,3,2)
plt.plot(x, x-2, ':c.')
plt.grid(color='grey', linestyle='-.')
plt.title('y = x - 2')

plt.subplot(2,3,3)
plt.plot(x, x+2, '--r.')
plt.grid(color='grey', linestyle='-.')
plt.title('y = x + 2')

plt.subplot(2,3,4)
plt.plot(x, 2*x, ':co')
plt.grid(color='grey', linestyle='-.')
plt.title('y = 2x')

plt.subplot(2,3,5)
plt.plot(x, 0.5*x, ':r.')
plt.grid(color='grey', linestyle='-.')
plt.title('y = 0.5x')

plt.subplot(2,3,6)
plt.plot(x, -x, '--co')
plt.grid(color='grey', linestyle='-.')
plt.title('y = -x')

plt.show()