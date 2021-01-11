import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimationsvName as ans

G = .000001 # The gravitational constant is set at this value for convenience
dt = 1/250

class Objects:

    def __init__(self, mass, x, y, vx, vy):

        self.mass = mass
        self.pos = np.array([x, y], dtype=float)
        self.v = np.array([vx, vy], dtype=float)

        
    def update(self, objs):

        self.force = np.array([0, 0], dtype=float)
        
        for obj in objs:
            self.seperation = np.hypot(self.pos[0]-obj.pos[0], self.pos[1]-obj.pos[1])
            
            if self.seperation > .1: # Turning off gravity if the objects get too close together
                self.force += np.array([(G*self.mass*obj.mass/(self.seperation**2))*
                                        ((np.absolute(obj.pos[0] - self.pos[0]))/self.seperation)*
                                        float(np.where(obj.pos[0]-self.pos[0] != 0, (obj.pos[0]-self.pos[0])/(np.absolute(obj.pos[0]-self.pos[0])), 0)),
                                        (G*self.mass*obj.mass/(self.seperation**2))*
                                        ((np.absolute(obj.pos[1] - self.pos[1]))/self.seperation)*
                                        float(np.where(obj.pos[1]-self.pos[1] != 0, (obj.pos[1]-self.pos[1])/(np.absolute(obj.pos[1]-self.pos[1])), 0))])
                self.acceleration = self.force/self.mass
                self.v += (self.acceleration*dt)
                self.pos += self.v*dt
                
        else:
            self.pos += self.v*dt

            
    def center_of_mass(positions, masses):
        cm = 0
        for i in range(len(masses)):
            cm += positions[i]*masses[i]
        cm = cm/np.sum(masses)
        return cm


plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_xlim(-.5, 8)
ax.set_ylim(-.5, 2)
ax.axis('off')

m = 10
c = 'white'
a = .5

objects = [Objects(m,0,0,0,0), Objects(m,0,1,0,0), Objects(m,0,2,0,0), Objects(m,.5,0,0,0),
           Objects(m,1,0,0,0), Objects(m,.5,2,0,0), Objects(m,1,2,0,0), Objects(m,2,2,0,0),
           Objects(m,2,1,0,0), Objects(m,2,0,0,0), Objects(m,2.5,0,0,0), Objects(m,3,0,0,0),
           Objects(m,4,0,0,0), Objects(m,4.5,2,0,0), Objects(m,5,0,0,0), Objects(m,4.5,1,0,0),
           Objects(m,4.25,1,0,0), Objects(m,4.75,1,0,0), Objects(m,6,2,0,0), Objects(m,7,2,0,0),
           Objects(m,6.5,1,0,0), Objects(m,6.5,0,0,0)]

scatters = [ax.scatter(objects[i].pos[0], objects[i].pos[1], s=5, c=c) for i in range(len(objects))]

lines = [ax.plot([0,0],[0,2], c=c, alpha=a), ax.plot([0,1],[0,0], c=c, alpha=a),
         ax.plot([0,1],[2,2], c=c, alpha=a), ax.plot([2,2],[0,2], c=c, alpha=a),
         ax.plot([2,3],[0,0], c=c, alpha=a), ax.plot([4,4.5],[0,2], c=c, alpha=a),
         ax.plot([5,4.5],[0,2], c=c, alpha=a), ax.plot([4.25,4.75],[1,1], c=c, alpha=a),
         ax.plot([6,6.5],[2,1], c=c, alpha=a), ax.plot([7,6.5],[2,1], c=c, alpha=a),
         ax.plot([6.5,6.5],[1,0], c=c, alpha=a)]

ts_lines = [ans.Transitions() for i in range(len(lines))]
ts_scatters = [ans.Transitions() for i in range(3*len(scatters))]
es = [ans.Effects() for i in range(len(objects))]

def animate(i):
    
    for j in range(len(lines)):
        ts_lines[j].alpha_transition(i, 4, .5, 0, lines[j][0])
    for j in range(len(scatters)):
        ts_scatters[j].color_transition(i, 4.5, plt.get_cmap('nipy_spectral'), 1, .1+.9*j/len(objects), scatters[j])
    for j in range(len(scatters)):
        ts_scatters[j+len(scatters)].dot_transition(i, 4+j/100, 5, 50, scatters[j], transition_time=.3)
    for j in range(len(scatters)):
        ts_scatters[j+2*len(scatters)].dot_transition(i, 4.4+j/100, 50, 5, scatters[j], transition_time=.3)

    if ans.time(i) == 6: # The purpose of this is to prevent the dots from disppearing for a few frames when the simulation starts/ends.
        for k in range(30):
            for j in range(len(scatters)):
                scatters[j].set_offsets([objects[j].pos[0], objects[j].pos[1]])
                es[j].tail([objects[j].pos[0]], [objects[j].pos[1]], scatters[j], plt.get_cmap('nipy_spectral')(.1+ .9*j/len(objects)), 30)
    
    if ans.time(i) > 6:
        for j in range(25):
            for obj in objects:
                obj.update(objects)
            
        for j in range(len(scatters)):
            es[j].tail([objects[j].pos[0]], [objects[j].pos[1]], scatters[j], plt.get_cmap('nipy_spectral')(.1+ .9*j/len(objects)), 30)
        
    cm = Objects.center_of_mass([obj.pos for obj in objects], [obj.mass for obj in objects])
    ax.set_xlim(cm[0]-4, cm[0]+4)
    ax.set_ylim(cm[1]-1.5, cm[1]+1.5)

animation = animation.FuncAnimation(fig, animate, interval=20, frames=700, repeat=False)

plt.show()
