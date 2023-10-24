import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 25)

func1 = plt.subplot(2, 1, 1)
func1.plot(x, np.sqrt(x+3), ':co')
plt.title('y = sqrt(x+3)')
plt.xlabel('x axis')
plt.ylabel('y axis')
func1.grid(True)

func2 = plt.subplot(2, 1, 2)
func2.plot(x, np.sign(x), '-.r>')
plt.title('y = sign(x)')
plt.xlabel('x axis')
plt.ylabel('y axis')
func2.grid(True)

plt.show()