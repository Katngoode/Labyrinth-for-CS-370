
import pygame 
import sys
import os
from enum import Enum
from pygame.rect import Rect
from Sprite import *
from Labyrinth_Main import *
from Labyrinth_Functions import *


class player():
    def __init__(self, player_num, tile, image):
        self.player_num = player_num
        self.tile = tile
        self.image = image
        self.treasures = 0
        self.PathFound = 0
        self.TileInserted = 0
    
    
    
    def get_tile(self):
        return self.tile

    def update_player(self, display):
        display.blit(pygame.image.load(r'LabyrinthPlayerOneT.png'), (get_tile_coordinates(self.tile.currentcolumn, self.tile.currentrow)))
    
    def move_player(self, newtile, Array, display):
        if newtile.travelable is 1:
            if newtile.treasure is not 0:
                treasure_found(newtile, display)
                self.treasures += 1
            for x in range(7):
                for y in range(7):
                    Array[y][x].get_image_filepath()
                    Array[y][x].draw(display, (get_tile_coordinates(x, y)))
                    Array[y][x].travelable = 0
                    Array[y][x].p1 = 0
                    if Array[y][x].treasure is not 0:
                        display.blit((pygame.image.load(Array[y][x].treasure_image)), (get_tile_coordinates(x, y)))
            #display.blit(pygame.image.load(r'LabyrinthPlayerOneT.png'), (get_tile_coordinates(tile.currentcolumn, tile.currentrow)))
            newtile.p1 = 1
            self.tile = newtile
            self.TileInserted = 0
            print("Player moved to", newtile.currentcolumn, newtile.currentrow)
            self.update_player(display)