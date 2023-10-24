import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi/2, np.pi/2, 25)
y = np.sin(x)

plt.plot(x,y,'-', color='#4C92D3')
plt.plot(y,x,':', color='#C10030')
plt.plot(x,x,'-', color='#5E158D')
plt.grid(True)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()