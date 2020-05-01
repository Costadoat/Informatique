# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:13:03 2015

@author: Renaud
"""
print "Exemple norme"
def norme_3(a,b,c):
	n = (a**2 + b**2 + c**2)**(1./2)
	return n

print norme_3(3,4,5)
print norme_3(4,5,6)

print "Somme pairs"
def somme_pairs(a) :
    i=1
    n=0
    while(i<=a):
        if i%2==0:
            n=n+i
        i=i+1
        return n
     
print somme_pairs(5)


print "Fonction f(x)=x^3+2.x^2+3.x-4"
def f(x) :
    f=x**3+2*x**2+3*x-4
    return f

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,100)
plt.plot(x,f(x))  # on utilise la fonction sinus de Numpy
plt.ylabel('fonction f(x)=x^3+2.x^2+3.x-4')
plt.xlabel("l'axe des abcisses")
plt.show()

print "Fonction f(x)=x^3+2.x^2+3.x-6"
def g(x) :
    f=x**3+2*x**2+3*x-6
    return f

print "Dichotomie"

def dichotomie(f,p):
    a=-10
    i=1
    b=10
    while (b-a)>p :
        if f(a)*f((a+b)/2)<=0:
            a, b=a, (a+b)/2.
        else:
            a, b=(a+b)/2., b
        i=i+1
        e=b-a
    return "Resultat {} (Erreur:{})".format(a, e)
      
print dichotomie(f,10**(-4))
print dichotomie(f,10**(-6))
print dichotomie(g,10**(-6))

