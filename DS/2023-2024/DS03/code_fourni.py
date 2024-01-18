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
plt.show()
imgplot = plt.imshow(img, interpolation='none', aspect='auto')
