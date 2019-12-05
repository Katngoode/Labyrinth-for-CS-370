#CS370
#Labyrinth


from Labyrinth_Functions import *

from Tile import *

import pygame
import sys
import os
import glob
import random
import numpy 

pygame.init()#initializes pygame
WINDOW_SIZE = [1280, 960]
screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
pygame.display.set_caption("Labyrinth")#Sets title of the screen
gameOver = False#Loops until user closes out of game
clock = pygame.time.Clock()#Manages how fast the screen updates

BLACK = (0,0,0)#Colors used in game
GRAY = (120,120,120)
RED = (161, 10, 10)
LIGHT_RED = (255, 48, 48)
PURPLE = (108, 16, 212)
LIGHT_PURPLE = (172, 98, 255)
GREEN = (0, 255, 0)
BACKGROUNDCOLOR = (0, 48, 146)

ROW_COUNT = 7
COLUMN_COUNT = 7
SQUARESIZE = 100

allImageFilesPaths = []


TILE_ARRAY = numpy.ndarray(shape=(7,7), dtype=object)
floatingTile = []
new_tile_initialization(TILE_ARRAY, floatingTile)

Player = TILE_ARRAY[3][3] #Placeholder for player class

print(get_tile_coordinates(2,0))
def main_game(display):

	screen.fill(BACKGROUNDCOLOR)

	for c in range(ROW_COUNT):#creates gameboard
		for r in range(COLUMN_COUNT):
			pygame.draw.rect(screen, BLACK, (r*SQUARESIZE+(SQUARESIZE*3), c*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))

	
	button(screen, "Quit", BLACK, "freesansbold.ttf", 25, 1205, 10, 65, 36, RED, LIGHT_RED)#Creates quit button

	grab_and_place_arrows(screen)#Places arrows around the board
	grab_and_place_movement_keys(screen)#Places movement keys on board

	for c in range(ROW_COUNT):#Fills game board with random and fixed tiles
		for r in range(COLUMN_COUNT):
		#allTiles[r][c].get_image_filepath()
			TILE_ARRAY[r][c].get_image_filepath()
			TILE_ARRAY[r][c].draw(screen, (get_tile_coordinates(c, r)))
		#if randomTilePositions[r][c] != 0:
			#randomTile = pygame.image.load(randomTilePositions[r][c])
			#screen.blit(randomTile, (get_tile_coordinates(r, c)))
		#elif randomTilePositions[r][c] == 0:
			#fixedTile = pygame.image.load(fixedTilePositions[r][c])
			#screen.blit(fixedTile, (get_tile_coordinates(r, c)))

	PathFound = 0

	while not gameOver:
		for event in pygame.event.get():#Empties event queue
			if event.type == pygame.QUIT:#Sent when User presses close button
				sys.exit()		


		click = pygame.mouse.get_pressed()#Stores '1' if click occurs
		mouse = pygame.mouse.get_pos()#Stores position of mouse

		if 1205 + 65 > mouse[0] > 1205 and 10 + 36 > mouse[1] > 10:#Adds functionality to quit button
			if click[0] == 1:
				sys.exit()		
	
		#button(screen, "FIND PATH!", GREEN, "GristledFont-Regular.ttf", 35, 50, 50, 50, 75, PURPLE, LIGHT_PURPLE)#Creates path button
		#if 50 + 50 > mouse[0] > 50 and 50 + 75 > mouse[1] > 50: #Adds functionality to path button
		#	if click[0] == 1:
		
		if PathFound is 0: #Check to see if pathfinding function has run
			find_path(Player, TILE_ARRAY)
			color_untravelable_path(TILE_ARRAY, screen)
			PathFound = 1

		for z in range(ROW_COUNT): #Check if player is clicking on a tile
			for j in range(COLUMN_COUNT):
				if ((j*100+(100*3)) + 100) > mouse[0] > (j*100+(100*3)) and ((z*100+100) + 100) > mouse[1] > (z*100+100):
					if click[0] == 1:
						move_player(TILE_ARRAY[z][j], TILE_ARRAY, screen, Player) #Move the player to the tile they clicked if it is travelable
						PathFound = 0

		#button(screen, "SHUFFLE!", GREEN, "GristledFont-Regular.ttf", 35, 50, 850, 150, 75, PURPLE, LIGHT_PURPLE)#Creates shuffle button
		#if 50 + 150 > mouse[0] > 50 and 850 + 75 > mouse[1] > 850:#Adds functionality to shuffle button
			#if click[0] == 1:
				#randomTilePositions = grab_and_randomize_tiles()


		clock.tick(60)#Sets to 60 frames per second

		pygame.display.flip()

	pygame.quit()#deactivates the pygame library
