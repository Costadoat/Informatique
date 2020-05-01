# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:24:55 2018

@author: Renaud
"""

from math import asin, pi, cos, sin
from PIL import Image, ImageDraw, ImageFont


def detectcarre(pix):
    i,j=0,0
    toto=0
    contour=1
    while ((pix[i,j]==(255,255,255) or pix[i,j]==(255,0,0)) and i<size[0] and j<size[1] ):
        pix[i,j]=(255,0,0)
        if (j==0 and contour==1):
            i+=1
            contour=0
            toto=1
        elif (i==0 and contour==1):
            j+=1
            toto=2
            contour=0
        elif toto==1 and i!=0:
            j+=1
            i+=-1
            contour=1
        else:
            j+=-1
            i+=1
            contour=1
    hg=[i,j]
    pix[i,j]=(0,255,0)
    i,j=size[0]-1,0
    toto=0
    contour=1
    while ((pix[i,j]==(255,255,255) or pix[i,j]==(255,0,0)) and i>=0 and i<size[0] and j>=0 and j<size[1]):
        pix[i,j]=(255,0,0)
        if (j==0 and contour==1):
            i+=-1
            contour=0
            toto=1
        elif (i==size[0]-1 and contour==1):
            j+=1
            toto=2
            contour=0
        elif toto==1 and i!=size[0]-1:
            j+=1
            i+=1
            contour=1
        else:
            j+=-1
            i+=-1
            contour=1
    hd=[i,j]
    i,j=0,size[1]-1
    toto=0
    contour=1
    while ((pix[i,j]==(255,255,255) or pix[i,j]==(255,0,0)) and i>=0 and i<size[0] and j>=0 and j<size[1]):
        pix[i,j]=(255,0,0)
        if (j==size[1]-1 and contour==1):
            i+=1
            contour=0
            toto=1
        elif (i==0 and contour==1):
            j+=-1
            toto=2
            contour=0
        elif toto==1 and i!=0:
            j+=-1
            i+=-1
            contour=1
        else:
            j+=1
            i+=1
            contour=1
    bg=[i,j]
    i,j=size[0]-1,size[1]-1
    toto=0
    contour=1
    while ((pix[i,j]==(255,255,255) or pix[i,j]==(255,0,0)) and i>=0 and i<size[0] and j>=0 and j<size[1]):
        pix[i,j]=(255,0,0)
        if (j==size[1]-1 and contour==1):
            i+=-1
            contour=0
            toto=1
        elif (i==size[0]-1 and contour==1):
            j+=-1
            toto=2
            contour=0
        elif toto==1 and i!=0:
            j+=-1
            i+=1
            contour=1
        else:
            j+=1
            i+=-1
            contour=1
    bd=[i,j]
    return hg,hd,bg,bd

def taille(hg,hd,bg,bd):
    largeur=0
    longueur=0
    return largeur,longueur

def orientation(hg,hd,bg,bd):
    angle=0
    return angle


for image in range(8):
    im = Image.open(str(image)+'.jpg')
    pix = im.load()
    size=im.size
    hg,hd,bg,bd=detectcarre(pix)
    print hg,hd,bg,bd
    print taille(hg,hd,bg,bd)
    print orientation(hg,hd,bg,bd)
    im.save('Copie '+str(image)+'.jpg')