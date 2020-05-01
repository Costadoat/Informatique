# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:37:31 2016

@author: Renaud
"""

import numpy as np
import scipy.optimize as resol

def deplacement(TA,v): #deplacement d'un torseur par un vecteur dans la même base
    TA[3:6]=TA[3:6]+np.cross(v,TA[0:3])
    return TA

L=0.2
l=0.2
x0=0
k=100000
Cm=10

def f(v):
    return v[0]+k*(v[1]-x0),Cm-2*l*np.sin(v[2])*v[0],2*l*np.cos(v[2])+v[1]-L

sol=resol.root(f,[0,0.1,1.32])
print(sol.x)