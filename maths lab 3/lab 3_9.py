import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 25)
func1 = plt.subplot(1,3,1)
func1.plot(x, np.exp(x), ':r.')
plt.xlabel('x axis')
plt.ylabel('y axis')
func1.grid(True)

x = np.linspace(np.exp(-2), np.exp(2), 25)
func2 = plt.subplot(1,3,2)
func2.plot(x, np.log(x), '-.bo')
plt.xlabel('x axis')
plt.ylabel('y axis')
func2.grid(True)

x = np.linspace(-2, np.exp(2), 25)
func3 = plt.subplot(1,3,3)
func3.plot(x, x, ':c>')
plt.xlabel('x axis')
plt.ylabel('y axis')
func3.grid(True)

plt.show()