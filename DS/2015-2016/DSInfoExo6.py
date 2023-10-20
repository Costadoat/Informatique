# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:58:50 2015

@author: willie
"""

import time
#import winsound

a=10

for i in range (1,a):
    time.sleep(1)
    print 'sleep'
    h=(a-i)/3600
    m=((a-i)%3600)/60
    s=((a-i)%3600)%60
    print '%s:%s:%s' % (h,m,s)
    if s==0 and m!=0 and h!=0:
        print 'beep'
    if s < 10:
        print 'beep'

for i in range(1,4):
    time.sleep(1)
    print 'sleep'
    for j in range(1,3):
        print 'beep'