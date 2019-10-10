#Functions

import pygame
import sys
import os
import random
from random import shuffle
import glob

def button(display, txt, txtColor, font, fontSize, x, y, w, h, ic, ac):#Function which creates button, (display: source of screen) (txt: what the button says) (txtColor: Color of text) (font: what font the text will be) (x, y: coordinates of button) (w, h: width and height of button) (ic, ac: inactive and active color)
	mouse = pygame.mouse.get_pos()#Stores position of mouse
	#click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(display, ac, (x, y, w, h))
	else:
		pygame.draw.rect(display, ic, (x, y, w, h))

	smallText = pygame.font.Font(font, fontSize)
	textSurf, textRect = text_objects(txt, smallText, txtColor)
	textRect.center = ((x + (w / 2)), (y + (h/2)))
	display.blit(textSurf, textRect)

def text_objects(text, font, color):#Defines text contents, font and color for text
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def get_tile_coordinates(col, row):#Function which takes in column and row and returns coordinates of tile
	colRow = tuple([col, row])#Stores col row as coordinate value

	for c in range(7):
		for r in range(7):
			coords = tuple([c*100+(100*3), r*100+100])#Stores coordinate value for current row and column
			pos = tuple([c, r])
			if pos == colRow:
				return(coords)

def grab_and_place_arrows(display):#Function which grabs images of arrows and puts them in positions around board
	mouse = pygame.mouse.get_pos()#Stores position of mouse	

	arrowDownIC = pygame.image.load("ArrowDownIC.png")
	arrowDownAC = pygame.image.load("ArrowDownAC.png")
	arrowUPIC = pygame.image.load("ArrowUPIC.png")
	arrowUPAC = pygame.image.load("ArrowUPAC.png")
	arrowLeftIC = pygame.image.load("ArrowLeftIC.png")
	arrowLeftAC = pygame.image.load("ArrowLeftAC.png")
	arrowRightIC = pygame.image.load("ArrowRightIC.png")
	arrowRightAC = pygame.image.load("ArrowRightAC.png")


	if 400 + 100 > mouse[0] > 400 and 0 + 100 > mouse[1] > 20:#If mouse hovers, then changes image
		display.blit(arrowDownAC, (435, 70))
	else:
		display.blit(arrowDownIC, (435, 35))

	if 600 + 100 > mouse[0] > 600 and 0 + 100 > mouse[1] > 20:
		display.blit(arrowDownAC, (635, 70))
	else:
		display.blit(arrowDownIC, (635, 35))

	if 800 + 100 > mouse[0] > 800 and 0 + 100 > mouse[1] > 20:
		display.blit(arrowDownAC, (835, 70))
	else:
		display.blit(arrowDownIC, (835, 35))

	if 400 + 100 > mouse[0] > 400 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (435, 800))
	else:
		display.blit(arrowUPIC, (435, 835))

	if 600 + 100 > mouse[0] > 600 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (635, 800))
	else:
		display.blit(arrowUPIC, (635, 835))

	if 800 + 100 > mouse[0] > 800 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (835, 800))
	else:
		display.blit(arrowUPIC, (835, 835))

	if 200 + 100 > mouse[0] > 220 and 200 + 100 > mouse[1] > 200:
		display.blit(arrowRightAC, (273, 235))
	else:
		display.blit(arrowRightIC, (238, 235))

	if 200 + 100 > mouse[0] > 220 and 400 + 100 > mouse[1] > 400:
		display.blit(arrowRightAC, (273, 435))
	else:
		display.blit(arrowRightIC, (238, 435))

	if 200 + 100 > mouse[0] > 220 and 600 + 100 > mouse[1] > 600:
		display.blit(arrowRightAC, (273, 635))
	else:
		display.blit(arrowRightIC, (238, 635))

	if 980 + 100 > mouse[0] > 1000 and 200 + 100 > mouse[1] > 200:
		display.blit(arrowLeftAC, (998, 235))
	else:
		display.blit(arrowLeftIC, (1033, 235))

	if 980 + 100 > mouse[0] > 1000 and 400 + 100 > mouse[1] > 400:
		display.blit(arrowLeftAC, (998, 435))
	else:
		display.blit(arrowLeftIC, (1033, 435))

	if 980 + 100 > mouse[0] > 1000 and 600 + 100 > mouse[1] > 600:
		display.blit(arrowLeftAC, (998, 635))
	else:
		display.blit(arrowLeftIC, (1033, 635))

