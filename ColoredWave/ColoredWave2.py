import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import mplanimations

t = np.linspace(-2*np.pi, 2*np.pi, 300)

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 3)

line = ax.scatter(t, np.exp(-(t**2)), s=5, c=mplanimations.normalize(np.exp(-(t**2))), cmap=plt.get_cmap('plasma'))

ts = [mplanimations.Transitions() for i in range(2)]

def animate(i):
    ts[0].scatter_transition(i, 1, t, t, np.exp(-(t**2)), .25*np.exp(-(t**2)), line, mplanimations.normalize(np.exp(-(t**2))), .25*mplanimations.normalize(np.exp(-(t**2))))
    ts[1].scatter_transition(i, 3, t, t, .25*np.exp(-(t**2)), np.exp(-(t**2)), line, .25*mplanimations.normalize(np.exp(-(t**2))), mplanimations.normalize(np.exp(-(t**2))))


ani = animation.FuncAnimation(fig, animate, interval=20, frames=200, repeat=False)

plt.show()


