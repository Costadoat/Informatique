# Question 1:
import matplotlib.pyplot as plt
import numpy as np
    
# Question 2:
def rayon(a,e,theta):
    return a*(1-e**2)/(1+e*np.cos(theta))

# Question 3:
aterre=1.49*10**11
eterre=0.016

theta=np.arange(0,2*np.pi,0.001)
plt.polar(theta,rayon(aterre,eterre,theta))
plt.show()

# Question 4:
G=6.67*10**(-11)
msoleil=1.97*10**30
mterre=6*10**24
def periode(a,m):
    P=np.sqrt(4*a**3*np.pi**2/(G*(m+msoleil)))
    return P/(3600*24)

P=periode(aterre,mterre)
print(P)
print("On trouve moins de 365 jours, cela est dû aux hypothèses de la modélisation.")

# Question 5:
def calcul_aire(a,e,i):
    return 0.5*rayon(a,e,theta[i+1])*rayon(a,e,theta[i])*np.sin(theta[i+1]-theta[i])
print(calcul_aire(aterre,eterre,0))

# Question 6:

def calcul_aire_ellipse(a,e):
    aire_t=0
    for i in range(len(theta)-1):
        aire_t+=calcul_aire(a,e,i)
    return aire_t

aire_ellipse=calcul_aire_ellipse(aterre,eterre)
print(aire_ellipse)

# Question 7:
def calcul_aire_mois(aire_ellipse,P):
    return aire_ellipse/(P/30)
aire_mois=calcul_aire_mois(aire_ellipse,P)
print(aire_mois)

# Question 8:
def gen_liste_points(a,e,aire_mois):
    aire_int=0
    i=0
    liste_points=[]
    while i < len(theta)-1:
        while aire_int<aire_mois and i < len(theta)-1:
            aire_int+=calcul_aire(a,e,i)
            i+=1
        aire_int=0
        liste_points.append(theta[i])
    return liste_points
print(gen_liste_points(aterre,eterre,aire_mois))

# Question 9:
a=[1.49*10**11,2.27944*10**11]
e=[0.016,0.093]
m=[6*10**24,6.418*10**23]

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

for planete in range(2):
    P=periode(a[planete],m[planete])
    print(P)
    aire_ellipse=calcul_aire_ellipse(a[planete],e[planete])
    aire_mois=calcul_aire_mois(aire_ellipse,P)
    liste_points=gen_liste_points(a[planete],e[planete],aire_mois)
    plt.polar(theta,rayon(a[planete],e[planete],theta))
    ax.scatter(liste_points, rayon(a[planete],e[planete],liste_points))

plt.show()

# Question 10:
a=[1.49*10**11,2.27944*10**11]
e=[0,0]
m=[6*10**24,6.418*10**23]

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

for planete in range(2):
    P=periode(a[planete],m[planete])
    aire_ellipse=calcul_aire_ellipse(a[planete],e[planete])
    aire_mois=calcul_aire_mois(aire_ellipse,P)
    liste_points=gen_liste_points(a[planete],e[planete],aire_mois)
    plt.polar(theta,rayon(a[planete],e[planete],theta))
    ax.scatter(liste_points, rayon(a[planete],e[planete],liste_points))

asonde=(a[0]+a[1])/2
esonde=(a[1]-a[0])/(a[0]+a[1])

P=periode(a[0],m[0])
aire_ellipse=calcul_aire_ellipse(a[0],e[0])
aire_mois=calcul_aire_mois(aire_ellipse,P)
liste_points=gen_liste_points(asonde,esonde,aire_mois)
plt.polar(theta,rayon(asonde,esonde,theta))
ax.scatter(liste_points, rayon(asonde,esonde,liste_points))

plt.show()

# Question 11:

print("On trouve une durée entre 7 et 8 mois.")
#####################################################################
from datetime import date,  timedelta

def parse(my_date):
    d, m, y = map(int, my_date.split('/'))
    return date(y, m, d)
 
def mois_diff(date_1, date_2):
    return abs((parse(date_1) - parse(date_2)).days)

DATE_1 = '30/7/2020'
DATE_2 = '18/2/2021'
mois = mois_diff(DATE_1,  DATE_2)/30
print("%.01f mois" % mois)
