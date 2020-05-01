# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 15:02:38 2017

@author: dorian
"""

#######################PARTIE A CONSERVER######################################

import matplotlib.pyplot as plt

def trace_coord(coord):
    plt.figure()
    plt.axis('equal')
    for i in range(len(coord)):
        x,y=coord[i][0],coord[i][1]
        plt.scatter(x,y,marker='x')


###############################################################################

print 'Question 1'
fichier1=open('liste_coordonnees.csv','r')
contenu=fichier1.read()
fichier1.close()

print contenu

print 'Question 2'

liste=contenu.split('\n')

print liste[0]

print liste[124]

print 'Question 3'

coord=[]

for element in liste:
    data=element.split(';')
    coord.append([float(data[0]),float(data[1])])

print coord[0]

print coord[145][0]

print 'Question 4'

trace_coord(coord)

print 'Tracé du cercle seul'

coord2=[]
for i in range(len(coord)):
    x,y=coord[i][0],coord[i][1]
    if x<120 and y>x*0.5-110: # ou bien if x**2+y**2<111.**2:
        coord2.append(coord[i])

trace_coord(coord2)

"""
theta = np.linspace(0, 2*np.pi, 200)
x_cercle = 100*np.cos(theta)
y_cercle = 100*np.sin(theta)
plt.plot(x_cercle, y_cercle)
"""

print 'Tracé des points à l\'intérieur du cercle de rayon 100 centré sur (0,0)'

coord3=[]
for i in range(len(coord)):
    x,y=coord[i][0],coord[i][1]
    if x**2+y**2<100.**2:
        coord3.append(coord[i])

trace_coord(coord3)

count=0
count_int=0
count_ext=0

coord4=[]
for i in range(len(coord)):
    count+=1
    x,y=coord[i][0],coord[i][1]
    if x**2+y**2<100.**2:
        count_int+=1
        coord4.append(coord[i])
    if x**2+y**2>100.**2:
        count_ext+=1

"""
theta = np.linspace(0, 2*np.pi, 200)
x_cercle = 100*np.cos(theta)
y_cercle = 100*np.sin(theta)
plt.plot(x_cercle, y_cercle)
"""

print 'Nombre de points total, à l\'intérieur et à l\'extérieur du cercle de rayon 100 centré sur (0,0)'

print count, count_int, count_ext