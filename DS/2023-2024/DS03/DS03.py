import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# QUESTION 1

img=mpimg.imread('paris-map_b.png')
imgplot = plt.imshow(img, interpolation='none', aspect='auto')
plt.axis('equal')
plt.savefig('img/fig00.png')
plt.show()
imgplot = plt.imshow(img, interpolation='none', aspect='auto')

# QUESTION 2
file=open('metro-paris-init.csv','r')
lignes=file.read().split('\n')
file.close()

stations_init=[]

for ligne in lignes[1:-1]:
    data=ligne.split(';')
    lati=float(data[4])
    long=float(data[3])
    stations_init.append([data[2],[lati,long]])

print(stations_init)

# QUESTION 3

# CODE FOURNI

# Coordonnées des stations en équivalent pixel sur la carte
coord_carte=[[197,187],[818,136.5],[1376.6,607.3],[706.6,792.2]]

# Calcul de l'échelle de la carte
rayon_terre=6361
distance_ns=rayon_terre*np.tan(np.pi*(stations_init[1][1][0]-stations_init[0][1][0])/180.)
distance_eo=rayon_terre*np.tan(np.pi*(stations_init[1][1][1]-stations_init[0][1][1])/180.)
echelle=[[distance_ns/(coord_carte[1][1]-coord_carte[0][1])],[distance_eo/(coord_carte[1][0]-coord_carte[0][0])]]

# Fonction pour convertir les coordonnées GPS en équivalent pixel sur la carte image
def gps_to_map(coord_station):
    coord_px_x=rayon_terre*np.tan(np.pi*(coord_station[1]-stations_init[0][1][1])/180.)/echelle[1]+coord_carte[0][0]
    coord_px_y=rayon_terre*np.tan(np.pi*(coord_station[0]-stations_init[0][1][0])/180.)/echelle[0]+coord_carte[0][1]
    return coord_px_x,coord_px_y

# Tracé des stations sur la carte
for idx,station in enumerate(stations_init):
    coord_px_x,coord_px_y=gps_to_map(station[1])
    plt.scatter(coord_px_x,coord_px_y,s=30,c ='red')

# Tracé de la figure
plt.axis('equal')
plt.savefig('img/fig01.png')
plt.show()
imgplot = plt.imshow(img, interpolation='none', aspect='auto')

# QUESTION 4

file=open('metro-paris.csv','r')
lignes=file.read().split('\n')
file.close()

stations=[]
x=[]
y=[]
for ligne in lignes[1:-1]:
    data=ligne.split(';')
    lati=float(data[4])
    long=float(data[3])
    if data[1]=='1':
        stations.append([data[2],[lati,long]])
        coord_px_x,coord_px_y=gps_to_map([lati,long])
        plt.scatter(coord_px_x,coord_px_y,s=30,c ='red')

plt.axis('equal')
plt.savefig('img/fig02.png')
plt.show()
imgplot = plt.imshow(img, interpolation='none', aspect='auto')

# QUESTION 5

file=open('metro-paris.csv','r')
lignes=file.read().split('\n')
file.close()

stations=[]
x=[]
y=[]
for ligne in lignes[1:-1]:
    data=ligne.split(';')
    lati=float(data[4])
    long=float(data[3])
    if data[1]=='1':
        stations.append([data[2],[lati,long]])
        coord_px_x,coord_px_y=gps_to_map([lati,long])
        plt.scatter(coord_px_x,coord_px_y,s=30,c ='red')
        x.append(coord_px_x)
        y.append(coord_px_y)

plt.plot(x,y)
plt.axis('equal')
plt.savefig('img/fig02.png')
plt.show()
imgplot = plt.imshow(img, interpolation='none', aspect='auto')

# QUESTION 6

def distance(stationA,stationB):
    phi1=stationA[1][0]*np.pi/180
    phi2=stationB[1][0]*np.pi/180
    deltalambda=(stationB[1][1]-stationA[1][1])*np.pi/180
    return np.arccos(np.sin(phi1)*np.sin(phi2)+np.cos(phi1)*np.cos(phi2)*np.cos(deltalambda))*rayon_terre

print(distance(stations_init[0],stations_init[2]))
print(distance(stations_init[1],stations_init[3]))

# QUESTION 7

liste_station_ordre=[stations[0]]
for idx_sta in range(len(stations)-1):
    min=20
    for station in stations:
        if station not in liste_station_ordre and distance(liste_station_ordre[-1],station)<min:
            min=distance(liste_station_ordre[-1],station)
            next_station=station
    liste_station_ordre.append(next_station)

x=[]
y=[]
for station in liste_station_ordre:
    coord_px_x,coord_px_y=gps_to_map(station[1])
    plt.scatter(coord_px_x,coord_px_y,s=30,c ='red')
    x.append(coord_px_x)
    y.append(coord_px_y)

plt.plot(x,y)


# Tracé de la figure
plt.axis('equal')
plt.savefig('img/fig03.png')
plt.show()
imgplot = plt.imshow(img, interpolation='none', aspect='auto')

# QUESTION 8

liste_station_ordre=[stations[0]]
distances=[0]
for idx_sta in range(len(stations)-1):
    min=20
    for station in stations:
        if station not in liste_station_ordre and distance(liste_station_ordre[-1],station)<min:
            min=distance(liste_station_ordre[-1],station)
            next_station=station
    distances.append(int(1000*min+distances[-1]))
    liste_station_ordre.append(next_station)

print(distances)


# QUESTION 9
L=[1,3,5,7,10,13]

def dichotomie(L, a):
    debut = 0
    fin = len(L) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if L[m] == a:
            return m
        elif L[m] < a:
            debut = m+1
        else:
            fin = m-1
    return False

print(dichotomie(L, 12))

# QUESTION 10

def dichotomie_inter(L, a):
    debut = 0
    fin = len(L) - 1
    while debut+1 < fin:
        m = (debut+fin) // 2
        if L[m] == a:
            return m
        elif L[m] < a:
            debut = m
        else:
            fin = m
    return debut,fin

print(dichotomie_inter(L, 12))

# QUESTION 11

print(dichotomie_inter(distances, 10000))

# QUESTION 12   

def trace_ligne(numero):
    file=open('metro-paris.csv','r')
    lignes=file.read().split('\n')
    file.close()

    stations=[]

    x=[]
    y=[]
    for ligne in lignes[1:-1]:
        data=ligne.split(';')
        lati=float(data[4])
        long=float(data[3])
        if data[1]==str(numero):
            stations.append([data[2],[lati,long]])
            coord_px_x,coord_px_y=gps_to_map([lati,long])
            plt.scatter(coord_px_x,coord_px_y,s=30,c ='red')
            x.append(coord_px_x)
            y.append(coord_px_y)

    liste_station_ordre=[stations[0]]
    for idx_sta in range(len(stations)-1):
        min=1
        for station in stations:
            if station not in liste_station_ordre and distance(liste_station_ordre[-1],station)<min:
                min=distance(liste_station_ordre[-1],station)
                next_station=station
        liste_station_ordre.append(next_station)

    x=[]
    y=[]
    for station in liste_station_ordre:
        coord_px_x,coord_px_y=gps_to_map(station[1])
        plt.scatter(coord_px_x,coord_px_y,s=30,c ='red')
        x.append(coord_px_x)
        y.append(coord_px_y)

    plt.plot(x,y)


    # Tracé de la figure
    plt.axis('equal')
    plt.savefig('img/fig04.png')
    plt.show()
    imgplot = plt.imshow(img, interpolation='none', aspect='auto')

trace_ligne(4)


