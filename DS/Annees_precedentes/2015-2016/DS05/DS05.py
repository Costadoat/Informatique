# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:20:35 2015

@author: Renaud
"""

import MySQLdb
import matplotlib.pyplot as plt

#conn = MySQLdb.connect (host = 'www.costadoat.fr',
#                        user = 'dorian',
#                        passwd = 'dorian',
#                        db = 'food')
#cursor = conn.cursor ()
#
#print "Question 2:"
#
#cursor.execute ("SELECT fdgrp_cd,fdgrp_desc,id FROM foodcats")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#
#print "Question 3:"
#
#cursor.execute ("SELECT ndb_no,fdgrp_cd,long_desc,id FROM fooddescs WHERE fdgrp_cd=0900 AND ndb_no<09016")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#        
#print "Question 4:"
#
#cursor.execute ("SELECT nutr_no,units,nutrdesc FROM nutrientdefs WHERE id<7")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#        
#print "Question 5:"
#
#cursor.execute ("SELECT ndb_no,nutr_no,nutr_val FROM nutrientdata WHERE (ndb_no=09003 OR ndb_no=09004) AND nutr_no<210 ")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#        
#print "Question 6:"
#
#cursor.execute ("SELECT ndb_no,fdgrp_cd,long_desc FROM fooddescs WHERE long_desc LIKE 'Apples,%'")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#
#        
#print "Question 7:"
#
#cursor.execute ("SELECT 'Proteine',n.nutr_val,f.long_desc FROM nutrientdata n JOIN fooddescs f ON n.ndb_no=f.ndb_no WHERE n.nutr_no=203 AND f.long_desc LIKE 'Apples,%' ORDER BY n.nutr_val DESC")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#    
#print "Question 8:"
#
#cursor.execute ("SELECT f.long_desc,n.ndb_no,n.nutr_val FROM nutrientdata n JOIN fooddescs f ON n.ndb_no=f.ndb_no WHERE n.nutr_no=203 AND f.long_desc LIKE 'Apples,%' AND n.nutr_val=(SELECT MAX(n.nutr_val) FROM nutrientdata n JOIN fooddescs f ON n.ndb_no=f.ndb_no WHERE n.nutr_no=203 AND f.long_desc LIKE 'Apples,%')")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#        
#print "Question 9:"
#
#cursor.execute ("SELECT 'Apples', AVG(n.nutr_val) FROM nutrientdata n JOIN fooddescs f ON n.ndb_no=f.ndb_no WHERE n.nutr_no=208 AND f.long_desc LIKE 'Apples,%'")
#rows = cursor.fetchall ()
#for row in rows:
#        print row
#        
#cursor.execute ("SELECT 'Peaches', AVG(n.nutr_val) FROM nutrientdata n JOIN fooddescs f ON n.ndb_no=f.ndb_no WHERE n.nutr_no=208 AND f.long_desc LIKE 'Peaches,%'")
#rows = cursor.fetchall ()
#for row in rows:
#        print row
#
#cursor.execute ("SELECT 'Bananas', AVG(n.nutr_val) FROM nutrientdata n JOIN fooddescs f ON n.ndb_no=f.ndb_no WHERE n.nutr_no=208 AND f.long_desc LIKE 'Bananas,%'")
#rows = cursor.fetchall ()
#for row in rows:
#        print row
#        
#print "Question 10:"
#
#cursor.execute ("SELECT COUNT(ndb_no) FROM fooddescs")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#        
#print "Question 11:"
#
#cursor.execute ("SELECT c.fdgrp_desc,COUNT(f.ndb_no) FROM fooddescs f JOIN foodcats c ON f.fdgrp_cd=c.fdgrp_cd GROUP BY f.fdgrp_cd")
#rows = cursor.fetchall ()
#
#for row in rows:
#        print row
#        
#print "Question 12:"
#
#ingredients=[['jambon','07029','30'],['beurre','01001','5'],['pain cereales','18035','80'],['cheddar','01009','20']]
#
#s=0
#
#for ingredient in ingredients:
#    cursor.execute ("SELECT nutr_val FROM nutrientdata WHERE ndb_no={0} AND nutr_no=208 ".format(ingredient[1]))
#    rows = cursor.fetchall ()
#    for row in rows:
#        s=s+float(ingredient[2])*float(row[0])/100.
#
#print ("Valeur energetique croque monsieur: {0} Kcal".format(s))
#
#print "Question 13:"
#
#print "Il lui faudra courir a 12.3km/h ou 12.6km/h"

print "Question 14:"

# il faut initialiser toutes les grandeurs utilisees ensuite dans le code
periode=180 # en secondes
temps=[] 
vitesse=[]
y0=0 
a=0.02 # en m/s²
v0=2.5 # en m/s

for i in range(5):
    for k in range(periode/2):
        temps.append(i*periode+k)
        vitesse.append(v0*3.6) # 3.6 pour conversion m/s --> km/h
    for k in range(periode/2):
        temps.append(i*periode+k+periode/2)
        vitesse.append((v0+a*k)*3.6) # idem

# Question 15
def F(t):
    return vitesse[temps.index(t)]  # on recupere la vitesse qui correspond au temps
                                    # temps.index(t) est utile si t0 est different de 0

# Question 16    
def methode_euler(F,y0,t):
    y = [0]*len(t)
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i]+(t[i+1]-t[i])*F(t[i])/3.6 # conversion de la vitesse 
                                                # km/h --> m/s puisque le temps
                                                # est en secondes
    return y

# Question 17
position=methode_euler(F,y0,temps)  # il faut appeler une fonction si on veut utliser
                                    # ce qu'elle renvoie
print position[-1] #la distance totale parcourue est la dernière distance calculee

# Question 18
plt.plot(temps,vitesse)

# Question 19

plt.plot(temps,position)
plt.show()