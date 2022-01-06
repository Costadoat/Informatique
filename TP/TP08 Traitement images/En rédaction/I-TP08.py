import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

## Ouverture d'une image

image = img.imread('David_Hockney_Portrait_of_an_Artist.png')
plt.imshow(image)
plt.show()

print(image.shape)

## Extraction d'une couleur

def extraire_couleur(image,id_couleur):
    image_out=image.copy()
    for i in range(3):
        if i!=id_couleur:
            image_out[:,:,i]=0
    return image_out

f, axarr = plt.subplots(1,3)
for i in range(3):
    axarr[i].imshow(extraire_couleur(image,i))
plt.show()

## Inversion des couleur

def inverser_couleur(image):
    image_out=image.copy()
    image_out[:,:,3]=0
    return np.ones(np.shape(image_out))-image_out

f, axarr = plt.subplots(1,2)
axarr[0].imshow(image)
axarr[1].imshow(inverser_couleur(image))
plt.show()

## Conversion en niveaux de gris

def convert_nb_base(image):
    image_out=np.zeros(np.shape(image))
    image_out[:,:,3]=1
    for j in range(3):
        for i in range(3):
            image_out[:,:,j]+=image[:,:,i]/3
    return image_out

def convert_nb_evol(image):
    image_out=np.zeros(np.shape(image))
    image_out[:,:,3]=1
    coefficients=[0.2125,0.7154,0.0721]
    for j in range(3):
        for i in range(3):
            image_out[:,:,j]+=image[:,:,i]*coefficients[i]
    return image_out

f, axarr = plt.subplots(1,2)
axarr[0].imshow(convert_nb_base(image))
axarr[1].imshow(convert_nb_evol(image))
plt.show()

## Contraste et luminosité

def contraste_luminosite(image,contraste,luminosite):
    return np.clip(contraste*image+luminosite,0,1)

f, axarr = plt.subplots(1,2)
axarr[0].imshow(image)
axarr[1].imshow(contraste_luminosite(image,2,-0.5))
plt.show()

## Rotation de pi/2

def rotation(image):
    nb_lig,nb_col,nb_coul=image.shape
    image2=np.zeros((nb_col,nb_lig,nb_coul))
    for i in range(nb_lig):
        for j in range(nb_col):
            for k in range(nb_coul):
                image2[j,i,k]=image[i,nb_col-1-j,k]
    return image2

def rotation(image):
    return np.rot90(image)

image_rot=image.copy()
f, axarr = plt.subplots(1,4, gridspec_kw={'width_ratios': [3/2, 1,3/2, 1]})
for i in range(4):
    axarr[i].imshow(image_rot)
    axarr[i].title.set_text('Rotation {}°'.format(i*90))
    image_rot=rotation(image_rot)
plt.show()

## Réduction de la taille d'une image

def reduire(image, facteur):
    nb_lig,nb_col,nb_coul=image.shape
    image2=np.zeros((nb_lig//facteur,nb_col//facteur,nb_coul))
    for i in range(nb_lig//facteur):
        for j in range(nb_col//facteur):
            for k in range(nb_coul):
                image2[i,j,k]=image[i*facteur,j*facteur,k]
    return image2

plt.imshow(reduire(image,5))
plt.show()

## Agrandir la taille d'une image

def agrandir(image, facteur):
    nb_lig,nb_col,nb_coul=image.shape
    image2=np.zeros((facteur*nb_lig,facteur*nb_col,nb_coul))
    for i in range(facteur*nb_lig):
        for j in range(facteur*nb_col):
            for k in range(nb_coul):
                image2[i,j,k]=image[i//facteur,j//facteur,k]
    return image2

plt.imshow(agrandir(image,2))
plt.show()

def contour(matB):
    normel=[]
    nb_lig,nb_col,nb_coul=matB.shape
    matC=np.zeros((nb_lig,nb_col,nb_coul))
    for i in range(2,nb_lig-2):
        for j in range(2,nb_col-2):
            p1=matB[i-2,j,0]
            p2=matB[i,j-2,0]            
            p3=matB[i+2,j,0]            
            p4=matB[i,j+2,0]
            norme=np.sqrt((p1-p3)**2+(p2-p4)**2)/2
            normel.append(norme)
            seuil=0.15
            if norme < seuil:
                p = 1
            else:
                p = 0               
            for k in range(nb_coul-1):
                matC[i,j,k]=p
            matC[i,j,3]=1
    print(max(normel),min(normel))
    return matC

image=reduire(image,3)
C=convert_nb_evol(image)
D=contour(C)


f, axarr = plt.subplots(1,3)
axarr[0].imshow(image)
axarr[0].title.set_text('Image originale')
axarr[1].imshow(C)
axarr[1].title.set_text('NB')
axarr[2].imshow(D)
axarr[2].title.set_text('Contour')
plt.show()
