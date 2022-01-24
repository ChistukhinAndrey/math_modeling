import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(1, 20, 1)

def radio_function (m, t):
   dmdt = k*m
   return dmdt
m_0 = 1
k = 1.17


b = odeint(radio_function, m_0, t)

plt.plot(t, b[:, 0], label='кол-во бактерий')
plt.xlabel ('Период распада, секунды')
plt.ylabel ('Функцияраспада')
plt.legend()

plt.show()