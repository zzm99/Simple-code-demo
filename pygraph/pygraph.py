import matplotlib.pyplot as plt
import numpy as np

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15,30,45,10]
explode = (0,0.1,0,0)

plt.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',shadow=False,startangle = 90)

plt.axis('equal')
plt.show()

np.random.seed(0)
mu, sigma = 100, 20
a = np.random.normal(mu, sigma, size = 100)

plt.hist(a, 40, density = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75)
plt.title('Histogram')

plt.show()

N = 20
theta = np.linspace(0.0, 2*np.pi, N, endpoint = False)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width = width, bottom= 0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r/10.0))
    bar.set_alpha(0.5)
    
plt.show()


fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Simple Scatter')

plt.show()





























