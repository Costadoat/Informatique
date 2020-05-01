import numpy as np
import matplotlib.pyplot as plt

#Question 1

rho=500
g=9.81
p=0.1
h=0.2
L=2
E=2.2*10**9
q=rho*g*p*h
print(q)

#Question 2

def Mfz(x):
    return x*q*L/2-q*x**2/2
print(Mfz(1.2))

#Question 3.a

def Ix(e,l):
    return e**3*l/12
print(Ix(0.018,0.3))

#Question 3.b

def ddf(x):
    return (Mfz(x))/(E*Ix(0.018,0.3))
print(ddf(1.2))

#Question 4.a

nbx=1000
x = np.linspace(0, L, nbx)
ddfleche=ddf(x)
print(ddfleche[250])

#Question 4.b

nbi = nbx - 1
dfleche = np.linspace(1, 1, nbx)
dfleche[0]=0
for i in range(nbi):
    dfleche[i+1] = dfleche[i] + ddfleche[i]*(x[i+1]-x[i])
print(dfleche[500])
plt.plot(x[:len(dfleche)],dfleche)

#Question 4.c

dfleche=dfleche-dfleche[500]
plt.plot(x[:len(dfleche)],dfleche)
plt.show()

#Question 4.d

nbi = nbx - 1
fleche = np.linspace(1, 1, nbx)
fleche[0]=0
for i in range(nbi):
    fleche[i+1] = fleche[i] + dfleche[i]*(x[i+1]-x[i])
plt.plot(x[:len(fleche)],fleche)
#plt.show()
print(fleche[500])
print("%f > 2cm, le cahier des charges n'est pas respecté." % (abs(fleche[500])*100))

#Question 5.a

def calcul_fleche(E,e):
    def ddf(x):
        return (Mfz(x))/(E*Ix(e,0.3))
    nbx=1000
    x = np.linspace(0, L, nbx)
    ddfleche=ddf(x)

    nbi = nbx - 1
    dfleche = np.linspace(1, 1, nbx)
    dfleche[0]=0
    for i in range(nbi):
        dfleche[i+1] = dfleche[i] + ddfleche[i]*(x[i+1]-x[i])
    dfleche=dfleche-dfleche[500]
    nbi = nbx - 1
    fleche = np.linspace(1, 1, nbx)
    fleche[0]=0
    for i in range(nbi):
        fleche[i+1] = fleche[i] + dfleche[i]*(x[i+1]-x[i])
    return fleche[500]

print(calcul_fleche(2.2*10**9,0.018))

#Question 5.b

fmax=0.02
liste_mat=[('médium',2.2),('contreplaqué',12.4),('verre',69)]
liste_ep=np.arange(0.001,0.1,0.001)

print('Pour respecter le cahier des charges:')
for (nom,E) in liste_mat:
    i=0
    while abs(calcul_fleche(E*10**9,liste_ep[i]))>fmax:
        i+=1
    print(" - il faudrait une étagère en %s de %imm d'épaisseur" % (nom,1000*liste_ep[i]))
        
