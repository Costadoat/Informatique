import numpy as np
import matplotlib.pyplot as plt

###################Calcul et tracé de la fonction##############################
t=np.linspace(0,0.2,1000)
xi_d=0.2
w0_d=204
K_d=2
s=K_d*(1-np.exp(-w0_d*xi_d*t)/np.sqrt(1-xi_d**2)*np.cos(w0_d*np.sqrt(1-xi_d**2)*t\
                                                      -np.arctan(xi_d/np.sqrt(1-xi_d**2))))
fig1=plt.figure('Réponse 1')
plt.plot(t,s)
plt.plot(t,s[-1]*np.ones(len(t)),'-.',c='#1f77b4')
plt.plot(t,0.95*s[-1]*np.ones(len(t)),'--',c='#1f77b4')
plt.plot(t,1.05*s[-1]*np.ones(len(t)),'--',c='#1f77b4')
plt.savefig('img/fig01.png')
###############################################################################

#Question 2:
K=s[-1]

#Question 3:
def recherche(s):
    val=s[0]
    for i in range(len(s)):
        if s[i] > val:
            val=s[i]
    return val

#Question 4:
i=0
while s[i]!=recherche(s):
    i+=1
Tp=2*t[i]

#Question 5:
def D(xi):
    return 100*np.exp(-xi*np.pi/np.sqrt(1-xi**2))

xi=0.7
while D(xi)<100*(recherche(s)-s[-1])/s[-1]:
    xi+=-0.1

w0=2*np.pi/(Tp*np.sqrt(1-xi**2))

print("Données",K_d,xi_d,w0_d)
print("Identifications",K,xi,w0)

i=-1
while s[i]<1.05*s[-1] and s[i]>0.95*s[-1]:
    i+=-1
t5=t[i]

def tr5(xi,w0):
    return np.log(20)/(xi*w0)

if abs(t5-tr5(xi,w0))<0.1:
    print("OK")
else:
    print("KO")
    
print("Le temps de réponse est %s secondes" % format(t5))
t5=tr5(xi,w0)
print("Le temps de réponse est %s secondes" % format(t5))
plt.plot([t[i],t[i]],[1.1*s[-1],0.9*s[-1]])


fig2=plt.figure('Réponse 2')

while t5>0.025:
    xi+=10**(-3)
    s=K*(1-np.exp(-w0*xi*t)/np.sqrt(1-xi**2)*np.cos(w0*np.sqrt(1-xi**2)*t-np.arctan(xi/np.sqrt(1-xi**2))))
    i=-1
    while s[i]<1.05*s[-1] and s[i]>0.95*s[-1]:
        i+=-1
    t5=t[i+1]


print("Pour xi=%.3f, le temps de réponse est %s secondes" % ((xi),(t5)))
plt.plot([t[i],t[i]],[1.1*s[-1],0.9*s[-1]])
plt.plot(t,s)
plt.plot(t,0.95*s[-1]*np.ones(len(t)))
plt.plot(t,1.05*s[-1]*np.ones(len(t)))


print((2**20-1)/5)
print(2**(-3),2**(-1),2**(-25))
