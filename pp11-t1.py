import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину и количество кадров
frames = 200
t = np.linspace(0, 5, frames)
 
# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = - g - mu * v_y
    return dxdt, dv_xdt, dydt, dv_ydt

# Определяем начальные значения и параметры
g = 9.8
v = 20
alpha = 90 * np.pi / 180
mu = 1

x0 = 0
v_x0 = v * np.cos(alpha)
y0 = 0
v_y0 = v * np.sin(alpha)

z0 = x0, v_x0, y0, v_y0

# Решаем систему диф. уравнений
def solve_func(i, key):
    sol = odeint(move_func, z0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  
  # Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 15
ax.set_xlim(-15, edge)
ax.set_ylim(0, edge)

plt.show()


