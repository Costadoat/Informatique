import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

## Question 1 : Ouvrir l'image et donner sa dimension
img = img.imread("mona_lisa.png")
print(img.shape)

## Question 2 : Afficher l'image
plt.imshow(img)
plt.axis('off')
plt.show()

## Question 3 : Modifier le contraste et la luminosité
def contraste_luminosite(image,contraste,luminosite):
    return np.clip(contraste*image+luminosite,0,1)

f, axarr = plt.subplots(1,2)
axarr[0].imshow(img)
axarr[0].set_title("Image originale")
axarr[0].axis('off')

axarr[1].imshow(contraste_luminosite(img,2,-0.5))
axarr[1].set_title("Nouvelle image")
axarr[1].axis('off')
plt.show()

# Question 4: Charger le masque CSV
fichier = open("masque_mona_lisa.csv", 'r')
contenu = fichier.read()
fichier.close()
lignes = contenu.split("\n")
mask=[]

for ligne in lignes[:-1]:
    data=[int(i) for i in ligne.split(',')]
    mask.append(data)
mask=np.array(mask)

print(mask[40])


# Question 5: Fonction flou récursif
def moyenne_voisins(img,i,j):
    pixel = 0
    for k in range(-1,2):
        for l in range(-1,2):
            pixel += (1/9)*img[i+k,j+l]
    return pixel

print(moyenne_voisins(img,75,11))
                        
def flou(img, n):
    img_blur = img.copy()
    h, w = img.shape[:2]
    for iter in range(n):
        for i in range(1,h-1):
            for j in range(1,w-1):
                if mask[i,j]==0:
                    img_blur[i,j] = moyenne_voisins(img,i,j)
    return img_blur
    
def flou_recursif(img, n):
    if n == 0:
        return img
    else:
        h, w = img.shape[:2]
        img_blur = img.copy()
        for i in range(1,h-1):
            for j in range(1,w-1):
                if mask[i,j]==0:
                    img_blur[i,j] = moyenne_voisins(img,i,j)
        return flou_recursif(img_blur, n-1)

# Question 6: Appliquer le flou récursif uniquement sur l'arrière-plan et afficher l'image
fig, axes = plt.subplots(1, 2)
axes[0].imshow(img)
axes[0].set_title("Image originale")
axes[0].axis('off')
axes[1].imshow(flou_recursif(img, n=2))
axes[1].set_title("Arrière-plan flou")
axes[1].axis('off')
plt.show()
