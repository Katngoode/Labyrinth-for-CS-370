
#Functions

import pygame
import sys
import os
import random
import numpy 
from random import shuffle
import glob
from Tile import *

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

def get_tile_coordinates(row, col):#Function which takes in column and row and returns coordinates of tile
	colRow = tuple([row, col])#Stores col row as coordinate value

	for c in range(7):
		for r in range(7):
			coords = tuple([r*100+(100*3), c*100+100])#Stores coordinate value for current row and column
			pos = tuple([r, c])
			if pos == colRow:
				#print(coords)
				return(coords)

def grab_and_place_arrows(display, TILE_ARRAY, floatingTile):#Function which grabs images of arrows and puts them in positions around board
	mouse = pygame.mouse.get_pos()#Stores position of mouse	
	click = pygame.mouse.get_pressed()

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
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 0, 1)
	else:
		display.blit(arrowDownIC, (435, 35))

	if 600 + 100 > mouse[0] > 600 and 0 + 100 > mouse[1] > 20:
		display.blit(arrowDownAC, (635, 70))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 0, 3)
	else:
		display.blit(arrowDownIC, (635, 35))

	if 800 + 100 > mouse[0] > 800 and 0 + 100 > mouse[1] > 20:
		display.blit(arrowDownAC, (835, 70))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 0, 5)
	else:
		display.blit(arrowDownIC, (835, 35))

	if 400 + 100 > mouse[0] > 400 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (435, 800))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 6, 1)
	else:
		display.blit(arrowUPIC, (435, 835))

	if 600 + 100 > mouse[0] > 600 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (635, 800))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 6, 3)
	else:
		display.blit(arrowUPIC, (635, 835))

	if 800 + 100 > mouse[0] > 800 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (835, 800))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 6, 5)
	else:
		display.blit(arrowUPIC, (835, 835))

	if 200 + 100 > mouse[0] > 220 and 200 + 100 > mouse[1] > 200:
		display.blit(arrowRightAC, (273, 235))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 1, 0)
	else:
		display.blit(arrowRightIC, (238, 235))

	if 200 + 100 > mouse[0] > 220 and 400 + 100 > mouse[1] > 400:
		display.blit(arrowRightAC, (273, 435))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 3, 0)
	else:
		display.blit(arrowRightIC, (238, 435))

	if 200 + 100 > mouse[0] > 220 and 600 + 100 > mouse[1] > 600:
		display.blit(arrowRightAC, (273, 635))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 5, 0)
	else:
		display.blit(arrowRightIC, (238, 635))

	if 980 + 100 > mouse[0] > 1000 and 200 + 100 > mouse[1] > 200:
		display.blit(arrowLeftAC, (998, 235))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 1, 6)
	else:
		display.blit(arrowLeftIC, (1033, 235))

	if 980 + 100 > mouse[0] > 1000 and 400 + 100 > mouse[1] > 400:
		display.blit(arrowLeftAC, (998, 435))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 3, 6)
	else:
		display.blit(arrowLeftIC, (1033, 435))

	if 980 + 100 > mouse[0] > 1000 and 600 + 100 > mouse[1] > 600:
		display.blit(arrowLeftAC, (998, 635))
		if click[0] == 1:
			tile_insertion(TILE_ARRAY, floatingTile, 5, 6)
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

#def get_image_filepath(tile):#Takes Tile class instance

#	tile.image = ("%%%%.png" (tile.north, tile.east, tile.south, tile.west))#Make sure this matches the naming convention for tiles

def rotate_tile_clockwise(tile):
	tilevalue = tile.north
	tile.north = tile.west
	tile.west = tile.south
	tile.south = tile.east
	tile.east = tilevalue

