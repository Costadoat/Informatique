# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:20:35 2015

@author: Renaud
"""

import numpy as np
import matplotlib.pyplot as plt

print "EXERCICE 1:"
      
def permutation(A,i,j):
    t = A[i]
    A[i] = A[j]
    A[j] = t
    
def transvection(A,i,j,x):
    # si vecteur
    if type(A[0]) != list:
        A[i] = A[i] + x*A[j]
    else:
        n = len(A[0])
        for k in range(n):
            A[i][k] = A[i][k] + x*A[j][k]
    
def recherche_pivot(A, j0):
    n = len(A) 
    imax = j0 
    for i in range(j0+1, n):
        if abs(A[i][j0]) > abs(A[imax][j0]):
            imax = i
    return imax

def triangle(A,b):
    n =len(b)
    x = [0 for i in range(n)]
    x[-1] = b[-1]/A[-1][-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/ A[i][i]
    return x
    
def resolution_systeme(A,b):
    n = len(A)

    for i in range(n-1):
        i0 = recherche_pivot(A,i)
        permutation(A,i,i0)
        permutation(b,i,i0) 
        
        for k in range(i+1,n):
            x = A[k][i]/A[i][i]
            transvection(A,k,i,-x)
            transvection(b,k,i,-x) 
    return triangle(A,b)

print "Question 1:"

E=5.
R1,R2,R3,R4,R5,R6=100,220,220,100,100,100

A = [
[R1,R2,0.,0.,0.],
[0.,R2,-R3,-R4,0.],
[0.,0.,0.,R4,-R5-R6],
[1.,-1.,-1.,0.,0.],
[0.,0.,1.,-1.,-1.]  ]

Y = [E,0.,0.,0.,0.]

print 'Matrice A:',A
print 'Vecteur Y:',Y

print "Question 2:"

print 'Resolution avec Pivot',resolution_systeme(A,Y)

x = np.linalg.solve(A,Y)
print 'Resolution avec numpy.linalg.solve',x

#print "\n EXERCICE 2:"
#
##Données
#h=0.04
#L=0.044
#R=0.015
#d=0.01
#
##Question 3
#
##Définition de l'équation non linéaire
#def f(theta,beta):
#    return (d*np.cos(theta)+R*np.cos(beta))**2+(d*np.sin(theta)-h+R*np.sin(beta))**2-L**2
#
##Question 4
#
##Définition de la dérivée
#def df(theta,beta):
#    return -2*d*(d*np.cos(theta)+R*np.cos(beta))*np.sin(theta)+2*d*(d*np.sin(theta)-h+R*np.sin(beta))*np.cos(theta)
#
##Question 5
#
## Recherche de solution par la méthode de Newton
#def resolution(f,df,theta0,epsilon,beta):
#    theta=theta0 # Initialisation à la première estimation fournie
#    #Tant que le critère de convergence n   'est pas satisfait
#    while (abs(f(theta,beta))>epsilon):
#        theta=theta-f(theta,beta)/df(theta,beta)
#    return theta #On renvoie la dernière estimation
#
##Question 6
#t=[]
#beta=[]
#for i in range(10): #Boucle sur les angles Beta
#    t.append(2*i/9.)
#    beta.append((0.3+0.5)*i/9.-0.5)
#
#print 't,beta: ',t,beta
#
#plt.plot(t,beta,"b")
#plt.show()
#
##Question 7
#theta=[]
#for i in range(10): #Boucle sur les angles Beta
#    #Calcul de theta
#    theta.append(resolution(f,df,0,1e-12,beta[i]))
#
#print beta,theta
#
##Question 8
#
#plt.plot(beta,theta,"b")
#plt.show()
#
##Question 9
#omega=[]
#for i in range(9): #Boucle sur les angles Beta
#    #Calcul de theta
#    o=(theta[i+1]-theta[i])/(t[i+1]-t[i])
#    print o
#    omega.append(o)
#    
#
#print omega,t[0:9]
#plt.plot(t[0:9],omega,"b")
#plt.plot(t,theta,"r")
#plt.show()
#
#pince1=np.array([[0,10,20,40,50],[0,0,-5,0,10]])
#pince2=np.array([[-10,0,10,40,50],[0,0,0,-5,-15]])
#
#plt.plot([-15,5,5,-15],[-10,-10,50,50],"m") #Tracé du bâti
#
#for i in range(10): #Boucle sur les angles Beta
#    #Calcul des matrices de rotation
#    Rt=np.array([[np.cos(theta[i]),-np.sin(theta[i])],[np.sin(theta[i]),np.cos(theta[i])]])
#    Rb=np.array([[np.cos(beta[i]),-np.sin(beta[i])],[np.sin(beta[i]),np.cos(beta[i])]])
#    #Rotation des pinces
#    pince1r=np.dot(Rb,pince1)
#    pince2r=np.dot(Rt,pince2)
#    #Tracé des pinces après rotation (en bleu)
#    plt.plot(pince1r[0,:],pince1r[1,:],"b")
#    plt.plot(pince2r[0,:],pince2r[1,:]+h,"b")
#    #Tracé de la bielle (en rouge)
#    plt.plot([pince1r[0,1],pince2r[0,0]],[pince1r[1,1],pince2r[1,0]+h],"-or")
# 
#plt.plot(0,0,"o") #Tracés de deux cercles aux articulations
#plt.plot(0,h,"o")
#plt.show()