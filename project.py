import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from scipy.constants import G
G /= 1.e9

Rearth = 6371
Rmoon = 1737

Mearth = 5.9722e24
Mmoon = 7.36e22
EMdistance = 3.84e4
fac = G * Mearth 
facmoon = G * Mmoon

def calc_a(r):
    r3 = np.hypot(*r)**3
    return -fac * r / r3
def calc_amoon(r):
    r3 = np.hypot(*r)**3
    return -facmoon * r / r3

def get_trajectory(h, launch_speed, launch_angle):
   

    v0 = launch_speed
    theta = np.radians(launch_angle)

    N = 100000
    tgrid, dt = np.linspace(0, 15000, N, retstep=True)
    tr = np.empty((N,2))
    v = np.empty((N,2))
    tr[0] = 0, Rearth + h
   
    v[0] = v0 * np.sin(theta), v0 * np.cos(theta)
    a = 0

    for i, t in enumerate(tgrid[1:]):
        r = tr[i] + v[i]*dt
        if np.hypot(*r) < Rearth:
           
            break
        tr[i+1] = r
        v[i+1] = v[i] + a*dt
        a = calc_a(tr[i+1])

    return tr[:i+1]


launch_speed, launch_angle = 2.92, 90
h = 200
tr = get_trajectory(h, launch_speed, launch_angle)

def plot_trajectory(ax, tr):
    earth_circle = Circle((0,0), Rearth, facecolor=(0.4, 0.4, 0.4))
    moon_circle = Circle((EMdistance/1.41, -EMdistance/1.41), Rmoon, facecolor=(0.9,0.9,0.9))
    ax.set_facecolor('k')
    ax.add_patch(earth_circle)
    ax.add_patch(moon_circle)
    ax.plot(*tr.T, c='y')
    ax.axis('equal')

   
    xmin, xmax = min(tr.T[0]), max(tr.T[0])
    ymin, ymax = min(tr.T[1]), max(tr.T[1])
    dx, dy = xmax - xmin, ymax - ymin
    PAD = 0.05
    ax.set_xlim(xmin - PAD*dx, xmax + PAD*dx)
    ax.set_ylim(ymin - PAD*dy, ymax + PAD*dy)


fig, axes = plt.subplots(nrows = 2, ncols = 2)
for i, launch_speed in enumerate([10.73, 7.91, 6, 10.3]):
    tr = get_trajectory(h, launch_speed, launch_angle)
    ax = axes[i//2, i%2]
    plot_trajectory(ax, tr)
    ax.set_title('{} km/s'.format(launch_speed))
plt.tight_layout()

plt.savefig('orbit.png')
plt.show()