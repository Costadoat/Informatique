# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""
# Import de la bibiliothèque numpy en tant que np
import numpy as np

# Chemin d'accès au fichier 
fichier = open('/home/willie/Dropbox/Informatique PTSI/TP13 - Projet musique/Scripts et fichiers//instrument_features.csv','r')

# préparation d'une liste destinée à recueillir les données des lignes du fichier
donnees=[]

#==============================================================================
# réponse rapide à base de méthodes du coeur de python 
# sinon reprendre le corrigé du TP6
for ligne in fichier: # on parcourt une à une les lignes du fichier
    """ chaque ligne du fichier est scindée en liste d'éléments distincts
    grâce à la méthode split à partir du séparateur virgule split(',') 
    après être débarassée des caractères d'espacement et d'échappement 
    (par exemple le caractère de fin de ligne \n) grâce à la méthode strip()"""
 
    donnees=donnees+[ligne.strip().split(',')] 
#==============================================================================
    

# transformation de la liste de lignes en tableau numpy
donnees=np.array(donnees)


# préparation de deux tableaux destinés à recueillir les données numériques 
# et textuelles
# partie numérique : on prépare un tableau de zéros flottants destinés 
# à recueillir toutes les données sauf les deux dernières colonnes
donneesnumeriques=np.zeros((np.shape(donnees)[0],np.shape(donnees)[1]-2),dtype='float')
 
# passage en flottant des données numériques
for i in range(donneesnumeriques.shape[0]):
   for j in range(donneesnumeriques.shape[1]):
        donneesnumeriques[i,j]=float(donnees[i,j])


# partie textuelle : on isole les deux dernières colonnes
donneestextuelles=donnees[:,np.shape(donnees)[1]-2:np.shape(donnees)[1]]

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

fichier_reponses=open('/home/willie/Dropbox/Informatique PTSI/TP13 - Projet musique/Scripts et fichiers/reponses_ordre'+str(ordre)+'.txt','w')
#fichier_reponses_groupees=open('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Python/Formation/reponses_groupees.txt','w')


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
        
        # pour chacune des lignes de référence, et pour toutes les colonnes 
        # on calcule les carrés des différences terme à terme avec la ligne 
        # du son testé
        carresdesdifferences=(donneesnumeriques[numero,:]-donneesnumeriquesreferences[:,:])**2
        
        # pour chaque ligne on fait la somme de tous les carrés 
        # (donc on somme les colonnes de carresdesdifferences --> axis=1)
        sommecarres=np.sum(carresdesdifferences,axis=1)
        
        # calcul des distances
        distance=np.sqrt(sommecarres)
        
        # détermination de la ligne qui réalise le minimum de distance
        position=int(np.where(distance==distance.min())[0])
        
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
    if bons>1:
        reponses=reponses+','+str(bons)+" bonnes reponses sur "+str(ordre)+'\n'
    else:
        reponses=reponses+','+str(bons)+" bonne reponse sur "+str(ordre)+'\n'
    
    # écriture de la chaîne des réponses dans le fichier des réponses    
    fichier_reponses.write(reponses)
    

# fermeture du fichier des réponses
fichier_reponses.close()
