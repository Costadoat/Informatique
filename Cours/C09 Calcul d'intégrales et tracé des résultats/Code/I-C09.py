# integration numerique par la methode des rectangles avec alpha = a

from math import pi
import numpy as np
import matplotlib.pyplot as plt

xmin = 0
xmax = 3*pi/2
nbx = 20 # nombre de points à modifier pour améliorer la précision
nbi = nbx - 1 # nombre d'intervalles

x = np.linspace(xmin, xmax, nbx)
inta = np.linspace(1, 1, nbx)
intb = np.linspace(1, 1, nbx)
y = np.cos(x)
plt.plot(x,y,"b", linewidth=3,label='cos(x)')

inta[0]=0
intb[0]=0
for i in range(nbi):
    inta[i+1] = inta[i] + y[i]*(x[i+1]-x[i])
    intb[i+1] = intb[i] + y[i+1]*(x[i+1]-x[i])
    # tracé des rectangles
    x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets
    y_rect = [0   , y[i], y[i]  , 0     , 0   ] # ordonnees des sommets
    #plt.plot(x_rect, y_rect,"r")

plt.plot(x[0:nbx-1], inta[0:nbx-1],"o",label='rect (a)')
plt.plot(x[0:nbx-1], intb[0:nbx-1],"o",label='rect (b)')

intt = np.linspace(1, 1, nbx)
intt[0]=0
for i in range(nbi):
    intt[i+1] = intt[i] + (y[i+1]+y[i])*(x[i+1]-x[i])/2
    # dessin du rectangle
    x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets
    y_rect = [0   , y[i], y[i+1]  , 0     , 0   ] # ordonnees des sommets
    plt.plot(x_rect, y_rect,"r")

plt.plot(x[0:nbx-1], intt[0:nbx-1],"o",label='trapezes')
y = np.sin(x)
plt.plot(x,y,"y",label='sin(x)')
plt.legend()
plt.show()

#Exercices

def carre(x):
    return x * x

xmin = 0
xmax = 1
nb = 100

dx = (xmax - xmin) / nb

integ = 0

for i in range(nb):
    x = xmin + i * dx
    integ += carre(x) * dx

print("Intégrale de x**2 entre xmin =", xmin, "et xmax =", xmax, "avec nb =", nb)
print("Résultat numérique: ", integ)
theorie = (xmax ** 3 - xmin ** 3) / 3
print("Résultat analytique:", theorie)
print("Erreur relative:", (integ / theorie - 1))



#Tracé de courbes

# Exemple 1:

import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(1,6))
y = np.array([2, 3, 5, 4, 1])
plt.plot(x, y)

plt.show()

plt.close()
# Exemple 2:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)

plt.show()

plt.close()
# Exemple 3:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)
y = np.sin(x)
plt.plot(x, y)
plt.xlim(np.pi/4, 3*np.pi/4)
plt.ylim(0.6, 1)

plt.show()

plt.close()

# Exemple 4:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)
y = np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.legend()
plt.title("Fonction sinus")
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.show()

plt.close()

# Exemple 5:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 20)
y = np.cos(x)
plt.plot(x, y, "o-", label="ligne -")
plt.plot(x, y-0.5, "o--", label="ligne --")
plt.plot(x, y-1, "o:", label="ligne :")
plt.plot(x, y-1.5, "o-.", label="ligne -.")
plt.plot(x, y-2, "o", label="pas de ligne")
plt.legend()

plt.show()

plt.close()

# Exemple 6:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 1, 0, 0])
y = np.array([0, 0, 1, 1, 0])
plt.plot(x, y)

theta = np.linspace(0, 2*np.pi, 40)

x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y)
plt.axis("equal")

plt.show()

plt.close()

# Exemple 7:

import numpy as np
import matplotlib.pyplot as plt

t=[]
v=[]

t1 = np.linspace(0, 1, 10)
v1 = 5*np.sin(t1*np.pi/1-np.pi/2)+5
t2 = np.linspace(1, 3, 20)
v2 = 10*t2/t2
t3 = np.linspace(3, 5, 20)
v3 = -5*np.sin((t3-3)*np.pi/2-np.pi/2)+5

t.extend(t1)
t.extend(t2)
t.extend(t3)
v.extend(v1)
v.extend(v2)
v.extend(v3)

plt.plot(t, v)
plt.title("Trapeze de vitesse")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.ylim(0, 12)

plt.show()
