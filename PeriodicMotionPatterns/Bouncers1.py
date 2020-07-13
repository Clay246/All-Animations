import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class bouncers:

    def __init__(self):
        global n
        self.x = n
        self.height = self.x
        self.vi = 0
        self.vf = np.sqrt(2*self.height*gravity)
        self.ball = plt.scatter(self.x, self.height, s=25, c='black')
        self.t = 0
        n += .05
        
        
    def bouncy(self):
        y = self.height + self.vi*self.t - .5*gravity*(self.t**2)
        if y >= 0:
            self.ball.set_offsets([self.x, y])
            self.t += interval/2000 # Half speed
        else:
            self.vi = self.vf
            self.height = 0
            self.t = 0


n = .1

fig, ax = plt.subplots()

plt.axis('off')
ax.set_aspect('equal')

floor, = plt.plot([0, 2], [0, 0], c='black', linewidth=2)

interval = 20
gravity = 9.81

bouncies = []

for i in range(29):
    bouncies.append(bouncers())


def update(i):
    for item in bouncies:
        item.bouncy()


ani = animation.FuncAnimation(fig, update, interval=interval, frames=1000, repeat=False)

plt.show()
