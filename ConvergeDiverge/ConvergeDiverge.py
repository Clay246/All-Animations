import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimations

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

xs = np.linspace(-5, 5, 11)
ys = np.linspace(-5, 5, 11)

x, y = np.meshgrid(xs, ys)

field = ax.scatter(x, y, s=1, c='orange')

xx = []
yy = []

# Perhaps a better way to do this part without using these functions
for item in x:
    for item2 in item:
        xx.append(item2)

for item in y:
    for item2 in item:
        yy.append(item2)

xx = np.array(xx)
yy = np.array(yy)

es = [mplanimations.Effects()]

def animate(i):
    global xx, yy
    
    if mplanimations.time(i) <= 4.5:
        xx += -xx*.02/2 # This is where the x component of the vector field is specified
        yy += -yy*.02/2 # This is where the y component of the vector field is specified

    elif 4.5 < mplanimations.time(i) <= 9.04:
        xx += xx*.02/2
        yy += yy*.02/2

    es[0].tail(xx, yy, field, 'orange', n=60*len(xx))

ani = animation.FuncAnimation(fig, animate, interval=20, frames=500, repeat=False)

plt.show()
