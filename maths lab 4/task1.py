import matplotlib.pyplot as plt
import numpy as np
OA = np.array([-2, 0])
OB = np.array([1, 2])
OC = np.array([1, -1])
AB = OB - OA
BC = OC - OB
print(AB, BC)
OD = BC + AB
AD = OD + AB

plt.grid()
plt.ylim(-5, 5)
plt.xlim(-5, 5)
plt.arrow(-2, 0, AB[0], AB[1], width=0.03, length_includes_head=True,
facecolor='Yellow')
plt.arrow(1, 2, BC[0], BC[1], width=0.03, length_includes_head=True,
facecolor='Red')
plt.arrow(OD[0], OD[1], AD[0], AD[1], width=0.03, length_includes_head=True,
facecolor='Red')
plt.show()