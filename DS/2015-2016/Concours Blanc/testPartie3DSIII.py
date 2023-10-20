# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:40:16 2015

@author: willie
"""

def estici(motif, texte,i):
    if i==texte.index(motif[0]):
        i=True
    else:
        i=False
    return i
        
print estici('lfekfklezlfzek','Bonjour le monde',8)


def recherche(motif,texte):
    for i in range(len(texte)):
        if motif[0]==texte[i]:
            for e in range(len(motif)):
                if motif[e]==texte[i+e]:
                    return True
        else:
            return False


print recherche('le', 'Bonjour le monde')

