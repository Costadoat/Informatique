import math as m

#==============================================================================
# préparation d'un dictionnaire destiné à recueillir les données
#==============================================================================
# Chemin d'accès au fichier 
fichier = open('instrument_features.csv','r')

# initialisation dictionnaire
donnees={}

# lecture est stockage des données 
for ligne in fichier: # on parcourt une à une les lignes du fichier
    """chaque ligne du fichier est scindée en liste d'éléments distincts
    grâce à la méthode split à partir du séparateur virgule split(',') 
    après être débarassée des caractères d'espacement et d'échappement 
    (par exemple le caractère de fin de ligne \n) grâce à la méthode strip()"""
    ligne_preparee = ligne.strip().split(',')
    
    cle = ligne_preparee[20]
    liste_valeurs = []
    for valeur in ligne_preparee[0:20]:
        liste_valeurs.append(float(valeur))
    donnees[cle]=liste_valeurs

fichier.close()

liste_instruments = list(donnees.keys())

#==============================================================================
# on demande à l'utilisateur le son-candidat dont il veut trouver l'instrument
#==============================================================================
cle_candidat = 'début'
while cle_candidat not in liste_instruments:
    if cle_candidat == 'début':
        cle_candidat=input('Quel instrument voulez-vous tester (deux lettres deux chiffres : LL CC) ?\n')
    else:
        print("Cet instrument n'existe pas.")
        print('Voici la liste des instruments :')
        print(liste_instruments)
        cle_candidat=input('Quel instrument voulez-vous tester (deux lettres deux chiffres : LL CC) ?\n')

#==============================================================================
# calculs des distances
#==============================================================================

# préparation des données de références
liste_donnees_candidat=donnees[cle_candidat]

# on calcule les distances candidat-référence

dictionnaire_distances = {}

for cle in liste_instruments:
    if cle != cle_candidat:
        somme_carres = 0
        for i in range(0,20):
            somme_carres = somme_carres + (liste_donnees_candidat[i]-donnees[cle][i])**2
        dictionnaire_distances[cle] = m.sqrt(somme_carres)

liste_sons_references = list(dictionnaire_distances.keys())

nom_instrument = liste_sons_references[0]

distance_minimale = dictionnaire_distances[liste_sons_references[0]]
for cle in liste_sons_references[1:]:
     if dictionnaire_distances[cle] < distance_minimale:
         distance_minimale = dictionnaire_distances[cle]
         nom_instrument = cle

#==============================================================================
# affichage de la réponse
#==============================================================================

if nom_instrument[-5:-3] == 'VI':
    print("Cela ressemble à un son de violon. Instrument le plus proche : "+nom_instrument+'.')

elif nom_instrument[-5:-3] == 'TR':
    print("Cela ressemble à un son de trompette. Instrument le plus proche : "+nom_instrument+'.')

elif nom_instrument[-5:-3] == 'PI':
    print("Cela ressemble à un son de piano. Instrument le plus proche : "+nom_instrument+'.')

elif nom_instrument[-5:-3] == 'CL':
    print("Cela ressemble à un son de clarinette. Instrument le plus proche : "+nom_instrument+'.')
    
else:
    print("Cela ne ressemble à rien.")
