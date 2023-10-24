import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-100, 100, 10000)
y = (-1)**x
plt.semilogx(x,y, ':ro')
plt.show()