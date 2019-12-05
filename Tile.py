import sys
import os
import pygame



class Tile:#create class for tiles characteristics
	def __init__(self, north, east, south, west, row, column):
		self.north = north#A property to indicate whether the tile is open on a given side, 0 = closed, 1 = open
		self.east = east
		self.south = south
		self.west = west
		#A property to store whether the tile has a treasure, when we implement separate treasures we can have this store the specific treasure name/number
		self.p1 = 0 #Stores whether player1 is on the tile, we can add additional properties when we start dealing with multiple players
		self.currentrow = row
		self.currentcolumn = column
		self.image = ""
		self.travelable = 0 #A property to tell whether or not the tile is travelable to
		self.treasure = 0 #A property to tell whether or not there is a treasure on this tile
		self.treasure_image = ""



	def get_image_filepath(self):#Takes Tile class instance
		if self.north == 1:
			FilenameNorth = "North"
		else:
			FilenameNorth = ""
		if self.east == 1:
			FilenameEast = "East"
		else:
			FilenameEast = ""
		if self.south == 1:
			FilenameSouth = "South"
		else:
			FilenameSouth = ""
		if self.west == 1:
			FilenameWest = "West"
		else:
			FilenameWest = ""

		#print(FilenameNorth)

		if FilenameNorth == "North" and FilenameEast == "East" and FilenameSouth == "" and FilenameWest == "":#Decides what image is set to depending on tile object
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthEast.png')).convert_alpha()
		elif FilenameNorth == "North" and FilenameEast == "" and FilenameSouth == "" and FilenameWest == "West":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthWest.png')).convert_alpha()
		elif FilenameNorth == "" and FilenameEast == "East" and FilenameSouth == "South" and FilenameWest == "":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'EastSouth.png')).convert_alpha()
		elif FilenameNorth == "" and FilenameEast == "" and FilenameSouth == "South" and FilenameWest == "West":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'SouthWest.png')).convert_alpha()
		elif FilenameNorth == "North" and FilenameEast == "" and FilenameSouth == "South" and FilenameWest == "":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthSouth.png')).convert_alpha()
		elif FilenameNorth == "" and FilenameEast == "East" and FilenameSouth == "" and FilenameWest == "West":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'EastWest.png')).convert_alpha()
		elif FilenameNorth == "North" and FilenameEast == "East" and FilenameSouth == "South" and FilenameWest == "":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthEastSouth.png')).convert_alpha()
		elif FilenameNorth == "North" and FilenameEast == "East" and FilenameSouth == "" and FilenameWest == "West":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthEastWest.png')).convert_alpha()
		elif FilenameNorth == "North" and FilenameEast == "" and FilenameSouth == "South" and FilenameWest == "West":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthSouthWest.png')).convert_alpha()
		elif FilenameNorth == "" and FilenameEast == "East" and FilenameSouth == "South" and FilenameWest == "West":
			self.image = pygame.image.load(os.path.join('..\LabyrinthProject', 'EastSouthWest.png')).convert_alpha()

		#self.image = (tileimage (FilenameNorth, FilenameEast, FilenameSouth, FilenameWest))#Make sure this matches the naming convention for tiles
	def draw(self, screen, pos):#Blits image onto screen
		if self.image != "":
			screen.blit(self.image, pos)

