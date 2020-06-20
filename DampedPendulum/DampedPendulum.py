import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation


def diffeq(y, t):
    b = .5 # This value tunes the air resistance
    L = .24 # Length of the pendulum
    g = 9.81 # Acceleration from gravity
    theta, thetap = y
    dydt = [thetap, -(g/L)*np.sin(theta)-b*thetap]
    return dydt

y0 = [2, 0]
times = np.linspace(0, 10, 1501)

sol = odeint(diffeq, y0, times) - np.pi/2

fig, ax = plt.subplots()

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, .5)
ax.set_aspect('equal')
ax.axis('off')

dot = ax.scatter(np.cos(sol[0,0]), np.sin(sol[0,0]), c='black')
line, = ax.plot([0,np.cos(sol[0,0])], [0,np.sin(sol[0,0])], c='black')

def ani(i):
    dot.set_offsets([np.cos(sol[i,0]), np.sin(sol[i,0])])
    line.set_data([0,np.cos(sol[i,0])], [0,np.sin(sol[i,0])])

animation = animation.FuncAnimation(fig, ani, interval = 20, frames=1500, repeat=True)

plt.show()

