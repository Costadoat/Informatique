# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:52:38 2013

@author: stephane
"""

from math import sqrt

def est_premier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for k in range(2,1+int(sqrt(n))):
        if n % k ==0 :
            return False
    return True
