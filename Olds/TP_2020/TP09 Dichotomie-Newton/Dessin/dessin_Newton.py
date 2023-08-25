import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-2,2,100)
Y=X**3-2*X+2
X_tangente=np.linspace(-0.4,1.2,5)
Y_tangente=X


plt.plot(X,Y,color='red')
plt.plot(X_tangente,X_tangente,color='green') #tangente en 1
plt.plot(X_tangente,-2*X_tangente+2,color='green') #tangente en 0
plt.plot(np.linspace(1,1,10),np.linspace(0,1,10),'--',color='blue') # verticale en 1
plt.plot(np.linspace(0,0,10),np.linspace(0,2,10),'--',color='blue') # verticale en 0


plt.text(-0.1,-0.6, r'$x_0=0$', color='k')
plt.text(0.9,-0.6, r'$x_1=1$', color='k')

plt.axhline(y=0,color='black')

plt.title('Methode de Newton qui boucle')

plt.savefig('Newton_boucle.pdf')
plt.close