# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:24:55 2018

@author: Renaud
"""

from math import asin, pi, cos, sin
from PIL import Image, ImageDraw, ImageFont

def detect_carre(pix):
    hgv,bdv,hdv,bgv=size[0]+1,0,0,size[1]+1
    for i in range(size[0]):
            for j in range(size[1]):
                moyenne=pix[i,j][0]+pix[i,j][1]+pix[i,j][2]
                if moyenne < 500:
                    if i+j<hgv:
                        hgv=i+j
                        hg=i,j
                    if i+j>bdv:
                        bdv=i+j
                        bd=i,j
                    if i-j>hdv:
                        hdv=i-j
                        hd=i,j
                    if i-j<bgv:
                        bgv=i-j
                        bg=i,j
    pix[hg]=(255,0,0)
    pix[hd]=(255,0,0)
    pix[bd]=(255,0,0)
    pix[bg]=(255,0,0)
    return hg, hd, bg, bd

def taille(hg,hd,bg,bd):
    largeur1=((hd[0]-hg[0])**2+(hd[1]-hg[1])**2)**(1/2.)
    largeur2=((bd[0]-bg[0])**2+(bd[1]-bg[1])**2)**(1/2.)
    largeur=(largeur1+largeur2)/2.
    hauteur1=((hd[0]-bd[0])**2+(hd[1]-bd[1])**2)**(1/2.)
    hauteur2=((hg[0]-bg[0])**2+(hg[1]-bg[1])**2)**(1/2.)
    hauteur=(hauteur1+hauteur2)/2.
    return largeur,hauteur

def orientation(hg,hd,bg,bd):
    angle1=(hd[1]-hg[1])
    largeur1=((hd[0]-hg[0])**2+(hd[1]-hg[1])**2)**(1/2.)
    angle1=asin((hg[1]-hd[1])/largeur1)
    largeur2=((bd[0]-bg[0])**2+(bd[1]-bg[1])**2)**(1/2.)
    angle2=asin((bg[1]-bd[1])/largeur2)
    hauteur1=((hd[0]-bd[0])**2+(hd[1]-bd[1])**2)**(1/2.)
    angle3=asin((bd[0]-hd[0])/hauteur1)
    hauteur2=((hg[0]-bg[0])**2+(hg[1]-bg[1])**2)**(1/2.)
    angle4=asin((bg[0]-hg[0])/hauteur2)
    angle=(angle1+angle2+angle3+angle4)/4.
    return angle*180./pi
    
for image in range(4):
    im = Image.open(str(image)+'.png')
    pix = im.load()
    size=im.size
    hg,hd,bg,bd=detect_carre(pix)
    print orientation(hg,hd,bg,bd)
    print taille(hg,hd,bg,bd)
    im.save('Copie '+str(image)+'.png')