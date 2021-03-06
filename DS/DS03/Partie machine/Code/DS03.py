import matplotlib.pyplot as plt
import numpy as np

a=[1.49*10**11,2.27944*10**11]
#e=0.82
G=6.67*10**(-11)
msoleil=1.97*10**30
e=[0,016,0,093]
m=[6*10**24,6.418*10**23]

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Question 1:
def rayon(a,e,theta):
    return a*(1-e**2)/(1+e*np.cos(theta))

def aire(a,e,i):
    return 0.5*rayon(a,e,theta[i+1])*rayon(a,e,theta[i])*np.sin(theta[i+1]-theta[i])

def periode(a,m):
    P=np.sqrt(4*a**3*np.pi**2/(G*(m+msoleil)))
    return P/(3600*24)

theta=np.arange(0,2*np.pi,0.001)
pourcent=0.05
aire_mois=[]
for planete in range(2):

    P=periode(a[planete],m[planete])
    print(P)

    aire_totale=0
    for i in range(len(theta)-1):
        aire_totale+=aire(a[planete],e[planete],i)

    aire_mois.append(aire_totale/(P/30))
    aire_int=0
    i=0
    liste_points=[]
    while i < len(theta)-1:
        while aire_int<aire_mois[planete] and i < len(theta)-1:
            aire_int+=aire(a[planete],e[planete],i)
            i+=1
        aire_int=0
        liste_points.append(theta[i])

    plt.polar(theta,rayon(a[planete],e[planete],theta))
    ax.scatter(liste_points, rayon(a[planete],e[planete],liste_points))
#plt.show()

asonde=(a[0]+a[1])/2
esonde=(a[1]-a[0])/(a[0]+a[1])
msonde=10**30

aire_int=0
i=0
liste_points=[]
while i < len(theta)-1:
    while aire_int<aire_mois[0] and i < len(theta)-1:
        aire_int+=aire(asonde,esonde,i)
        i+=1
    aire_int=0
    liste_points.append(theta[i])
print(liste_points)


Ps=np.sqrt(4*asonde**3*np.pi**2/(G*(msonde+msoleil)))
Ps=Ps/(3600*24)
print(Ps)

plt.polar(theta,rayon(asonde,esonde,theta))
ax.scatter(liste_points, rayon(asonde,esonde,liste_points))
plt.show()



