# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:21:43 2018

@author: costa
"""

import numpy as np
import copy

Atest = [[2.,2.,-3.,4.], [-2.,-1.,-3.,2.], [6.,4.,4.,5.] , [1.,5.,3.,2.]]
btest = [2.,-5.,16.,11.]
Atestnp = np.array([[2.,2.,-3.,4.], [-2.,-1.,-3.,2.], [6.,4.,4.,5.] , [1.,5.,3.,2.]])
btestnp = np.array([2.,-5.,16.,11.])
coefficients=np.array([4.,4.,4.,4.,4.])


Notes=[]
def test_solution(code,sol):
    try:
    # Bloc à essayer
        x=eval(code)
        if x != sol:
            print "La commande %s a renvoyé la valeur %s alors qu'elle aurait du envoyer la valeur %s." % (code,x,sol)
    except:
    # Bloc qui sera exécuté en cas d'erreur
        print erreur #Génère une erreur pour afficher le message
    
def test_question1():
    try:
        test_solution('recherche_pivot(Atest, 0)',2)
        test_solution('recherche_pivot(Atest, 1)',3)
        test_solution('recherche_pivot(Atest, 2)',2)
        test_solution('recherche_pivot(Atest, 3)',3)
        test_solution('recherche_pivot(Atestnp, 0)',2)
        test_solution('recherche_pivot(Atestnp, 1)',3)
        test_solution('recherche_pivot(Atestnp, 2)',2)
        test_solution('recherche_pivot(Atestnp, 3)',3)
        note[0]=1
    except:
        print "La commande recherche_pivot a renvoyé une erreur."
        note[0]=0
    print 'Question 1:',note[0],'\r'
    
def permutation_cor(A,i,j):
    t = A[i]
    A[i] = A[j]
    A[j] = t

def permutationnp_cor(A,i,j):
    t = A[i].copy()
    A[i] = A[j]
    A[j] = t


def test_question2():
    try:
        B11=copy.deepcopy(Atestnp)
        B21=copy.deepcopy(Atestnp)
        permutationnp_cor(B11,0,1)
        permutation(B21,0,1)
        B12=copy.deepcopy(Atestnp)
        B22=copy.deepcopy(Atestnp)
        permutationnp_cor(B12,0,2)
        permutation(B22,0,1)
        B13=copy.deepcopy(Atestnp)
        B23=copy.deepcopy(Atestnp)
        permutationnp_cor(B13,0,3)
        permutation(B23,0,3)
        if B11==B21.all() and B12==B22.all() and B13==B23.all():
            note[1]=1
    except:
        try:
            B11=Atest[:]
            B21=Atest[:]
            permutation_cor(B11,0,1)
            permutation(B21,0,1)
            B12=Atest[:]
            B22=Atest[:]
            permutation_cor(B12,0,2)
            permutation(B22,0,2)
            B13=Atest[:]
            B23=Atest[:]
            permutation_cor(B13,0,3)
            permutation(B23,0,3)
            if B11==B21 and B12==B22 and B13==B23:
                note[1]=1
        except:
            print 'Le script de permutation ne fonctionne ni pour numpy ni en normal.'
            note[1]=0
    print 'Question 2:',note[1],'\r'

def transvection_cor(A,i,j,x):
    # si vecteur
    if type(A[0]) != list:
        A[i] = A[i] + x*A[j]
    else:
        n = len(A[0])
        for k in range(n):
            A[i][k] = A[i][k] + x*A[j][k]

def transvectionnp_cor(A,i,j,x):
    A[i] = A[i] + x*A[j]

def test_question3():
    try:
        B11=copy.deepcopy(Atestnp)
        B21=copy.deepcopy(Atestnp)
        transvectionnp_cor(B11,1,0,-1)
        transvection(B21,1,0,-1)
        B12=copy.deepcopy(Atestnp)
        B22=copy.deepcopy(Atestnp)
        transvectionnp_cor(B12,2,0,-0.5)
        transvection(B22,2,0,-0.5)
        B13=copy.deepcopy(Atestnp)
        B23=copy.deepcopy(Atestnp)
        transvectionnp_cor(B13,3,0,1)
        transvection(B23,3,0,1)
        B14=copy.deepcopy(btestnp)
        B24=copy.deepcopy(btestnp)
        transvectionnp_cor(B14,1,0,-1)
        transvection(B24,1,0,-1)
        B15=copy.deepcopy(btestnp)
        B25=copy.deepcopy(btestnp)
        transvectionnp_cor(B15,2,0,-0.5)
        transvection(B25,2,0,-0.5)
        if (B11==B21).all() and (B12==B22).all() and (B13==B23).all() and (B14==B24).all() and (B15==B25).all():
            note[2]=1
        else:
            print erreur #Génère une erreur pour tenter le calcul sans numpy
    except:
        try:
            B11=Atest[:]
            B21=Atest[:]
            transvection_cor(B11,0,1)
            transvection(B21,0,1)
            B12=Atest[:]
            B22=Atest[:]
            transvection_cor(B12,0,2)
            transvection(B22,0,2)
            B13=Atest[:]
            B23=Atest[:]
            transvection_cor(B13,0,3)
            transvection(B23,0,3)
            if B11==B21 and B12==B22 and B13==B23:
                note[2]=1
            else:
                print erreur #Génère une erreur pour afficher le message
        except:
            print 'Le script de transvection ne fonctionne ni pour numpy ni en normal.'
            note[2]=0
    print 'Question 3:',note[2],'\r'

def triangle_cor(A,b):
    n =len(b)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/ A[i][i]
    return x

def triangle_cor(A,b):
    n =len(b)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/ A[i][i]
    return x

def test_question4():
    try:
        if triangle_cor(Atestnp,btestnp)==triangle(Atest,btest):
            note[3]=1
        else:
            print erreur #Génère une erreur pour afficher le message
    except:
        print 'Le script de triangularisation ne fonctionne ni pour numpy ni en normal.'
        note[3]=0
    print 'Question 4:',note[3],'\r'

def test_question5():
    try:
        t1=resolution_systeme(Atest,btest)[0]>0.642 and resolution_systeme(Atest,btest)[0]<0.643
        t2=resolution_systeme(Atest,btest)[1]>1.108 and resolution_systeme(Atest,btest)[1]<1.109
        t3=resolution_systeme(Atest,btest)[2]>1.237 and resolution_systeme(Atest,btest)[2]<1.238
        t4=resolution_systeme(Atest,btest)[3]>0.552 and resolution_systeme(Atest,btest)[3]<0.553
        if t1 and t2 and t3 and t4:
            note[4]=1
        else:
            print erreur #Génère une erreur pour afficher le message
    except:
        print 'Le script de résolution globale ne fonctionne pas.'
        note[4]=0
    print 'Question 5:',note[4],'\r'
    
import os
import os.path

ilots=os.listdir('Code')
if len(ilots)!=0:
    for ilot in ilots:
        if ilot[-2:]=='py':
            print '\n##############################'
            print '\r'+ilot[:-3]
            note=np.zeros(5)
            try:
                execfile("Code/"+ilot[:])
                test_question1()
                test_question2()
                test_question3()
                test_question4()
                test_question5()
            except:
                print "La compilation du fichier %s a généré une erreur." % (ilot[:])
            notefinale=np.sum(note*coefficients)
            print 'Note:',notefinale
            Notes.append([ilot[:-3],note*coefficients,notefinale])
        print '\n##############################'
        print '\rRésultats'

for note in Notes:
    print note[0],";",note[1][0],";",note[1][1],";",note[1][2],";",note[1][3],";",note[1][4],";",note[2]