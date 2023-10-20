# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 17:03:06 2015

@author: Renaud
"""

import time
import winsound

a=100
for i in range(1,a):
    time.sleep(1) #attente d'une seconde
    h=(a-i)/3600
    m=((a-i)%3600)/60
    s=((a-i)%3600)%60
    print '%s:%s:%s' % (h,m,s)
    if s == 0 and m!=0 and h!=0:
        winsound.Beep(2500,500)
    if s < 10:
        winsound.Beep(2500,500)


for i in range(1,4):
    time.sleep(1)
    for j in range(1,3):
        winsound.Beep(2500,500)
    