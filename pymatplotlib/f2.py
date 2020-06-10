from math import sin, cos
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.8
leng = 1.0

def pendulum_equations(w, t, l):
    th, v = w
    dth = v
    dv  = - g/l * sin(th)
    return dth, dv

t = np.arange(0, 20, 0.1)
track = odeint(pendulum_equations, (1.0, 0), t, args=(leng,))
xdata = [leng*sin(track[i, 0]) for i in range(len(track))]
ydata = [-leng*cos(track[i, 0]) for i in range(len(track))]

figure, ax = plt.subplots()
ax.grid()
line, = ax.plot([], [], 'H-', color='darkred', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    time_text.set_text('')
    return line, time_text

def update(i):
    newx = [0, xdata[i]]
    newy = [0, ydata[i]]
    line.set_data(newx, newy)
    time_text.set_text(time_template %(0.1*i))
    return line, time_text

ani = animation.FuncAnimation(figure, update, range(1, len(xdata)), init_func=init, interval=50)
#ani.save('f2.gif', writer='pillow', fps=100)
plt.show()
