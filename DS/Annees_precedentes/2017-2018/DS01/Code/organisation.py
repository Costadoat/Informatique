# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:49:21 2017

@author: renaud
"""

semaine=1

while semaine < 45:
    #Groupe TD
    if semaine%2==0:
        groupe_td='G1'
    else:
        groupe_td='G2'

    #Groupe TP
    if semaine%3==2:
        groupe_tp='GA'
    elif semaine%3==1:
        groupe_tp='GB'
    else:
        groupe_tp='GC'
        
    if groupe_td=='G1' and groupe_tp=='GC':
        print semaine,groupe_td,groupe_tp,'TP le lundi'
    else:
        print semaine,groupe_td,groupe_tp

    semaine=semaine+1

semaine=1

while semaine < 45:
    #Groupe TD
    if semaine%2==0:
        groupe_td='G1'
    else:
        groupe_td='G2'

    #Groupe TP
    if semaine%3==2:
        groupe_tp='GA'
    elif semaine%3==1:
        groupe_tp='GB'
    elif semaine%3==3:
        groupe_tp='GC'
    else:
        groupe_tp='GD'
        
    if groupe_td=='G1' and groupe_tp=='GC':
        print semaine,groupe_td,groupe_tp,'TP le lundi'
    else:
        print semaine,groupe_td,groupe_tp

    semaine=semaine+1
    
    

def puissance_deux(n):
    y, n_loc = 1, n
    if n>0:
        while n_loc > 0:
            y=y*2
            n_loc = n_loc-1
    else:
        while n_loc < 0:
            y=y/2.
            n_loc = n_loc+1
    return y
    
print puissance_deux(-3)
    
    