import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 24, 0.1)

def radio_function (s, t):
   cos_alpha = np.cos(np.pi/12 * t - np.pi)
   if cos_alpha<0:
     cos_alpha = 0
   dsdt = np.sqrt(s/np.pi)*cos_alpha*s*E*k
   
   return dsdt
 
E = 1367 
k = 0.0000034

s_0 = 1600

b = odeint(radio_function, s_0, t)

plt.plot(t, b[:, 0], label='Площадь')
plt.xlabel ('Время, часы')
plt.ylabel ('Площадь, м^2')
plt.legend()

plt.show()








