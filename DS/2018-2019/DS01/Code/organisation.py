# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:49:21 2017

@author: renaud
"""

print "Solution de départ"
semaine=1

while semaine < 45:
    #Piscine
    if semaine%6==1:
        piscine='6A'
    elif semaine%6==3:
        piscine='6B'
    elif semaine%6==5:
        piscine='6C'
    else:
        piscine=''
 
    #Sport collectif
    if semaine%3==2:
        foot='6A'
        basket='6C'
        volley='6B'
    elif semaine%3==1:
        foot='6B'
        basket='6A'
        volley='6C'
    else:
        foot='6C'
        basket='6B'
        volley='6A'

    print "Semaine %s \t Piscine %s \t Football %s \t Basket %s \t Volley %s" % (semaine, piscine, foot, basket, volley)
    semaine=semaine+1

print "Solution du prof de techno"
semaine=1

while semaine < 45:
    #Piscine
    if semaine%6==1:
        piscine='6A'
    elif semaine%6==3:
        piscine='6B'
    elif semaine%6==5:
        piscine='6C'
 
    #Sport collectif
    if semaine%3==2:
        foot='6A'
        basket='6C'
        volley='6B'
    elif semaine%3==1:
        foot='6B'
        basket='6A'
        volley='6C'
    else:
        foot='6C'
        basket='6B'
        volley='6A'

    print "Semaine %s \t Piscine %s \t Football %s \t Basket %s \t Volley %s" % (semaine, piscine, foot, basket, volley)
    semaine=semaine+1

print "Solution corrigée"
semaine=1

while semaine < 45:
    #Piscine
    if semaine%6==1:
        piscine='6A'
    elif semaine%6==3:
        piscine='6B'
    elif semaine%6==5:
        piscine='6C'
    else:
        piscine=''
 
    #Sport collectif
    if semaine%3==2:
        foot='6A'
        basket='6C'
        volley='6B'
    elif semaine%3==1:
        foot='6B'
        basket='6A'
        volley='6C'
    else:
        foot='6C'
        basket='6B'
        volley='6A'

    if piscine==foot:
        foot=''
    elif piscine==basket:
        basket=''
    elif piscine==volley:
        volley=''
    print "Semaine %s \t Piscine %s \t Football %s \t Basket %s \t Volley %s" % (semaine, piscine, foot, basket, volley)
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
    
    
