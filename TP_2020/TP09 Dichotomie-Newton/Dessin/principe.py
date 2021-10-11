import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(1,4,100)
Y=X**2-4
X_tangente=np.linspace(0,1,5)
Y_tangente=X

plt.text(2,1, r'$a$', color='k')

plt.plot(X,Y,color='red')
plt.plot(X_tangente,X_tangente,color='green') #tangente en 1
plt.plot(X_tangente,-2*X_tangente+2,color='green') #tangente en 0
plt.plot(np.linspace(1,1,10),np.linspace(-2,1,10),'--',color='blue') # verticale en 1
plt.plot(np.linspace(0,0,10),np.linspace(-2,2,10),'--',color='blue') # verticale en 0

#plt.xticks(np.linspace(2,3,2),['$a$','$x_0$'],fontsize=10)

plt.axhline(y=0,color='black')

#plt.savefig('Newton_boucle.pdf')
plt.close