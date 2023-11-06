import matplotlib.pyplot as plt
import numpy as np

g = 9.8
Na = 6.022*10**(23)
T = 200
k = 1.381*10**(-23)
u = (0.002, 0.028)

h = np.linspace(0,10,100)
n1 = (u[0]*g / k * T) * np.exp()

plt.plot(h, n1,'-', color='#4C92D3')
plt.plot(h, n2,'-', color='#99AAEE')
plt.grid(True)
plt.xlabel('h axis')
plt.ylabel('n axis')
plt.show()