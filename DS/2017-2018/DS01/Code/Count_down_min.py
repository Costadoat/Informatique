# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 17:03:06 2015

@author: Renaud
"""

import time

a=100
for i in range(1,a):
    time.sleep(1) #attente d'une seconde
    i=i+1
    m=(a-i)/60
    s=(a-i)%60
    print '%s:%s' % (m,s)
