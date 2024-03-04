import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import copy

# Question1
parchemin1 = img.imread('parchemin1.png')
parchemin2 = img.imread('parchemin2.png')
parchemin3 = img.imread('parchemin3.png')

plt.imshow(parchemin1)
plt.show()

# Question2
parchemin=parchemin1+parchemin2+parchemin3

taille=np.shape(parchemin)

for i in range(taille[0]):
    for j in range(taille[1]):
        for k in range(taille[2]):
            if parchemin[i,j,k]>1:
                parchemin[i,j,k]=1

plt.imshow(parchemin)
plt.show()

# Question 3

def dmstodd(coord,dir):
    if dir=='W' or dir=='S':
        signe=-1
    else:
        signe=1
    return signe*(coord[0]+coord[1]/60+coord[2]/3600)
    
print(dmstodd([20,37,42],'N'))
#20 37 42N
y=dmstodd([20,37,42],'N')

# Question 4
#70 52 15W
x1=dmstodd([70,52,15],'W')

#enlever 2°20'13,82"
x2=dmstodd([70-2,52-20,15-13.82],'W')

def distance(stationA,stationB):
    rayon_terre=6361
    phi1=stationA[0]*np.pi/180
    phi2=stationB[0]*np.pi/180
    deltalambda=(stationB[1]-stationA[1])*np.pi/180
    return np.arccos(np.sin(phi1)*np.sin(phi2)+np.cos(phi1)*np.cos(phi2)*np.cos(deltalambda))*rayon_terre

print("Il leur a fallu parcourir {:.2f} km.".format(distance([x1,y],[x2,y])))

# Question 5

diamants = img.imread('tresor.png')
taille=np.shape(diamants)
plt.imshow(diamants)
plt.show()

image_couleurs=np.ones(taille)-diamants
image_couleurs[:,:,3]=1
plt.imshow(image_couleurs)
plt.show()

#3 rouges rubis
#8 bleus  saphirs
#12 verts emeraudes

# Question 5

def norme(vec):
    s=0
    for i in range(len(vec)):
        s+=vec[i]**2
    return np.sqrt(s)

print(norme([1,2,3]))

# Question 6

seuil=0.8

red=[1,0,0,1]
green=[0,1,0,1]
blue=[0,0,1,1]

img_coul=[]
for i in range(3):
    img_coul.append(image_couleurs.copy())

for idx,couleur in enumerate([red,green,blue]):
    for i in range(taille[0]):
        for j in range(taille[1]):
                if norme(img_coul[idx][i,j]-couleur)>seuil:
                    img_coul[idx][i,j]=[1,1,1,1]
                    
f, axarr = plt.subplots(1,3)
for i in range(3):
    axarr[i].imshow(img_coul[i])
plt.show()

# Question 7

def convert_nb(image):
    image_out=np.zeros(np.shape(image))
    image_out[:,:,3]=1
    coefficients=[0.2125,0.7154,0.0721]
    for j in range(3):
        for i in range(3):
            image_out[:,:,j]+=image[:,:,i]*coefficients[i]
    return image_out

image_nb=convert_nb(image_couleurs)
plt.imshow(image_nb)
plt.show()

# Question 8

def contour(image_nb):
    normel=[]
    nb_lig,nb_col,nb_coul=image_nb.shape
    image_out=np.zeros((nb_lig,nb_col,nb_coul))
    for i in range(2,nb_lig-2):
        for j in range(2,nb_col-2):
            p1=image_nb[i-2,j,0]
            p2=image_nb[i,j-2,0]
            p3=image_nb[i+2,j,0]
            p4=image_nb[i,j+2,0]
            norme=np.sqrt((p1-p3)**2+(p2-p4)**2)/2
            normel.append(norme)
            seuil=0.1
            if norme < seuil:
                p = 1
            else:
                p = 0
            for k in range(nb_coul-1):
                image_out[i,j,k]=p
            image_out[i,j,3]=1
    return image_out

contours=contour(image_nb)
f, axarr = plt.subplots(1,3)
axarr[0].imshow(image_couleurs)
axarr[0].title.set_text('Image originale')
axarr[1].imshow(image_nb)
axarr[1].title.set_text('NB')
axarr[2].imshow(contours)
axarr[2].title.set_text('Contour')
plt.show()

