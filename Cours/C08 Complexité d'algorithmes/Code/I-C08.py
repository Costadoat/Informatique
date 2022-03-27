# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 15:56:33 2015

@author: Renaud
"""
import numpy as np

tab=[1,3,4,5,7,8,2,6,9]

print(tab)

for i in range(1,len(tab)-1):
    min=i
    for j in range(i+1,len(tab)):
        if tab[j] < tab[min]:
            min=j
    tmp=tab[i]
    tab[i]=tab[min]
    tab[min]=tmp
print(tab)



def factorielle(n) :
    if  n==0:
        return 1
    else:
        i, res=1, 1
        while i<=n:
            res=res*i
            i=i+1
        return res
        
print(factorielle(4))

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

liste=[]
naive=[]
dicho=[]

def number_in_list(nb,tab):
    a = 0
    for i in range(len(tab)):
        if tab[i]==nb:
            return a
        a=a+1
    return False
    
def number_in_list_dicho(nb,tab):
    a, g, d = 0, 0, len(tab)-1
    while g <= d:
        m = (g + d) // 2
        if tab[m] == nb:
            return a
        if tab[m] < nb:
            g = m+1
        else:d = m-1
        a=a+1
    return False


max=1000
for nb_list in range(1,max):
    print(str(nb_list/max*100)+"%")
    a, b=0, 0
    tab=range(1,nb_list)
    for nb in tab:
        if number_in_list(nb,tab)>a:
            a=number_in_list(nb,tab)
        if number_in_list(nb,tab)>b:
            b=number_in_list_dicho(nb,tab)
    liste.append(nb_list);
    naive.append(a);
    dicho.append(b);
    #print nb_list, a,b
plt.plot(liste, naive,"g",label='Boucles (naive)')
plt.plot(liste, dicho,"r",label='Boucles (dichotomie)')
plt.legend()
plt.show()
