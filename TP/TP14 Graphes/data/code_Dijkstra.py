#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:44:01 2022

@author: jg
"""
  
 


def etapes(Graphe,depart,final,s_traites,dist,prec):
    """
    Etapes de l'algorithme de Dijkstra (version récursive)
        
    s_traites:  Liste des sommets déjà traités
    dist:       Distances minimales trouvées pour chaque sommet
    prec:       Indique pour chaque sommet, celui qui le précède dans le trajet le plus court trouvé    
    """    
    #on choisit le sommet à traiter:
    if not dist:
        #si aucune distance n'a été calculée, on choisit depart(et on note 0 comme distance pour le depart)
        s_courant=depart
        dist[s_courant]=0 
    else:
        #sinon on choisit un sommet non encore traité dont la distance calculée est minimale 
        non_traites={ s:dist.get(s,float('inf'))  for s in Graphe if s not in s_traites }
        s_courant=min(non_traites, key=non_traites.get)

    #si le sommet courant est celui à atteindre
    if s_courant==final:
        #construction de la liste des sommets, à rebours
        Chaine=[final]
        while Chaine[-1]!=depart:
            Chaine.append(prec[Chaine[-1]])
        #on renvoie la distance minimale trouvée et la liste des sommets
        Chaine.reverse()
        return dist[final],Chaine

    #on traite tous les voisins du sommet courant
    for voisin in Graphe[s_courant]:
        #on récupère la distance précédemment calculée pour ce voisin (+inf si non atteint)
        dist_voisin_prec=dist.get(voisin,float('+inf'))
        #on calcule la nouvelle distance obtenue

        dist_voisin_new=dist[s_courant]+Graphe[s_courant][voisin]
        #on compare les deux distances et on modifie si nécessaire
        if dist_voisin_new<dist_voisin_prec:
            dist[voisin]=dist_voisin_new
            prec[voisin]=s_courant

    #on ajoute le sommet courant à la liste des sommets traites
    s_traites.append(s_courant)

    #on réitère la méthode pour traiter le sommet suivant
    return etapes(Graphe,depart,final,s_traites,dist,prec)

def Dijkstra(Graphe,depart,final):
    """
    Application de l'algorithme de Dijkstra
    
    Graphe:     Graphe fourni sous forme d'un dictionnaire
    depart:     Sommet initial du trajet cherché 
    final:      Sommet final du trajet cherché
    """  
    return etapes(Graphe,depart,final,[],{},{})
      

    


