import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import mysql.connector
import numpy as np

# Insertion carte de France
img=mpimg.imread('carte_france.png')
imgplot = plt.imshow(img, interpolation='none', aspect='auto')


# Connection base de données
cnx = mysql.connector.connect(user='dorian', password='dorian',
                              host='www.costadoat.fr',
                              database='villes')
# Rayon de la terre
rayon=6371

#Fonction calcul_coord qui convertit les string latitude et longitude en angles en degrés
def calcul_coord(data):
    signe=1
    data1=data
    if data[0]=='-':
        signe=-1
        data1=data[1:]
    elif  data[0]=='+':
        data1=data[1:]
    return signe*(float(data1[-6:-4])+float(data1[-4:-2])/60.+float(data1[-2:])/3600.)


#Requète SQL coordonnées Nice et Brest
cursor = cnx.cursor()
query = ("SELECT ville_nom_reel, ville_latitude_dms, ville_longitude_dms, ville_population_2010 AS Population FROM villes_france_free WHERE ville_nom_reel='Brest' OR ville_nom_reel='Nice'")
cursor.execute(query)
coord_ini=[]

for (ville_nom_reel, ville_latitude_dms, ville_longitude_dms, ville_population_2010) in cursor:
    coord_ini.append([calcul_coord(ville_latitude_dms), calcul_coord(ville_longitude_dms)])

cursor.close()

# Coordonnées de ces villes en pixel sur la carte
coord_carte=[[679,753],[1967,1489]]

# Calcul de l'échelle de la carte
distance_ns=rayon*np.tan(np.pi*(coord_ini[1][0]-coord_ini[0][0])/180.)
distance_eo=rayon*np.tan(np.pi*(coord_ini[1][1]-coord_ini[0][1])/180.)
echelle=[[distance_ns/(coord_carte[1][1]-coord_carte[0][1])],[distance_eo/(coord_carte[1][0]-coord_carte[0][0])]]

# Tracé des villes Nice et Brest
#plt.scatter(coord_carte[0][0],coord_carte[0][1],s=10)
#plt.scatter(coord_carte[1][0],coord_carte[1][1],s=10)

# Fonction place_ville qui permet de placer une ville en fonction de ses coordonnées GPS au format string
def place_ville(data_lat,data_long):
    coord_ville=[calcul_coord(data_lat),calcul_coord(data_long)]
    distance_ns_1=rayon*np.tan(np.pi*(coord_ville[0]-coord_ini[0][0])/180.)/echelle[0]+coord_carte[0][1]
    distance_eo_1=rayon*np.tan(np.pi*(coord_ville[1]-coord_ini[0][1])/180.)/echelle[1]+coord_carte[0][0]
    plt.scatter(distance_eo_1,distance_ns_1,s=10,c ='red')

#Requète SQL sur les villes que l'on choisit de placer
cursor = cnx.cursor()
# Villes de moins de 10 habitants
query = ("SELECT ville_nom_reel, ville_latitude_dms,ville_longitude_dms, ville_population_2010 AS Population FROM villes_france_free WHERE ville_population_2010<10")
# Département 40
#query = ("SELECT ville_nom_reel, ville_latitude_dms,ville_longitude_dms, ville_population_2010 AS Population FROM villes_france_free WHERE ville_departement=40")
# Départements dont la population a diminué entre 1999 et 2010
#query= ("SELECT ville_nom_reel, ville_latitude_dms,ville_longitude_dms, ville_population_2010 AS Population FROM villes_france_free V JOIN (SELECT ville_departement FROM villes_france_free GROUP BY ville_departement HAVING SUM(ville_population_2010)-SUM(ville_population_1999)<0) D ON D.ville_departement=V.ville_departement")

for (ville_nom_reel, ville_latitude_dms, ville_longitude_dms, ville_population_2010) in cursor:
    #print(ville_nom_reel, ville_latitude_dms, ville_longitude_dms)
    place_ville(ville_latitude_dms, ville_longitude_dms)

cursor.close()

# Tracé de la figure
plt.axis('equal')
plt.show()

# Fermeture de la connexion à la base
cnx.close()
