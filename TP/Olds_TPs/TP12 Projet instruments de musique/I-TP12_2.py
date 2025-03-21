# python3
# -*- coding: utf-8 -*-

# Ouverture du fichier features
file=open('instrument_features.csv','r')
content=file.read()
file.close()

# Découpage des lignes
lines=content.split("\n")
sound_data=[]

for line in lines[:-1]:
    data=line.split(',')
    sound_data.append((data[:20],data[21]))

# Test du dataset obtenu
# print(len(sound_data))
# print(type(sound_data[0][0]),type(sound_data[0][1]))
# print(sound_data[0][0],sound_data[0][1])


# Fonction qui sert à comparer les deux sons
def compare(son_candidat,son_reference):
    difference=0
    for i in range(len(son_candidat[0])):
        difference+=(float(son_candidat[0][i]) - float(son_reference[0][i]))**2
    return difference

# Choix d'un son candidat
numero_son_candidat=0
son_candidat=sound_data[numero_son_candidat]
# print(son_candidat)

def type_instrument(son_candidat):
    nb_voisins=3
    resultat=[None] * (nb_voisins + 1)
    min_difference=[10**9] * (nb_voisins + 1)
    # Comparaison du son candidat au sons références
    for son_reference in sound_data:
        #Exclusion du son candidat des sons références
        if son_candidat!=son_reference:
            # Calcule de la différence entre les deux sons
            difference=compare(son_candidat,son_reference)
            # On garde le résultat des nb_voisins sons les plus proches
            for i in range(nb_voisins-1,-1,-1):
                if difference<min_difference[i]:
                    min_difference[i+1]=min_difference[i]
                    min_difference[i]=difference
                    resultat[i+1]=resultat[i]
                    resultat[i]=son_reference[1]
    return resultat[:3]

for son_candidat in sound_data:
    print('Réel: ',son_candidat[1],'Voisins: ',type_instrument(son_candidat))
        
