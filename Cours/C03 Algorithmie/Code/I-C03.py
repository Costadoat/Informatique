# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:16:48 2015

@author: Renaud
"""

def moyenne(a,b):
    m=(b+a)/2.
    return m

print(moyenne(40,2))

import math


a=3.
b=4.
n=10

for i in range(1,n) :
    m=(b+a)/2.
    if math.sin(m) > 0:
        a=m
    else:
        b=m
    i = i+1
print("Pi=%.48f" % (m))

while math.sin(m) > 10**-10 or math.sin(m) < -10**-10:
    m=(b+a)/2.
    if math.sin(m) > 0:
        a=m
    else:
        b=m
    i = i+1
print("Pi=%.48f" % (m))

p=math.pi
if (p > a and p < b) or (p < a and p > b):
    print("Faire le calcul")
else:
    print("Attention, il n'est pas possible de trouver pi entre %s et %s" % (a,b))
