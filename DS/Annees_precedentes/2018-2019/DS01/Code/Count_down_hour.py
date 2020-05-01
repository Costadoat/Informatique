# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 17:03:06 2015

@author: Renaud
"""

import time

a=15
for i in range(1,a):
    time.sleep(1) #attente d'une seconde
    i=i+1
    h=(a-i)/3600
    m=((a-i)%3600)/60
    s=((a-i)%3600)%60
    print '%s:%s:%s' % (h,m,s)
