# -*- coding: utf-8 -*-
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt



a=1
b=2
eps=0.001

def f(x):
    return(1./2*(x+2/float(x)))
    
def g(x):
    return(f(x)-x)

def Dicho(g,a,b,eps):
    compteur=0
    while b-a>2*eps :
        compteur=compteur+1
        c=(a+b)/float(2)
        if g(a)*g(c)<0:
            b=c
        else :
            a=c
    return(c,compteur)
    
u=2
n=Dicho(g,a,b,eps)[1] # nombre d iterations



def ResolutionRec(f,u,eps):
    for i in range(n):
        u=f(u)
    return(u)   
    
  
    

print(Dicho(g,a,b,eps))        
print(ResolutionRec(f,u,n)) 
print(sqrt(2))

t=10
m=0.2
X=np.linspace(m,t,100)
Y=np.vectorize(f)(X)
Xn=np.linspace(-t,-m,100)
Yn=np.vectorize(f)(Xn)

plt.clf()
plt.xlim(-3,3)
plt.axis('equal')
plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.plot(X,Y,color='black')
plt.plot(Xn,Yn,color='black')
plt.plot(np.linspace(-t,t,100),np.linspace(-t,t,100))
plt.plot([t,f(t),f(t),f(f(t)),f(f(t)),f(f(f(t)))],[f(t),f(t),f(f(t)),f(f(t)),f(f(f(t))),f(f(f(t)))],color='red')
plt.xticks([t,f(t),f(f(t)),f(f(f(t)))],['$u_0$','$u_1$','$u_2$','$u_3$' ],fontsize=10)
plt.yticks([-5,0,5],['$-5$','$0$','$5$' ],fontsize=10)
plt.title('Tracer de la suite recurrente')
plt.savefig('TracerSuite.pdf')