# [ Python Game for ComputerScience ]
# Written by Brennan Macaig.
# Copyright (C) 2014, Brennan Macaig.
# This file is protected under the GNU GPL v3
# Please see the GPL file distributed with this
# software for more information. 

import pygame, sys

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((720, 484), 0, 32)

backgroundFile = 'Background.JPEG'
background = pygame.image.load(backgroundFile).convert()

while True:

	for event in pygame.event.get():
		if event.type == quit:
			pygame.quit()
			sys.exit()

	screen.blit(background, (0,0))
	pygame.display.update()


