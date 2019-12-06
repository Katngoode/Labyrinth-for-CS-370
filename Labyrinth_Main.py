
#CS370
#Labyrinth

from Labyrinth_Functions import *

from Tile import *
from pygame.locals import *
from Labyrinth_Player import player

import pygame
import sys
import os
import glob
import random
import numpy 
import math
from pygame.rect import Rect
#from enum import Enum
from Sprite import *
import ctypes

pygame.init()#initializes pygame
#WINDOW_SIZE = [1280, 960]
#screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res,pygame.FULLSCREEN)
#surface = pygame.Surface((2560, 1440))
#screen = pygame.display.set_mode((1300, 1000), pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()
area = screen.get_rect()
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




def main_game(display):

	allImageFilesPaths = []

	TILE_ARRAY = numpy.ndarray(shape=(7,7), dtype=object)
	floatingTile = []
	new_tile_initialization(TILE_ARRAY, floatingTile)

	print(get_tile_coordinates(2,0))
	floatPos = tuple([1200, 400])





	screen.fill(BACKGROUNDCOLOR)

	for c in range(ROW_COUNT):#creates gameboard
		for r in range(COLUMN_COUNT):
			pygame.draw.rect(screen, BLACK, (r*SQUARESIZE+(SQUARESIZE*3), c*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))

	#button(screen, "SHUFFLE!", GREEN, "GristledFont-Regular.ttf", 35, 50, 850, 150, 75, PURPLE, LIGHT_PURPLE)#Creates shuffle button
	button(screen, "Quit", BLACK, "freesansbold.ttf", 25, 1205, 10, 65, 36, RED, LIGHT_RED)#Creates quit button
	
	for c in range(ROW_COUNT):#Fills game board with random and fixed tiles
		for r in range(COLUMN_COUNT):
			TILE_ARRAY[r][c].get_image_filepath()
			TILE_ARRAY[r][c].draw(screen, (get_tile_coordinates(c, r)))

	#Initialize player on board
	player_one = player(0, TILE_ARRAY[0][0], r'LabyrinthPlayerOneT.png')
	player_one.update_player(screen)
	init_treasures(TILE_ARRAY, screen)

	while not gameOver:
		for event in pygame.event.get():#Empties event queue
			if event.type == pygame.QUIT:#Sent when User presses close button
				sys.exit()

		click = pygame.mouse.get_pressed()#Stores '1' if click occurs
		mouse = pygame.mouse.get_pos()#Stores position of mouse

		grab_and_place_arrows(screen, TILE_ARRAY, floatingTile, player_one)#Places arrows around the board
		#grab_and_place_movement_keys(screen)#Places movement keys on board

		#display the floating tile
		floatingTile[0].get_image_filepath()
		floatingTile[0].draw(screen, floatPos)
		if floatingTile[0].treasure is not 0:
			display.blit((pygame.image.load(floatingTile[0].treasure_image)), floatPos)

		if 1205 + 65 > mouse[0] > 1205 and 10 + 36 > mouse[1] > 10:#Adds functionality to quit button
			if click[0] == 1:
				sys.exit()

		#Redisplay board if new one has been inserted
		if player_one.TileInserted is 1:
			for c in range(ROW_COUNT):
				for r in range(COLUMN_COUNT):
					TILE_ARRAY[r][c].get_image_filepath()
					TILE_ARRAY[r][c].draw(screen, (get_tile_coordinates(c, r)))
					if TILE_ARRAY[r][c].treasure is not 0:
						display.blit((pygame.image.load(TILE_ARRAY[r][c].treasure_image)), (get_tile_coordinates(c, r)))
					player_one.TileInserted = 2
					player_one.update_player(screen)
		
		#Run pathing function if a tile has been inserted
		if player_one.PathFound is 0 and player_one.TileInserted is 2: #Check to see if pathfinding function has run
			find_path(player_one.get_tile(), TILE_ARRAY)
			color_untravelable_path(player_one, TILE_ARRAY, screen)

		#Check for player clicks on tiles
		for z in range(ROW_COUNT):
			for j in range(COLUMN_COUNT):
				if ((j*100+(100*3)) + 100) > mouse[0] > (j*100+(100*3)) and ((z*100+100) + 100) > mouse[1] > (z*100+100):
					if click[0] == 1:
						player_one.move_player(TILE_ARRAY[z][j], TILE_ARRAY, screen) #Move the player to the tile they clicked if it is travelable
						PathFound = 0

		#End Game if all treasures have been found
		if player_one.treasures is 24:
			return
		
		clock.tick(60)#Sets to 60 frames per second

		pygame.display.flip()

	pygame.quit()#deactivates the pygame library



