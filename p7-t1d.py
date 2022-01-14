import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
 
edge = 10
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []

def star():
 
  t = np.arrange(-10, 10, 0.01)
  x = 12*np.cos(t) + 8*np.cos(1.5*t)
  y = 12*np.cos(t) - 8*np.cos(1.5*t)
  star =plt.plot(x, y, 'o', color = 'blue', label = 'line')

star()
plt.show