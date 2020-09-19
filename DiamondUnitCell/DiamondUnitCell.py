import CrystalGraphs
import matplotlib.animation as animation

CrystalGraphs.size = 75
CrystalGraphs.ax.set_title('Diamond', c='white')

CrystalGraphs.fcc(1, [0, 0, 0, 'white'], [.25, .25, .25, 'cyan'], draw_path=True)

CrystalGraphs.set_axes_equal(CrystalGraphs.ax)

def animate(angle):
    CrystalGraphs.ax.view_init(azim=angle/2)
    
ani = animation.FuncAnimation(CrystalGraphs.fig, animate, frames=720, repeat=False, interval=10)

CrystalGraphs.show()
