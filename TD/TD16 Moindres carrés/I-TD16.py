"""
Ajustement d'un plan par moindres carrés sur un nuage de points 3D.
Équation du plan : z = a*x + b*y + c
"""

import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # nécessaire pour la projection 3D

# 1. Lecture des données
x, y, z = [], [], []
file=open('points.csv', 'r')
contenu=file.read()
lignes=contenu.split('\n')
for ligne in lignes[:-1]:
    row=ligne.split(';')
    x.append(float(row[0]))
    y.append(float(row[1]))
    z.append(float(row[2]))

x = np.array(x)
y = np.array(y)
z = np.array(z)
n = len(x)

def permutation(A,i,j):
    t = A[i]
    A[i] = A[j]
    A[j] = t
    
def transvection(A,i,j,x):
    # si vecteur
    if type(A[0]) != list:
        A[i] = A[i] + x*A[j]
    else:
        n = len(A[0])
        for k in range(n):
            A[i][k] = A[i][k] + x*A[j][k]
    
def recherche_pivot(A, j0):
    n = len(A) 
    imax = j0 
    for i in range(j0+1, n):
        if abs(A[i][j0]) > abs(A[imax][j0]):
            imax = i
    return imax

def triangle(A,b):
    n =len(b)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/ A[i][i]
    return x
    
def resolution_systeme(A,b):
    n = len(A)

    for i in range(n-1):
        i0 = recherche_pivot(A,i)
        permutation(A,i,i0)
        permutation(b,i,i0) 
        
        for k in range(i+1,n):
            x = A[k][i]/A[i][i]
            transvection(A,k,i,-x)
            transvection(b,k,i,-x) 
            
    return triangle(A,b)

# 2. Construction du système des équations normales (sans column_stack ni @)
# On calcule directement les sommes issues des dérivées de E(a,b,c) = Σ(z_i - a*x_i - b*y_i - c)^2
 
Sx   = 0.0
Sy   = 0.0
Sxx  = 0.0
Syy  = 0.0
Sxy  = 0.0
Sxz  = 0.0
Syz  = 0.0
Sz   = 0.0
 
for i in range(n):
    Sx  += x[i]
    Sy  += y[i]
    Sxx += x[i]*x[i]
    Syy += y[i]*y[i]
    Sxy += x[i]*y[i]
    Sxz += x[i]*z[i]
    Syz += y[i]*z[i]
    Sz  += z[i]
 
# Système 3x3 : AtA * [a, b, c]^T = Atz
AtA = np.array([
    [Sxx, Sxy, Sx],
    [Sxy, Syy, Sy],
    [Sx,  Sy,  n ]
])

Atz = np.array([Sxz, Syz, Sz])
 

coeffs = resolution_systeme(AtA, Atz)  # résolution du système 3x3 par pivot de Gauss
a, b, c = coeffs

print(f"Équation du plan : z = {a:.4f} x + {b:.4f} y + {c:.4f}")

# 3. Distances des points au plan
# Plan sous la forme a*x + b*y - z + c = 0
norme = np.sqrt(a**2 + b**2 + 1)
distances = np.abs(a*x + b*y - z + c) / norme

for i in range(n):
    print(f"Point {i+1}: ({x[i]:.2f}, {y[i]:.2f}, {z[i]:.2f}) -> distance = {distances[i]:.4f}")

print(f"\nDistance moyenne : {distances.mean():.4f}")
print(f"Distance max     : {distances.max():.4f}")

# 4. Affichage 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Points
ax.scatter(x, y, z, color='red', label='Points', depthshade=True)

# Grille pour le plan
xx, yy = np.meshgrid(
    np.linspace(x.min(), x.max(), 10),
    np.linspace(y.min(), y.max(), 10)
)
zz = a*xx + b*yy + c

ax.plot_surface(xx, yy, zz, alpha=0.4, color='blue')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Plan des moindres carrés : z = {a:.3f}x + {b:.3f}y + {c:.3f}')
ax.legend()

plt.tight_layout()
plt.savefig('plan_3d.png', dpi=150)
plt.show()
