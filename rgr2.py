import matplotlib.pyplot as plt
import numpy as np
import math as m

h = np.linspace(1, 100000, 100)

y1=0.002
y2=0.028

N=6.022
k=1.381
g=9.8
t=200

m1=(y1)/(N)
m2=(y2)/(N)

n01=(m1*g)/(k*t)
n02=(m2*g)/(k*t)

n1=n01*m.e**(-1*((m1*g*h)/(k*t)))
n2=n02*m.e**(-1*((m2*g*h)/(k*t)))

handle1,=plt.plot(h,n1,color='gray',label='Молекула водорода.')
handle2,=plt.plot(h,n2,'k',label='Молекула азота.')
plt.legend(handles=[handle1,handle2])
plt.title('Графики распределение Больцмана для молекул водорота и азота.')
plt.xlabel('h')
plt.ylabel('n')

plt.grid(True)
plt.show()
