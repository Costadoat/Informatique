# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Renaud.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def ligne_droite(x,y,Lx,Ly,n):
    for i in range(1,n+1):
        x.append((Lx/n)+x[-1])
        y.append((Ly/n)+y[-1])
    
def tourner(x,y,R,a_0,a,sx,sy,n):
    x_0,y_0=x[-1],y[-1]
    for i in range(1,n+1):
        theta=a_0+a*np.pi*i/n
        x.append((x_0+sx*R)+R*np.cos(theta))
        y.append((y_0+sy*R)+R*np.sin(theta))
        
x,y=[7.5],[-5]
ligne_droite(x,y,0.,210.,10)
for i in range(2):
    tourner(x,y,7.5,np.pi,-1,1,0,10)
    ligne_droite(x,y,0.,-210.,10)
    tourner(x,y,7.5,-np.pi,1,1,0,10)
    ligne_droite(x,y,0.,210.,10)
tourner(x,y,7.5,np.pi,-1,1,0,10)
ligne_droite(x,y,0.,-220.,10)
tourner(x,y,7.5,0,-1/2.,-1,0,10)
ligne_droite(x,y,-60.,0.,10)
tourner(x,y,7.5,-np.pi/2,-1/2.,0,1,10)

someX, someY = 0, 0
plt.figure()
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX - .1, someY - .1), 90, 200,alpha=1, facecolor='grey'))
plt.plot(x, y)
plt.axis([-20, 120, -40, 240])
plt.show()
