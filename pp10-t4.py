import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-5, 5, 0.01)




def diff_func(v, t):
  y, x = v
  dydx= x
  dzdx = -4*x - 5*y
  return dydx, dzdx



y0 = 4
x0 = -1


v0 = y0, x0


sol = odeint (diff_func, v0, t)

plt.plot(t, sol[:, 0], 'g')
plt.plot(t, sol[:, 1], 'g')
plt.legend()
plt.show()

