#Question 1:

def fibonacci(n):

    # valeurs 1 et 0
    if n == 0:
        return [n]        

    elif n == 1:
        return [0,1]

    else:
        f1, f2, f3 = 0, 1, 1
        fibo=[f1,f2,f3]
        while f2+f3 <=n:
            f1 = f2
            f2 = f3
            f3 = f1 + f2
            fibo.append(f3) #il faut ajouter cette ligne
        return fibo

print(fibonacci(10))

#Question 2:
 
def decomposition_fibo(n):
    resultat=[]
    valeurs=fibonacci(n)
    i=len(valeurs)-1
    while n>0:
        if n>=valeurs[i]:
            resultat.append(valeurs[i])
            n = n-valeurs[i]
            i-=1
        i-=1
    return resultat

print(decomposition_fibo(14))

#Question 3:

for n in range(23):
    print(n,decomposition_fibo(n))

#Question 4:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

M,N=6,5
Z=[[0 for i in range(M)] for i in range(N)]
Z[1][2]=1
Z[2][2]=1
Z[3][2]=1

def calcul_nb_voisins(Z):
    lx,ly = len(Z[0]), len(Z)
    v = [[0] * lx for i in range(ly)]
    for x in range(lx):
        for y in range(ly):
            v[y%ly][x%lx] = Z[(y-1)%ly][(x-1)%lx]+Z[(y-1)%ly][x%lx] \
            +Z[(y-1)%ly][(x+1)%lx] + Z[y%ly][(x-1)%lx] + 0 \
            +Z[y%ly][(x+1)%lx] + Z[(y+1)%ly][(x-1)%lx]\
            +Z[(y+1)%ly][x%lx]+Z[(y+1)%ly][(x+1)%lx]
    return v

print(calcul_nb_voisins(Z))

#Question 5:

def update(frameNum, img, Z):
    lx,ly = len(Z[0]), len(Z)
    N = calcul_nb_voisins(Z)
    for x in range(lx):
        for y in range(ly):
            if Z[y][x] == 1 and (N[y][x] < 2 or N[y][x] > 3):
                Z[y][x] = 0
            elif Z[y][x] == 0 and N[y][x] == 3:
                Z[y][x] = 1
    img.set_data(Z)
    return img,

fig, ax = plt.subplots()
img = ax.imshow(Z, interpolation='nearest')
ani = FuncAnimation(fig, update, fargs=(img, Z), frames=2, interval=1, save_count=1)

plt.show()


#Question 6:

# Planeur

M,N=6,5
Z=[[0 for i in range(M)] for i in range(N)]
Z[2][1]=1
Z[3][2]=1
Z[1][3]=1
Z[2][3]=1
Z[3][3]=1

fig, ax = plt.subplots()
img = ax.imshow(Z, interpolation='nearest')
plt.show()

# Planeur

M,N=70,50
Z=[[0 for i in range(M)] for i in range(N)]
Z[2][1]=1
Z[3][2]=1
Z[1][3]=1
Z[2][3]=1
Z[3][3]=1

fig, ax = plt.subplots()
img = ax.imshow(Z, interpolation='nearest')
ani = FuncAnimation(fig, update, fargs=(img, Z), frames=2, interval=1, save_count=1)

plt.show()


# Le canon à planeurs de Gosper, créé par Bill Gosper, qui émet des planeurs.

#------------------------------------------------------------------------------------------------------------------
##M,N=200,100
##Z=[[0 for i in range(N)] for i in range(N)]
##
##Z[6][2]=1
##Z[7][2]=1
##Z[6][3]=1
##Z[7][3]=1
##Z[6][12]=1
##Z[7][12]=1
##Z[8][12]=1
##Z[5][13]=1
##Z[9][13]=1
##Z[4][14]=1
##Z[10][14]=1
##Z[4][15]=1
##Z[10][15]=1
##Z[7][16]=1
##Z[5][17]=1
##Z[9][17]=1
##Z[6][18]=1
##Z[7][18]=1
##Z[8][18]=1
##Z[7][19]=1
##Z[4][22]=1
##Z[5][22]=1
##Z[6][22]=1
##Z[4][23]=1
##Z[5][23]=1
##Z[6][23]=1
##Z[3][24]=1
##Z[7][24]=1
##Z[2][26]=1
##Z[3][26]=1
##Z[7][26]=1
##Z[8][26]=1
##Z[4][36]=1
##Z[5][36]=1
##Z[4][37]=1
##Z[5][37]=1
##
##data=''
##for y in range(len(Z)):
##    data+=';'.join([str(el) for el in Z[y]])+'\n'
##file=open('gosper_canon.csv','w')
##file.write(data)
##file.close()
###------------------------------------------------------------------------------------------------------------------     

#Question 7:

file=open('gosper_canon.csv','r')
contenu=file.read()
lignes=contenu.split('\n')
Z=[]
for ligne in lignes[:-1]:
    cells=ligne.split(';')
    data=[]
    for cell in cells:
        data.append(int(cell))
    Z.append(data)

fig, ax = plt.subplots()
img = ax.imshow(Z, interpolation='nearest')
ani = FuncAnimation(fig, update, fargs=(img, Z), frames=2, interval=1, save_count=1)

plt.show()

#Question 8:

def calcul_nb_voisins(Z):
    lx,ly = len(Z[0]), len(Z)
    v = [[0] * lx for i in range(ly)]
    for x in range(lx-1):
        for y in range(ly-1):
            v[y%ly][x%lx] = Z[(y-1)%ly][(x-1)%lx]+Z[(y-1)%ly][x%lx] \
            +Z[(y-1)%ly][(x+1)%lx] + Z[y%ly][(x-1)%lx] + 0 \
            +Z[y%ly][(x+1)%lx] + Z[(y+1)%ly][(x-1)%lx]\
            +Z[(y+1)%ly][x%lx]+Z[(y+1)%ly][(x+1)%lx]
    return v

file=open('gosper_canon.csv','r')
contenu=file.read()
lignes=contenu.split('\n')
Z=[]
for ligne in lignes[:-1]:
    cells=ligne.split(';')
    data=[]
    for cell in cells:
        data.append(int(cell))
    Z.append(data)

fig, ax = plt.subplots()
img = ax.imshow(Z, interpolation='nearest')
ani = FuncAnimation(fig, update, fargs=(img, Z), frames=2, interval=1, save_count=1)

plt.show()



