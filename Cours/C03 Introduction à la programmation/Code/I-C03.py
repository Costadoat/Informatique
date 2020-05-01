# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:16:07 2015

@author: Renaud
"""

def Euclide_PGCD(a,b):      
      q=a/b
      r=a%b
      print("q=%s" % q)
      print("r=%s" % r)
      while r!=0: # tant que ce reste est non nul :
          a=b # b devient le nouveau a
          b=r # r devient le nouveau b
          q=a/b
          r=a%b # on recalcule le reste
          print("q=%s" % q)
          print("r=%s" % r)
      return(b)
      
print("PGCD=%s" % Euclide_PGCD(5810,1125))


