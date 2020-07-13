import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class bouncers:

    def __init__(self, height):
        global n, heights
        self.x = n
        self.height = height
        self.vi = 0
        self.vf = np.sqrt(2*self.height*gravity)
        self.ball = plt.scatter(self.x, self.height, s=25, c='black')
        self.t = 0
        n += 50
        ax.scatter(self.x, self.height, c='black', alpha=.25)
        
        
    def bouncy(self):
        y = self.height + self.vi*self.t - .5*gravity*(self.t**2)
        if y >= 0:
            self.ball.set_offsets([self.x, y])
            self.t += interval/100 # 10X actual speed
        else:
            self.vi = self.vf
            self.height = 0
            self.t = 0


n = 0

fig, ax = plt.subplots()

plt.axis('off')

ax.set_aspect('equal')

floor, = plt.plot([-10, 460], [0, 0], c='black', linewidth=2)

ax.text(0, -25, '1', ha='center')
ax.text(50, -25, '2', ha='center')
ax.text(100, -25, '3', ha='center')
ax.text(150, -25, '12', ha='center')
ax.text(200, -25, '10', ha='center')
ax.text(250, -25, '60', ha='center')
ax.text(300, -25, '105', ha='center')
ax.text(350, -25, '280', ha='center')
ax.text(400, -25, '252', ha='center')

interval = 20
gravity = 9.81

b = [bouncers(19.62), bouncers(44.145), bouncers(78.48), bouncers(122.625), bouncers(176.58), bouncers(240.345), bouncers(313.92), bouncers(397.305), bouncers(490.5)]

def update(i):
    for item in b:
        item.bouncy()


ani = animation.FuncAnimation(fig, update, interval=interval, frames=1000, repeat=False)

plt.show()
