# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""
    
# Chemin d'accès au fichier     
fichier = file('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Python/Formation/instrument_features.csv')

mot='' #caractères d'un mot
donnees=[] #liste des lignes

for ligne in fichier:
    #print len(ligne)
    mots=[] #liste des mots d'une ligne
    for caractere in ligne:
        #print caractere
        if caractere==',' or caractere=='\n': #s'il y a une virgule ou si la ligne est finie
            mots=mots+[mot] # on ajoute le mot à la liste des mots de la ligne
            mot='' # le mot est fini, on réinitialise
        else:
            mot=mot+caractere # on ajoute le caractere au mot en cours
    donnees=donnees+[mots] # on a fini la ligne on ajoute la liste des mots à la liste des lignes

# la fin du fichier ne peut pas être détectée dans les boucles
# en conséquence, le dernier mot de la dernière ligne ne peut pas être détecté
# on l'ajoute manuellement à la liste des mots et on écrase la dernière ligne
mots=mots+[mot]
donnees[-1]=mots

print len(donnees)

# Chemin d'accès au fichier 
fichier_bis = file('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Python/Formation/instrument_features.csv')
donnees_bis =[]

for ligne in fichier_bis: # on parcourt une à une les lignes du fichier
    #print ligne
    """ chaque ligne du fichier est scindée en liste d'éléments distincts
    grâce à la méthode split à partir du séparateur virgule split(',') 
    puis débarassée des caractères d'espacement et d'échappement 
    (par exemple le caractère de fin de ligne \n) grâce à la méthode strip()"""

    donnees_bis=donnees_bis+[ligne.strip().split(',')] 
    
print len(donnees_bis)    

print donnees == donnees_bis