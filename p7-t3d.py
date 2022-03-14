import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
 
edge = 25
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []
 
def animate(frame):
    t = frame
  
    xn = -((np.sin(t)**3)*16)

    yn = -(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))
 
    x.append(xn)
    y.append(yn)
    line.set_data(x, y)
 
ani = animation.FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 10, 0.1),
                        interval=30)
 
ani.save('my_anim.gif')
