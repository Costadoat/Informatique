# when we're in pylab mode, the next two imports are not necessary
# we do it here for correctness sake, iow your code will also run without pylab mode

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation

# Données
G = 6.67*10**(-11)
m_terre=5.9736*10**24
r_terre=6378.1370*1000
periode=1000.
ro=(m_terre*G*periode**2/(4*np.pi**2))**(1/3.)
a=m_terre*G/ro**2
v_init=2*np.pi*ro/periode
print('Vitesse initiale',v_init,'Rayon orbite',ro)

# gravitational acceleration on Earth in m*s^-2
def attraction_terrestre(x,y):
    centre=[0,0]
    d_carre=(x-centre[0])**2+(y-centre[1])**2
    f=G*m_terre/d_carre**(3/2.)
    print(G*m_terre/d_carre)
    ax,ay=-f*(x-centre[0]),-f*(y-centre[1])
    print(ax,ay)
    return np.array((ax,ay))

# bounds of the room
xlim = (-50000*1000,50000*1000)
ylim = (-50000*1000,50000*1000)

# 1 millisecond delta t
delta_t = 1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()

# in Python 2.7 we have to derive from object to have new-style classes
# in Python 3 this is still valid, but not necessary, as all classes are new-style
class Ball(object):

    def __init__(self, xy, v):
        """
        :param xy: Initial position.
        :param v: Initial velocity.
        """
        self.xy = np.array(xy)
        self.v = np.array(v)

        self.scatter, = ax.plot([], [], 'o', markersize=20)

    def update(self):
        # delta t is 0.1
        delta_v = delta_t * attraction_terrestre(self.xy[0],self.xy[1])
        self.v = np.add(self.v,delta_v)

        self.xy += self.v

        self.scatter.set_data(self.xy)

balls = [Ball((0.0,ro), (v_init,0.0))]
theta=np.linspace(0,2*np.pi,1000)
ax.plot(ro*np.cos(theta),ro*np.sin(theta),'r')
ax.plot(r_terre*np.cos(theta),r_terre*np.sin(theta))
ax.axis('equal')



def init():
    return []

def animate(t):
    # t is time in seconds
    global xy, v

    for ball in balls:
        ball.update()

    # have to return an iterable
    return [ball.scatter for ball in balls]

# interval in milliseconds
# we're watching in slow motion (delta t is shorter than interval)
ani = animation.FuncAnimation(fig, animate, np.arange(0,100,delta_t), init_func=init, interval=10, blit=True)

plt.show()
