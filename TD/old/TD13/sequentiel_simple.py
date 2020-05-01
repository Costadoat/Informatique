# -*- coding: utf-8 -*-
"""
Created on Sat May 05 08:07:25 2018

@author: quillot/costa
"""

import pygame as pg
import datetime
#initialisation de Pygame
pg.init()
#création de la fenêtre d'affichage
screen = pg.display.set_mode((800,250))
#création des rectangles : boutons et segments
s0 = pg.Rect(370,25,360,75)
b0 = pg.Rect(50,15,200,25)
b1 = pg.Rect(50,65,200,25)
b2 = pg.Rect(50,115,200,25)
b3 = pg.Rect(50,165,200,25)
b4 = pg.Rect(50,215,200,25)
#mise des rectangles dans des listes et état des rectangles : allumés ou éteints
rects = [s0,b0,b1,b2,b3,b4]
buttons = [b0,b1,b2,b3,b4]
#initialisation de la police pour l'affichage de texte et liste de texte à ajouter sur les boutons
myfont = pg.font.SysFont("monospace", 20)
labels = ["Start","Power","Stop","Plus","Moins"]
i = 0
pg.draw.rect(screen,(0,174,0),b0)
pg.draw.rect(screen,(237,255,0),b1)
pg.draw.rect(screen,(255,0,0),b2)
pg.draw.rect(screen,(237,255,0),b3)
pg.draw.rect(screen,(237,255,0),b4)
#Affichage des boutons et reinitialisation de leur état à éteint 
i = 0
for text in labels:
    label = myfont.render(text,1,(0,0,0))
    screen.blit(label,(130,17+i*50))
    i+=1

running=1
nb=10
etat=0
while running:
    #Detection des évenèments utilisateurs 
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:			
            print(event)
            if event.key == pg.K_ESCAPE:
                running = 0 
                pg.quit()
    #Enregistrement des coordonnées de la souris si il y a eu un clique 
        if event.type == pg.MOUSEBUTTONDOWN:
            mcoords = pg.mouse.get_pos()
            #création d'un mini rect 1x1 à cet emplacement puis test de collision avec les boutons
            mouse_rect = pg.Rect(mcoords[0],mcoords[1],1,1) 
            i = 0
            for button in buttons:
                if mouse_rect.colliderect(button):
                    #si bouton autre que clear alors on regarde quel bouton est touché
                    pressed = labels[i]
                    nb = i
                    print(pressed)
                    print(nb)
                i+=1   									
            mcoords = (0,0)
    if etat==0 and nb==1:
        etat=1
        fin = datetime.datetime.now() + datetime.timedelta(0,3)
        nb=10
    if etat==1 and (nb==1 or datetime.datetime.now().time()>fin.time()):
        etat=0
        nb=10

    if etat==0:
        pg.draw.rect(screen,(255,0,0),s0)
        label = myfont.render("INIT",1,(0,0,0))
        screen.blit(label,(500,30))
        label = myfont.render("00:00",1,(0,0,0))
        screen.blit(label,(510,60))
    if etat==1:
        pg.draw.rect(screen,(0,174,0),s0)
        label = myfont.render("MODE PUISSANCE",1,(0,0,0))
        screen.blit(label,(500,30))
        duree=fin-datetime.datetime.now()
        label = myfont.render(str(duree)[3:7],1,(0,0,0))
        screen.blit(label,(510,60))
    if etat==2:
        pg.draw.rect(screen,(237,255,0),s0)
        label = myfont.render("Pause",1,(0,0,0))
        screen.blit(label,(510,30))
        label = myfont.render("00:00",1,(0,0,0))
        screen.blit(label,(510,60))
    pg.display.update()
