# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""
# Import de la bibiliothèque numpy en tant que np
import numpy as np

# Chemin d'accès au fichier 
fichier = open('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Cours et TP/Projet musique/Scripts et fichiers/instrument_features.csv','r')

# préparation d'une liste destinée à recueillir les données des lignes du fichier
donnees=[]

mot='' #caractères d'un mot d'une ligne

# Un fichier est un itérable qu'on peut parcourir ligne à ligne
for ligne in fichier:
    #print len(ligne)
    mots=[] #liste des mots d'une ligne
    
    # une ligne est une chaîne de caractère itérable qu'on peut parcourir 
    # caractère par caractère
    for caractere in ligne:
        #print caractere
        if caractere==',' or caractere=='\n': #s'il y a une virgule ou si la ligne est finie
            mots=mots+[mot] # on ajoute le mot à la liste des mots de la ligne
            mot=''          # le mot est fini, on réinitialise
        else:               # sinon
            mot=mot+caractere   # on ajoute le caractere au mot en cours
    
    donnees=donnees+[mots]      # on a fini la ligne on ajoute la liste des mots
                                # à la liste des lignes ; 
                                # donnees est donc une liste de listes

# print donnees

# la fin du fichier ne peut pas être détectée dans les boucles
# en conséquence, le dernier mot de la dernière ligne n'est pas traité correctement
# on l'ajoute manuellement à la liste des mots et on écrase la dernière ligne
#mots=mots+[mot]
#donnees[-1]=mots


#==============================================================================
## alternative rapide à base de méthodes du coeur de python 
#
#for ligne in fichier: # on parcourt une à une les lignes du fichier
#    """ chaque ligne du fichier est scindée en liste d'éléments distincts
#    grâce à la méthode split à partir du séparateur virgule split(',') 
#    puis débarassée des caractères d'espacement et d'échappement 
#    (par exemple le caractère de fin de ligne \n) grâce à la méthode strip()"""
# 
#    donnees=donnees+[ligne.strip().split(',')] 
#==============================================================================
    

# transformation de la liste de lignes en tableau numpy
donnees=np.array(donnees)
#print donnees.shape
 

# préparation de deux tableaux destinés à recueillir les données numériques 
# et textuelles
# partie numérique : on prépare un tableau de zéros flottants destinés 
# à recueillir toutes les données sauf les deux dernières colonnes
donneesnumeriques=np.zeros((np.shape(donnees)[0],np.shape(donnees)[1]-2),dtype='float')
 
# passage en flottant des données numériques
for i in range(donneesnumeriques.shape[0]):
   for j in range(donneesnumeriques.shape[1]):
        donneesnumeriques[i,j]=float(donnees[i,j])

print donneesnumeriques
# partie textuelle : on isole les deux dernières colonnes
donneestextuelles=donnees[:,np.shape(donnees)[1]-2:np.shape(donnees)[1]]

print donneestextuelles
#==============================================================================
# alternative rapide à base de méthodes du coeur de numpy
#
#donnees=np.array(donnees)
#
#donneesnumeriques=donnees[:,0:np.shape(donnees)[1]-2].astype(float)
#donneestextuelles=donnees[:,np.shape(donnees)[1]-2:np.shape(donnees)[1]]
#==============================================================================



# on demande à l'utilisateur combien de premiers voisins il veut
ordre=int(input("Combien de premiers voisins voulez-vous déterminer (1-59) ? "))

fichier_reponses=open('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Cours et TP/Projet musique/Scripts et fichiers/reponses_ordre'+str(ordre)+'.txt','w')
#fichier_reponses_groupees=open('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Python/Formation/reponses_groupees.txt','w')


## on demande à l'utilisateur le son dont il veut trouver l'instrument
#numero=int(input('Quel numéro de son voulez-vous tester (0-59) ? '))

# on réalise une boucle qui parcourt tous les sons 1 par 1 et
# utilise les autres sons comme références
for numero in range(donneesnumeriques.shape[0]):
    position=numero
    
    # préparation du variant de boucle while
    nombredevoisins=0
    
    # initialisation de la chaîne de caractère contenant les réponses
    # on met le numéro de ligne et le nom de l'instrument qu'on teste
    reponses=str(numero)+','+str(donnees[numero,-1])
        
    # intialisation du compteur de réponses correctes
    bons=0
    
    # préparation des données de références
    donneesnumeriquesreferences=donneesnumeriques
    donneestextuellesreferences=donneestextuelles
    
    # tant qu'on n'a pas déterminé le nombre de premiers voisins demandés on fait
    while nombredevoisins < ordre:
        
        # ajout du séparateur dans la chaîne des réponses    
        reponses=reponses+','
        
        # on élimine du tableau des données de références la ligne correspondant
        # au son testé ou au voisin précédemment trouvé, en créant un nouveau 
        # tableau en concaténant deux sous tableaux dont la ligne du son testé 
        # est exclue 
        donneesnumeriquesreferences=np.concatenate((donneesnumeriquesreferences[0:position,:],donneesnumeriquesreferences[position+1:,:]),axis=0)
        donneestextuellesreferences=np.concatenate((donneestextuellesreferences[0:position,:],donneestextuellesreferences[position+1:donneestextuellesreferences.shape[0],:]),axis=0)        
        print donneestextuellesreferences.shape
        print donneesnumeriquesreferences.shape
        
        # pour chacune des lignes de référence, et pour toutes les colonnes 
        # on calcule les carrés des différences terme à terme avec la ligne 
        # du son testé
        carresdesdifferences=(donneesnumeriques[numero,:]-donneesnumeriquesreferences[:,:])**2
        
        # pour chaque ligne on fait la somme de tous les carrés 
        # (donc on somme les colonnes de carresdesdifferences --> axis=1)
        sommecarres=np.sum(carresdesdifferences,axis=1)
        
        # calcul des distances
        distance=np.sqrt(sommecarres)
        #print distance.shape
        
        # détermination de la ligne qui réalise le minimum de distance
        position=int(np.where(distance==distance.min())[0])
        print position
        
        # on ajoute dans la chaîne des réponses l'instrument du son réalise le 
        # minimum de distance
        reponses=reponses+str(donneestextuellesreferences[position,-1])
        
        # si la réponse trouvée est correcte on incrémente le nombre de correctes
        if donnees[numero,-1]==donneestextuellesreferences[position,-1]:
            bons=bons+1
        
        # on incrémente le nombre de premiers voisins calculés    
        nombredevoisins=nombredevoisins+1
    
    # ajout de la liste des premiers voisins et du nombre de réponses fausses 
    # dans la chaîne des réponses    
    reponses=reponses+','+str(bons)+" bons"+'\n'
    
    # écriture de la chaîne des réponses dans le fichier des réponses    
    fichier_reponses.write(reponses)
    

# fermeture du fichier des réponses
fichier_reponses.close()
