import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365

seconds_in_year = 365 * 24 * 60 * 60

years = 2

t = np.linspace(0, years*seconds_in_year, frames)


def move_func(s, t):
  
    (x, v_x, y, v_y, m) = s

    dxdt = v_x
  
    dv_xdt = - G * ms * x / (x**2 + y**2)**1.5
  
    dydt = v_y

    dv_ydt = - G * ms * y / (x**2 + y**2)**1.5
  
    #dmdt= -(((3*m*p/4*np.pi)**2/3)*Qs)/(4 * d**2*Qw)

    dist = (x**2 + y**2)**0.5
    dmdt = - (1 - albedo)*(Qs * (np.pi*(3*m/4*np.pi*p)**(2/3))/(4*np.pi*(dist)**2))/Qw
    
  
  
    return (dxdt, dv_xdt, dydt, dv_ydt, dmdt ) 
  
G = 6.67 * 10**(-11)

ms = 1.98 * 10**(30)

cm = 2.2 *10**14
#масса каметы  
p=900

a = np.pi / 3 +np.pi

v= 40000

tn = - 150

x10 = 0.5* (10 **11)

v_x10 = v * np.sin(a) 

y10 =  200 * (10 **9)

v_y10 = v* np.cos(a)

c = 2100

albedo = 0.97

Qw = (((200-tn) * c* 1)+(2300 * 1000))/1

Qs = 3.828*10**26

d = 150 *10**9

s0 = (x10, v_x10, y10, v_y10,cm)

sol = odeint(move_func, s0, t)

for i in range(frames):
  print(f"t: {t[i]} | m: {sol[i,4]}")

def solve_func(i, key):
    
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        
        
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        
    return ((x, y), )

fig, ax = plt.subplots()


ball1, = ax.plot([], [], 'o', color='b')
ball_line1, = ax.plot([], [], '-', color='b')


ax.plot([0], [0], 'o', color='y', ms=20)


def animate(i):
  ball1.set_data(solve_func(i, 'point')[0])
  ball_line1.set_data(solve_func(i, 'line')[0])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

ax.axis('equal')
edge = 1.5 *  y10

ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('123.gif')