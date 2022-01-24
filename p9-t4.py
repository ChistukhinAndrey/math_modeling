import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(1, 200, 1)
 

def radio_function(v, t):
    dmdt = (b-k*v)/m
    return dmdt
v_0=0
v=4
b=8000
m=15*(10**3)
k=100

 

solve_Bi = odeint(radio_function, v_0, t)
F=b-k*solve_Bi[:,0]
# Построение решения в виде графика функции
plt.plot(solve_Bi[:,0], F,color='r', label='Скорость')
plt.xlabel('Время тяги')
plt.ylabel('Скорость')
plt.title('Зависимость тяги локомотива от cкорости   ')
plt.legend()

plt.show()