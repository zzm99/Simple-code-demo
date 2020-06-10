import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#author： zzm
#time： 2019.4.25
#制作李萨如图形动态gif
#李萨如图形的轨迹方程：
# x = A1cos(wt+β1)
# y = A2cos(wt+β2)

figure, t = plt.subplots()
xx, yy = [], []
dot, = t.plot([], [], 'r-', animated=False)


def x(s):
    return np.cos(5*s)

def y(s):
    return np.cos(3*s+3/4*np.pi)

def init():
    t.set_xlim(-1, 1)
    t.set_ylim(-1, 1)
    return dot,

def update(frame):
    xx.append(x(frame))
    yy.append(y(frame))
    dot.set_data(xx, yy)
    return dot,

photo = FuncAnimation(figure, update, frames=np.linspace(0,np.pi*2, 128),
                    init_func=init, blit=True)

photo.save('zzm.gif', writer='pillow', fps=30)
plt.show()

