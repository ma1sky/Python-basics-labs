import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 15)
y = 2*x**2 + 4*x - 3

parab = plt.figure()
axp = parab.add_subplot(1,1,1)
plt.title('$y = 2x^2+4x-3$')
axp.plot(x,y, '--co')
parab.show()
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.grid(linestyle='--', color='pink')

x = np.linspace(-100, 100, 15)
y = 3/x

hyperb = plt.figure()
axh = hyperb.add_subplot(1,1,1)
axh.plot(x,y, ':r*')
plt.title('y = 1/x')
hyperb.show()

plt.ylabel('y axis')
plt.xlabel('x axis')
plt.grid(linestyle='-.', color='yellow')
plt.show()