import matplotlib.pyplot as plt
import numpy as np

#author：zzm
#time: 2019.4.25
s = np.arange(0, np.pi*2, 0.01)

def x(s,a,p):
    return a*np.sin(p*s)

def y(s,b,q,t):
    return b*np.sin(q*s+t)

def lisa(a,b,n,t,posit):
    p = 1
    q = n*p
    plt.subplot(3,3,posit)
    plt.grid()
    plt.plot(x(s,a,p),y(s,b,q,t))

lisa(1,1,1,0,1)
lisa(1,1,1,np.pi/2,2)
lisa(1,1,1,1,3)
lisa(1,1,2,0,7)
lisa(1,1,1,np.pi/2,8)
lisa(1,1,1,1,9)

plt.savefig('test', dpi = 600)
plt.show()


