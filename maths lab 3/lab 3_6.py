import matplotlib.pyplot as plt
import numpy as np


degree = np.arange(-3, 4, 1)
dozens = np.ones((7)) * 10
dozInDeg = np.power(dozens, degree)

plt.subplot(2, 1, 1)
plt.plot(degree, dozInDeg,'--r>')

plt.grid(color='grey', linestyle='-.')
plt.ylabel('dozens in degree')
plt.xlabel('degree')


plt.subplot(2, 1, 2)
plt.semilogy(degree, dozInDeg,'-.c<')

plt.grid(color='grey', linestyle='-.')
plt.ylabel('dozens in degree')
plt.xlabel('degree')


plt.show()