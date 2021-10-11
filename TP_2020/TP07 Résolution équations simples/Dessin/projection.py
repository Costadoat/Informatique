
from math import * 
import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(5,15,100)
plt.plot(t,3*t,'k')
a=10
b=3*a+1
#plt.plot([6,8.1,9,a,12,12.7,14],[3*6+1,3*8.1-2,3*9-2,b,3*12+3,3*12.7-0.8,3*14+1],'.')


ax = plt.axes()
ax.arrow(a, 3*a, a, 3*a, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.show()