def tile_insertion(TILE_ARRAY, floatingTile, row, col):#row and col of location where tile is being inserted
	tempTile = [0]
	if row == 0:
		tempTile[0] = floatingTile[0]
		floatingTile[0] = TILE_ARRAY[6][col]#I may want to clear the floatingTile's currentrow and currentcolumn here if it become a problem
		TILE_ARRAY[6][col] = TILE_ARRAY[5][col]
		TILE_ARRAY[6][col].currentrow = 6
		TILE_ARRAY[6][col].currentcolumn = col
		TILE_ARRAY[5][col] = TILE_ARRAY[4][col]
		TILE_ARRAY[5][col].currentrow = 5
		TILE_ARRAY[5][col].currentcolumn = col
		TILE_ARRAY[4][col] = TILE_ARRAY[3][col]
		TILE_ARRAY[4][col].currentrow = 4
		TILE_ARRAY[4][col].currentcolumn = col
		TILE_ARRAY[3][col] = TILE_ARRAY[2][col]
		TILE_ARRAY[3][col].currentrow = 3
		TILE_ARRAY[3][col].currentcolumn = col
		TILE_ARRAY[2][col] = TILE_ARRAY[1][col]
		TILE_ARRAY[2][col].currentrow = 2
		TILE_ARRAY[2][col].currentcolumn = col
		TILE_ARRAY[1][col] = TILE_ARRAY[0][col]
		TILE_ARRAY[1][col].currentrow = 1
		TILE_ARRAY[1][col].currentcolumn = col
		TILE_ARRAY[0][col] = tempTile[0]
		TILE_ARRAY[0][col].currentrow = 0
		TILE_ARRAY[0][col].currentcolumn = col
		print(floatingTile[0])
	if row == 6:
		tempTile[0] = floatingTile[0]
		floatingTile[0] = TILE_ARRAY[0][col]
		TILE_ARRAY[0][col] = TILE_ARRAY[1][col]
		TILE_ARRAY[0][col].currentrow = 0
		TILE_ARRAY[0][col].currentcolumn = col
		TILE_ARRAY[1][col] = TILE_ARRAY[2][col]
		TILE_ARRAY[1][col].currentrow = 1
		TILE_ARRAY[1][col].currentcolumn = col
		TILE_ARRAY[2][col] = TILE_ARRAY[3][col]
		TILE_ARRAY[2][col].currentrow = 2
		TILE_ARRAY[2][col].currentcolumn = col
		TILE_ARRAY[3][col] = TILE_ARRAY[4][col]
		TILE_ARRAY[3][col].currentrow = 3
		TILE_ARRAY[3][col].currentcolumn = col
		TILE_ARRAY[4][col] = TILE_ARRAY[5][col]
		TILE_ARRAY[4][col].currentrow = 4
		TILE_ARRAY[4][col].currentcolumn = col
		TILE_ARRAY[5][col] = TILE_ARRAY[6][col]
		TILE_ARRAY[5][col].currentrow = 5
		TILE_ARRAY[5][col].currentcolumn = col
		TILE_ARRAY[6][col] = tempTile[0]
		TILE_ARRAY[6][col].currentrow = 6
		TILE_ARRAY[6][col].currentcolumn = col
		print(floatingTile[0])
	if col == 0:
		tempTile[0] = floatingTile[0]
		floatingTile[0] = TILE_ARRAY[row][6]
		TILE_ARRAY[row][6] = TILE_ARRAY[row][5]
		TILE_ARRAY[row][6].currentrow = row
		TILE_ARRAY[row][6].currentcolumn = 6
		TILE_ARRAY[row][5] = TILE_ARRAY[row][4]
		TILE_ARRAY[row][5].currentrow = row
		TILE_ARRAY[row][5].currentcolumn = 5
		TILE_ARRAY[row][4] = TILE_ARRAY[row][3]
		TILE_ARRAY[row][4].currentrow = row
		TILE_ARRAY[row][4].currentcolumn = 4
		TILE_ARRAY[row][3] = TILE_ARRAY[row][2]
		TILE_ARRAY[row][3].currentrow = row
		TILE_ARRAY[row][3].currentcolumn = 3
		TILE_ARRAY[row][2] = TILE_ARRAY[row][1]
		TILE_ARRAY[row][2].currentrow = row
		TILE_ARRAY[row][2].currentcolumn = 2
		TILE_ARRAY[row][1] = TILE_ARRAY[row][0]
		TILE_ARRAY[row][1].currentrow = row
		TILE_ARRAY[row][1].currentcolumn = 1
		TILE_ARRAY[row][0] = tempTile[0]
		TILE_ARRAY[row][0].currentrow = row
		TILE_ARRAY[row][0].currentcolumn = 0
		print(floatingTile[0])
	if col == 6:
		tempTile[0] = floatingTile[0]
		floatingTile[0] = TILE_ARRAY[row][0]
		TILE_ARRAY[row][0] = TILE_ARRAY[row][1]
		TILE_ARRAY[row][0].currentrow = row
		TILE_ARRAY[row][0].currentcolumn = 0
		TILE_ARRAY[row][1] = TILE_ARRAY[row][2]
		TILE_ARRAY[row][1].currentrow = row
		TILE_ARRAY[row][1].currentcolumn = 1
		TILE_ARRAY[row][2] = TILE_ARRAY[row][3]
		TILE_ARRAY[row][2].currentrow = row
		TILE_ARRAY[row][2].currentcolumn = 2
		TILE_ARRAY[row][3] = TILE_ARRAY[row][4]
		TILE_ARRAY[row][3].currentrow = row
		TILE_ARRAY[row][3].currentcolumn = 3
		TILE_ARRAY[row][4] = TILE_ARRAY[row][5]
		TILE_ARRAY[row][4].currentrow = row
		TILE_ARRAY[row][4].currentcolumn = 4
		TILE_ARRAY[row][5] = TILE_ARRAY[row][6]
		TILE_ARRAY[row][5].currentrow = row
		TILE_ARRAY[row][5].currentcolumn = 5
		TILE_ARRAY[row][6] = tempTile[0]
		TILE_ARRAY[row][6].currentrow = row
		TILE_ARRAY[row][6].currentcolumn = 6
		print(floatingTile[0])


