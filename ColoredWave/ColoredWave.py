import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

t = np.linspace(-2, 12, 300)

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(-.25, 1.25)

line = ax.scatter(t, np.exp(-((t+2)**2)), s=5, c=np.exp(-((t+2)**2)), cmap=plt.get_cmap('plasma'))

def animate(i):
    line.set_offsets(np.column_stack((t, np.exp(-((t+2-i/25)**2)))))
    line.set_array(np.exp(-((t+2-i/25)**2)))


ani = animation.FuncAnimation(fig, animate, interval=20, frames=350, repeat=True)

plt.show()

