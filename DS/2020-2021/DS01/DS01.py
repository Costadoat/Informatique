import matplotlib.pyplot as plt
import numpy as np

Vr=10.
fr=0.6
k=16

def theta(t):
    return 2*np.pi*fr*t

def v(t):
    return Vr*np.sin(k*theta(t))*np.cos(theta(t))
    
t=np.linspace(0,2,1000)
plt.plot(t,v(t))

print("Recherche du Vrmax")
m=v(0)
for ti in t:
    if v(ti)>m:
        m=v(ti)
print(m)

i=0
m=v(t[i])-1
while v(t[i])<=m :
    if v(t[i])>m:
        m=v(t[i])
print(m)

yc=1
print('Recherche des intervalles [t,t+dt], incluants un passage par v(t)=1')
bornes=[]
for i in range(1,len(t)):
#    if v(t[i-1]) > 1 and v(t[i]) < 1 or v(t[i-1]) < 1 and v(t[i]) > 1:
    if (v(t[i-1])-yc)*(v(t[i])-yc) < 0:
        bornes.append([t[i-1],t[i]])

print(bornes[0:4])

def dichotomie(f,a,b,p):
    m=(a+b)/2.
    while np.abs(f(m)) >  p:
        m=(b+a)/2.
        if f(a)*f(m) > 0:
            a=m
        else:
            b=m
    return m

def g(t):
    return v(t)-yc

print("Recherche par dichotomie")
p=10**(-6)
l1=[]
l2=[]
for borne in bornes:
    x=dichotomie(g,borne[0],borne[1],p)
    if x<1/fr:
        l1.append(x)
        l2.append(v(x))

print(len(l1)/2)
plt.scatter(l1, l2, c = 'red')
plt.grid('on')
plt.show()

print((2**23+(2**24-1)/5)*2**(-24))

print(2**(-24)/5)

print((2**23+(2**24-1)/5)*2**(-24)+2**(-24)/5)
