# [ Python Game for ComputerScience ]
# Written by Brennan Bman.
# Copyright (C) 2014, Brennan Bman
# This file is protected under the GNU GPL v3
# Please see the GPL file distributed with this
# software for more information. 

# Import code from pygame and system.
import pygame, sys

# This line should explain itself...?
from pygame.locals import *

# Init pygame
pygame.init()


# Call the background files and mouse files.
backgroundFile1 = "Background.JPEG"
#backgroundFile2 = "Background2.JEPG"
mouseFile = "mouse.png"
#mouseFile2 = "mouse2.png"

#Create frame
screen = pygame.display.set_mode((720, 484), 0, 32)

# Display the first background.
background = pygame.image.load(backgroundFile).convert()

# Display the mouse image.
mouce_c=pygame.image.load(mouseFile).convert_alpha()

# Update loop. Redisplays images, redraws character, etc. 
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(background, (0,0))

	#x,y = pygame.mouse.get_pos()
	#x -= mouse_c.get_width() / 2
	#y -= mouse_c.get_height() / 2

	#screen.blit(mouse_c, (x, y))
	pygame.display.update()


