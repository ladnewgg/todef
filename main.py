import pygame
from ga_classes import Map
from ga_classes import Terrain
from pygame.locals import *
import time
import random

board = Map((5, 5))
board.basicmap(0, 0)
# Grid :
GRID_X = 0
GRID_Y = 0
WIDTH = 32
HEIGHT = 32
MARGIN = 0

WINDOW_SIZE = [(WIDTH + MARGIN) * board.width + MARGIN + GRID_X, (HEIGHT + MARGIN) * board.length + MARGIN + GRID_Y]

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TODEF")
gameIcon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(gameIcon)

clock = pygame.time.Clock()
quit = False

Tiles = {}
Tiles[Terrain.MOUNTAIN] = pygame.image.load(f"assets/mountain.png").convert()
Tiles[Terrain.ROCK] = pygame.image.load(f"assets/rock.png").convert()
Tiles[Terrain.GRASS] = pygame.image.load(f"assets/grass.png").convert()
Tiles[Terrain.WATER] = pygame.image.load(f"assets/water.png").convert()

while not quit :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

	screen.fill((0, 0, 0))

	for y in range(board.width):
		for x in range(board.length):
			screen.blit(Tiles[board.grid[x][y]], ((MARGIN + WIDTH) * y + MARGIN + GRID_X, (MARGIN + HEIGHT) * x + MARGIN + GRID_Y))

	clock.tick(20)
	pygame.display.flip()

pygame.quit()
	