def grab_and_place_movement_keys(display):#Function which grabs images of movement keys and places them in correct positions
	mouse = pygame.mouse.get_pos()#Stores position of mouse	
	click = pygame.mouse.get_pressed()

	moveUpIC = pygame.image.load("moveUpIC.png")
	moveRightIC = pygame.image.load("moveRightIC.png")
	moveDownIC = pygame.image.load("moveDownIC.png")
	moveLeftIC = pygame.image.load("moveLeftIC.png")
	moveUpAC = pygame.image.load("moveUpAC.png")
	moveRightAC = pygame.image.load("moveRightAC.png")
	moveDownAC = pygame.image.load("moveDownAC.png")
	moveLeftAC = pygame.image.load("moveLeftAC.png")	

	if 1110 + 45 > mouse[0] > 1125 and 800 + 60 > mouse[1] > 800:#If mouse clicks, then changes image
		display.blit(moveUpIC, (1110, 800))
		if click[0] == 1:
			display.blit(moveUpAC, (1110, 800))
	else:
		display.blit(moveUpIC, (1110, 800))

	if 1110 + 45 > mouse[0] > 1125 and 870 + 60 > mouse[1] > 870:
		display.blit(moveDownIC, (1110, 870))
		if click[0] == 1:
			display.blit(moveDownAC, (1110, 870))
	else:
		display.blit(moveDownIC, (1110, 870))

	if 1160 + 45 > mouse[0] > 1160 and 825 + 60 > mouse[1] > 845:
		display.blit(moveRightIC, (1160, 835))
		if click[0] == 1:
			display.blit(moveRightAC, (1160, 835))
	else:
		display.blit(moveRightIC, (1160, 835))

	if 1060 + 45 > mouse[0] > 1060 and 825 + 60 > mouse[1] > 845:
		display.blit(moveLeftIC, (1060, 835))
		if click[0] == 1:
			display.blit(moveLeftAC, (1060, 835))
	else:
		display.blit(moveLeftIC, (1060, 835))



def grab_and_randomize_tiles():#Function which grabs tiles in specified directory and puts them in random positions in matrix
	elbowTiles = []#Stores elbow tiles
	straightTiles = []#Stores straight tiles 
	tTiles = []#Stores T Tiles
	randomImagePaths = []#Stores random rotated image paths

	twoDimBoard = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles in random positions

	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory
	for file in glob.glob("Elbow*"):
		elbowTiles.append(file)
	for file in glob.glob("Straight*"):
		straightTiles.append(file)
	for file in glob.glob("T*"):
		tTiles.append(file)
	for x in range(15):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(elbowTiles))
	for x in range(13):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(straightTiles)) 
	for x in range(6):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(tTiles))

	for c in range(7):
		for r in range(7):
			currPos = tuple([c, r])
			if currPos == (0, 1) or currPos == (0, 3) or currPos == (0, 5) or currPos == (1, 0) or currPos == (1, 1) or currPos == (1, 2) or currPos == (1, 3) or currPos == (1, 4) or currPos == (1, 5) or currPos == (1, 6) or currPos == (2, 1) or currPos == (2, 3) or currPos == (2, 5) or currPos == (3, 0) or currPos == (3, 1) or currPos == (3, 2) or currPos == (3, 3) or currPos == (3, 4) or currPos == (3, 5) or currPos == (3, 6) or currPos == (4, 1) or currPos == (4, 3) or currPos == (4, 5) or currPos == (5, 0) or currPos == (5, 1) or currPos == (5, 2) or currPos == (5, 3) or currPos == (5, 4) or currPos == (5, 5) or currPos == (5, 6) or currPos == (6, 1) or currPos == (6, 3) or currPos == (6, 5):#checks if current position is for non fixed tiles
				imagePath = random.choice(randomImagePaths)
				twoDimBoard[c][r] = imagePath
				randomImagePaths.remove(imagePath)

	return twoDimBoard

def grab_fixed_tiles():#Function which grabs tiles in specified directory and puts them in fixed positions in matrix
	elbowTiles = []#Stores elbow tiles
	tTiles = []#Stores T Tiles

	twoDimBoard = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles in fixed positions

	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory
	for file in glob.glob("Starting*"):
		twoDimBoard[0][0] = file#Matrix goes by row first and column second
	for file in glob.glob("ElbowSouthWest*"):
		twoDimBoard[6][0] = file
	for file in glob.glob("ElbowWestNorth*"):
		twoDimBoard[6][6] = file
	for file in glob.glob("ElbowNorthEast*"):
		twoDimBoard[0][6] = file
	for file in glob.glob("TEastSouthWest*"):
		twoDimBoard[2][0] = file
		twoDimBoard[4][0] = file
		twoDimBoard[4][2] = file
	for file in glob.glob("TNorthEastSouth*"):
		twoDimBoard[0][2] = file
		twoDimBoard[2][2] = file
		twoDimBoard[0][4] = file
	for file in glob.glob("TNorthSouthWest*"):
		twoDimBoard[6][2] = file
		twoDimBoard[4][4] = file
		twoDimBoard[6][4] = file
	for file in glob.glob("TWestNorthEast*"):
		twoDimBoard[2][4] = file
		twoDimBoard[2][6] = file
		twoDimBoard[4][6] = file

	return twoDimBoard



		











		



