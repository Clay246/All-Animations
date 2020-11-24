import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint
import mplanimations

dc = .1 # Drag coefficient
offset = 2 # Delays the arrival of the plane at x=0 by this many seconds

# Differential equation for x coordinate
def diffeqx(x, t):
    xcoord, xcoordp = x
    dxdt = [xcoordp, -dc*xcoordp]
    return dxdt

# Differential equation for y coordinate
def diffeqy(y, t):
    g = 9.81
    ycoord, ycoordp = y
    dydt = [ycoordp, -g+dc*np.absolute(ycoordp)]
    return dydt

t = np.linspace(0, 12, 601)
tp = np.linspace(-offset, 20, (20+offset)/.02)

# Initial conditions for the differential equations
y0 = [400, 0]
x0 = [0, 100]

# Solutions
solutionx = odeint(diffeqx, x0, t)
solutiony = odeint(diffeqy, y0, t)

# Finding the frame at which the projectile reaches the ground
for i in range(len(solutiony)):
    if solutiony[i,0] <= 0:
        t0 = i
        break

# Converting the frame to a time for the animation
starttime = mplanimations.time(t0)+offset

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_xlim(-100, 1200)
ax.set_ylim(-20, 450)

ax.fill_between([-100, 1200], [0, 0], [450, 450], color='lightskyblue')
ax.fill_between([-100, 1200], [-20, -20], [0, 0], color='forestgreen')

btrail = ax.scatter(0, 400, c='grey', s=2)
bomb = ax.scatter(0, 400, c='black', s=10)
ptrail = ax.scatter(0, 400, s=2)
plane = ax.scatter(0, 400, marker='$✈$', s=200)

ts = [mplanimations.Transitions() for i in range(3)]
es = [mplanimations.Effects() for i in range(2)]

n = 0
def animate(i):
    global n
    
    if mplanimations.time(i) <= offset:
        bomb.set_offsets([[100*tp[i], 400]])
    
    if offset < mplanimations.time(i) <= starttime:
        n += 1
        bomb.set_offsets([solutionx[n,0], solutiony[n,0]])
        es[0].tail([solutionx[n,0]], [solutiony[n,0]], btrail, 'grey', 20)

    else:
        btrail.set_offsets([-1000,0]) # Simply hiding the point
        ts[0].dot_transition(i, starttime, 10, 1000, bomb, transition_type=mplanimations.linear)
        ts[1].color_transition(i, starttime, plt.cm.autumn, 0, 1, bomb, transition_type=mplanimations.linear)
        ts[2].alpha_transition(i, starttime, 1, 0, bomb)

    plane.set_offsets([100*tp[i], 400])    
    es[1].tail([100*tp[i]], [400], ptrail, 'lightgrey', 100)

ani = animation.FuncAnimation(fig, animate, interval=20, frames=800, repeat=False)

plt.show()