def new_tile_initialization(TILE_ARRAY, floatingTile):
	#TILE_ARRAY = allFilePaths
	#TILE_ARRAY = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles
	#get_tile_coordinates(0, 0),STARTING01,
	
	t0 = Tile(0,1,1,0,0,0)#initialize and place all of the tiles that dont move
	TILE_ARRAY[0][0]=t0
	t1 = Tile(0,1,1,1,0,2)
	TILE_ARRAY[0][2]=t1
	t2 = Tile(0,1,1,1,0,4)
	TILE_ARRAY[0][4]=t2
	t3 = Tile(0,0,1,1,0,6)
	TILE_ARRAY[0][6]=t3
	t4 = Tile(1,1,1,0,2,0)
	TILE_ARRAY[2][0]=t4
	t5 = Tile(1,1,1,0,2,2)
	TILE_ARRAY[2][2]=t5
	t6 = Tile(0,1,1,1,2,4)
	TILE_ARRAY[2][4]=t6
	t7 = Tile(1,0,1,1,2,6)
	TILE_ARRAY[2][6]=t7
	t8 = Tile(1,1,1,0,4,0)
	TILE_ARRAY[4][0]=t8
	t9 = Tile(1,1,0,1,4,2)
	TILE_ARRAY[4][2]=t9
	t10 = Tile(1,0,1,1,4,4)
	TILE_ARRAY[4][4]=t10
	t11 = Tile(1,0,1,1,4,6)
	TILE_ARRAY[4][6]=t11
	t12 = Tile(1,1,0,0,6,0)

	TILE_ARRAY[6][0]=t12
	t13 = Tile(1,1,0,1,6,2)
	TILE_ARRAY[6][2]=t13
	t14 = Tile(1,1,0,1,6,4)
	TILE_ARRAY[6][4]=t14
	t15 = Tile(1,0,0,1,6,6)
	TILE_ARRAY[6][6]=t15
	t16 = Tile(1,0,1,0,0,0)#Straight tiles
	t17 = Tile(1,0,1,0,0,0)
	t18 = Tile(1,0,1,0,0,0)
	t19 = Tile(1,0,1,0,0,0)
	t20 = Tile(1,0,1,0,0,0)
	t21 = Tile(1,0,1,0,0,0)
	t22 = Tile(1,0,1,0,0,0)
	t23 = Tile(1,0,1,0,0,0)
	t24 = Tile(1,0,1,0,0,0)
	t25 = Tile(1,0,1,0,0,0)
	t26 = Tile(1,0,1,0,0,0)
	t27 = Tile(1,0,1,0,0,0)
	t28 = Tile(1,0,1,0,0,0)
	t29 = Tile(1,1,0,0,0,0)#Elbow tiles
	t30 = Tile(1,1,0,0,0,0)
	t31 = Tile(1,1,0,0,0,0)
	t32 = Tile(1,1,0,0,0,0)
	t33 = Tile(1,1,0,0,0,0)
	t34 = Tile(1,1,0,0,0,0)
	t35 = Tile(1,1,0,0,0,0)
	t36 = Tile(1,1,0,0,0,0)
	t37 = Tile(1,1,0,0,0,0)
	t38 = Tile(1,1,0,0,0,0)
	t39 = Tile(1,1,0,0,0,0)
	t40 = Tile(1,1,0,0,0,0)
	t41 = Tile(1,1,0,0,0,0)
	t42 = Tile(1,1,0,0,0,0)
	t43 = Tile(1,1,0,0,0,0)
	t44 = Tile(1,1,0,0,0,0)
	t45 = Tile(1,1,0,0,0,0)
	t46 = Tile(1,1,0,0,0,0)
	t47 = Tile(1,1,1,0,0,0)#T tiles
	t48 = Tile(1,1,1,0,0,0)
	t49 = Tile(1,1,1,0,0,0)#extra tile This comment is weird

	initializationList = [t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44,t45,t46,t47,t48,t49]

	for a in initializationList:
		for b in range(random.randint(0,3)):
			rotate_tile_clockwise(a)
	random.shuffle(initializationList)
	for column in range(7):
		for row in range(7):
			#if [row][column] != t0 or [row][column] != t1 or [row][column] != t2 or [row][column] != t3 or [row][column] != t4 or [row][column] != t5 or [row][column] != t6 or [row][column] != t7 or [row][column] != t8 or [row][column] != t9 or [row][column] != t10 or [row][column] != t11 or [row][column] != t12 or [row][column] != t13 or [row][column] != t14 or [row][column] != t15:
			if TILE_ARRAY[row][column] == None:#This is testing if TILE_ARRAY[row][column] is empty, may have to change logic to work
				TILE_ARRAY[row][column] = initializationList[0]
				TILE_ARRAY[row][column].currentrow = row
				TILE_ARRAY[row][column].currentcolumn = column
				del initializationList[0]
	floatingTile.append(initializationList[0])
	#print(TILE_ARRAY)#shows contents of tile_array
	return TILE_ARRAY, floatingTile

