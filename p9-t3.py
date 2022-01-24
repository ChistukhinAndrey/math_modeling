import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(1, 200, 1)
 

def radio_function(v, t):
    dmdt =  (v**2*y+F)/m
    return dmdt
v_0=0
v=4
a=1
m=10
y=-1.5
F=m*a
 

solve_Bi = odeint(radio_function, v_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0],color='r', label='Скорость')
plt.xlabel('Время разгона')
plt.ylabel('Скорость')
plt.title('Разгон')
plt.legend()

plt.show()