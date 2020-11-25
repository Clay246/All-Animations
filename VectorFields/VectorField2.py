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

# Points for the scatter plot grid
xs = np.linspace(-6, 6, 20)
ys = np.linspace(-6, 6, 20)

# Points for the quiver grid
xqs = np.linspace(-5, 5, 17)
yqs = np.linspace(-5, 5, 17)

# The grids
xx, yy = np.meshgrid(xs, ys)
xq, yq = np.meshgrid(xqs, yqs)

# The vector field functions
def Fieldx(x, y):
    return np.cos(x-y)

def Fieldy(x, y):
    return np.sin(x+y)

def Normalize(x, y):
    return np.sqrt(Fieldx(x, y)**2+Fieldy(x, y)**2)

# The magnitude of the vectors
magnitude = np.hypot(xq, yq)

# The static plots
arrow = ax.quiver(xq, yq, Fieldx(xq,yq)/Normalize(xq,yq), Fieldy(xq,yq)/Normalize(xq,yq), magnitude, cmap='viridis_r')
field = ax.scatter(xx, yy, s=2, c='dodgerblue')


# There is probably a better way to do this part, but meshgrid makes the lists a bit weird
x = []
y = []

for item in xx:
    for item2 in item:
        x.append(item2)

for item in yy:
    for item2 in item:
        y.append(item2)

x = np.array(x)
y = np.array(y)



es = [mplanimations.Effects()]

def animate(i):
    global x, y
    for i in range(10):
        x += Fieldx(x, y)*.02/(50) # A numerical integration approach
        y += Fieldy(x, y)*.02/(50) # This is left as .02/5 because .02 is the interval
    es[0].tail(x, y, field, 'dodgerblue', n=60*len(x))

ani = animation.FuncAnimation(fig, animate, interval=20, frames=700, repeat=False)

plt.show()