def find_path(tile, Array):

	tile.travelable = 1

	if tile.currentrow <=0:
		NTile = None
	else:
		NTile = Array[((tile.currentrow)-1)][(tile.currentcolumn)]

	if tile.currentrow >=6:
		STile = None
	else:
		STile = Array[((tile.currentrow)+1)][(tile.currentcolumn)]

	if tile.currentcolumn >=6:
		ETile = None
	else:
		ETile = Array[(tile.currentrow)][((tile.currentcolumn)+1)]

	if tile.currentcolumn <=0:
		WTile = None
	else:
		WTile = Array[(tile.currentrow)][((tile.currentcolumn)-1)]

	if tile.north is 1 and NTile is not None and NTile.south is 1 and NTile.travelable is 0:
		#print("Tile Travelable South to North from", tile.currentrow, tile.currentcolumn, "to", NTile.currentrow, NTile.currentcolumn)
		find_path(NTile, Array)

	if tile.east is 1 and ETile is not None and ETile.west is 1 and ETile.travelable is 0:
		#print("Tile Travelable West to East", tile.currentrow, tile.currentcolumn, "to", ETile.currentrow, ETile.currentcolumn)
		find_path(ETile, Array)

	if tile.south is 1 and STile is not None and STile.north is 1 and STile.travelable is 0:
		#print("Tile Travelable North to South", tile.currentrow, tile.currentcolumn, "to", STile.currentrow, STile.currentcolumn)
		find_path(STile, Array)

	if tile.west is 1 and WTile is not None and WTile.east is 1 and WTile.travelable is 0:
		#print("Tile Travelable East to West", tile.currentrow, tile.currentcolumn, "to", WTile.currentrow, WTile.currentcolumn)
		find_path(WTile, Array)


def color_untravelable_path(Array, display):
	for x in range(7):
		for y in range(7):
			if Array[x][y].travelable is 0:
				Array[x][y].image.fill((150, 0, 0, 255), special_flags=pygame.BLEND_RGB_MULT) #Color unmoveable path red
				display.blit(Array[x][y].image, (get_tile_coordinates(y, x)))
			if Array[x][y].treasure is not 0:
					display.blit((pygame.image.load(Array[x][y].treasure_image)), (get_tile_coordinates(y, x)))


def move_player(tile, Array, display, PlayerPos):	
	if tile.travelable is 1:
		if tile.treasure is not 0:
			treasure_found(tile, display)
		for x in range(7):
			for y in range(7):
				Array[y][x].get_image_filepath()
				Array[y][x].draw(display, (get_tile_coordinates(x, y)))
				Array[y][x].travelable = 0
				Array[y][x].p1 = 0
				if Array[y][x].treasure is not 0:
					display.blit((pygame.image.load(Array[y][x].treasure_image)), (get_tile_coordinates(x, y)))
		display.blit(pygame.image.load(r'LabyrinthPlayerOneT.png'), (get_tile_coordinates(tile.currentcolumn, tile.currentrow)))
		tile.p1 = 1
		PlayerPos = tile
		print("Player moved to", tile.currentcolumn, tile.currentrow)

def treasure_found(tile, display):
	#incrememnt player score
	print("Player has found a treasure!")
	tile.treasure = 0


def init_treasures(Array, display):
	for j in range(24): #Randomize the location of all 24 treasures into the array
		y = random.randint(0,6)
		x = random.randint(0,6)
		if Array[y][x].treasure is 0:
			Array[y][x].treasure = random.randint(1,7) #Randomize each treasure as one of four images
			if Array[y][x].treasure is 1:
				Array[y][x].treasure_image = "Treasure1.png"
			elif Array[y][x].treasure is 2:
				Array[y][x].treasure_image = "Treasure2.png"
			elif Array[y][x].treasure is 3:
				Array[y][x].treasure_image = "Treasure3.png"
			elif Array[y][x].treasure is 4:
				Array[y][x].treasure_image = "Treasure4.png"
			elif Array[y][x].treasure is 5:
				Array[y][x].treasure_image = "Treasure5.png"
			elif Array[y][x].treasure is 6:
				Array[y][x].treasure_image = "Treasure6.png"
			else:
				Array[y][x].treasure_image = "Treasure7.png"
			display.blit((pygame.image.load(Array[y][x].treasure_image)), (get_tile_coordinates(x, y)))