# -*- coding: utf-8 -*-
"""
Created on Sat May 05 08:07:25 2018

@author: costa
"""

import pygame as pg
#initialisation de Pygame
pg.init()
#création de la fenêtre d'affichage
screen = pg.display.set_mode((1600,800))
#création des rectangles : boutons et segments
s10 = pg.Rect(370,25,360,25)
s11 = pg.Rect(730,50,25,337)
s12 = pg.Rect(730,413,25,337)
s13 = pg.Rect(370,750,360,25)
s14 = pg.Rect(345,413,25,337)
s15 = pg.Rect(345,50,25,337)
s16 = pg.Rect(370,25,360,25)
s20 = pg.Rect(870,25,360,25)
s21 = pg.Rect(1230,50,25,337)
s22 = pg.Rect(1230,413,25,337)
s23 = pg.Rect(870,750,360,25)
s24 = pg.Rect(845,413,25,337)
s25 = pg.Rect(845,50,25,337)
s26 = pg.Rect(870,387,360,25)
b0 = pg.Rect(50,15,200,25)
b1 = pg.Rect(50,65,200,25)
b2 = pg.Rect(50,115,200,25)
b3 = pg.Rect(50,165,200,25)
b4 = pg.Rect(50,215,200,25)
b5 = pg.Rect(50,265,200,25)
b6 = pg.Rect(50,315,200,25)
b7 = pg.Rect(50,365,200,25)
b8 = pg.Rect(50,415,200,25)
b9 = pg.Rect(50,465,200,25)
ba = pg.Rect(50,515,200,25)
bb = pg.Rect(50,565,200,25)
bc = pg.Rect(50,615,200,25)
bd = pg.Rect(50,665,200,25)
be = pg.Rect(50,715,200,25)
bf = pg.Rect(50,765,200,25)
#mise des rectangles dans des listes et état des rectangles : allumés ou éteints
rects = [s10,s11,s12,s13,s14,s15,s16,s20,s21,s22,s23,s24,s25,s26,b0,b1,b2,b3]
buttons = [b0,b1,b2,b3]
rect_states = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
#initialisation de la police pour l'affichage de texte et liste de texte à ajouter sur les boutons
myfont = pg.font.SysFont("monospace", 20)
labels = ["Start","Stop","+","-"]

running=1
while running:
	#Affichage des boutons et reinitialisation de leur état à éteint 
	i = 0
	for rect in rects:
		if rect_states[i] == 1:
			pg.draw.rect(screen,(255,204,0),rect)
		else:
			pg.draw.rect(screen,(102,102,102),rect)
		i+=1 
	for i in range(14):
		rect_states[i] = 0 	
	i = 0
	for text in labels:
		label = myfont.render(text,1,(0,0,0))
		screen.blit(label,(145,17+i*50))
		i+=1
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
			if mouse_rect.colliderect(bclear):				
				#si clear alors on bloque l'état des rect sur éteint en empechant le changement d'état à allumé 
				pressed = "No button pressed"					
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
	if pressed != "No button pressed":
		#si il y a eu clique on est ici et bins[nb] donne le binaire du bouton touché
		a0 = bins[nb][0]
		a1 = bins[nb][1]
		a2 = bins[nb][2]
		a3 = bins[nb][3]		
		#on determine les No des a0,a1,a2 et a3
		noa0 = No(a0)
		noa1 = No(a1)
		noa2 = No(a2)
		noa3 = No(a3)		
		#Tests pour affichage des segments 
		if And2(noa1,noa3) or And2(a1,a2) or And3(noa0,noa1,a2) or And3(a0,noa1,noa2) or And3(noa0,a1,a3) or And3(a0,a1,noa3):
			rect_states[0] = 1 
		if And2(noa1,noa3) or And3(noa1,noa0,a3) or And3(a0,a3,noa2) or And3(noa0,a2,a3) or And3(noa0,noa2,noa3):
			rect_states[1] = 1
		if And2(noa0,a1) or And2(a0,noa1) or And2(noa2,a3) or And3(noa1,noa2,noa3) or And2(noa1,a3):
			rect_states[2] = 1
		if And3(noa1,noa2,noa3) or And3(noa0,noa1,a2) or And3(a0,noa1,a3) or And3(a1,noa2,a3) or And3(a1,a2,noa3) or And3(a0,a1,noa3):
			rect_states[3] = 1 
		if And3(noa0,noa1,noa3) or And3(a0,noa2,noa3) or And3(a1,a2,noa3) or And3(a0,a1,a3) or And3(a0,noa1,a2):
			rect_states[4] = 1
		if And2(a0,noa1) or And2(a1,noa3) or And3(noa0,a1,noa2) or And3(a0,a1,a2) or And3(noa1,noa2,noa3):
			rect_states[5] = 1
		if And3(noa0,noa1,a2) or And2(a0,noa1) or And3(a0,a1,a2) or And3(noa0,a1,noa3) or And3(a1,noa2,a3):
			rect_states[6] = 1 
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	pg.display.update()	