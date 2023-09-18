from enum import Enum
import random


class Map :
	def __init__(self, size) :
		self.length = size[0]
		self.width = size[1]
		self.grid = [[Terrain.MOUNTAIN for _ in range(self.length)] for _ in range(self.width)]

	def console_print(self, symbols = None) :
		if symbols is None :
			symbols = {}
			symbols[Terrain.MOUNTAIN] = '█'
			symbols[Terrain.GRASS] = ' '
			symbols[Terrain.ROCK] = '.'
			symbols[Terrain.WATER] = '~'
		for i in self.grid :
			for j in i :
				print(symbols[j], end = '')
			print()

	def firstmap(self) :
		self.width = self.length = 10
		self.grid = [[T.MOUNTAIN for i in range(self.length)],
			[T.MOUNTAIN, T.MOUNTAIN, T.MOUNTAIN, T.MOUNTAIN, T.MOUNTAIN, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.WATER, T.WATER, T.WATER, T.WATER, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.WATER, T.WATER, T.WATER, T.WATER, T.WATER, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.MOUNTAIN, T.ROCK, T.ROCK, T.ROCK, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.MOUNTAIN, T.ROCK, T.ROCK, T.GRASS, T.ROCK, T.ROCK, T.GRASS, T.GRASS, T.MOUNTAIN],
			[T.MOUNTAIN, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.GRASS, T.MOUNTAIN, T.MOUNTAIN],
			[T.MOUNTAIN for i in range(self.length)]]

	def basicmap(self, rockchance = 0.4, waterchance = 0.4) :
		for x in range(self.width):
		    for y in range(self.length):
		        if x == 0 or x == self.width - 1 or y == 0 or y == self.length - 1:
		            self.grid[x][y] = Terrain.MOUNTAIN
		        else:
		            # Randomly place water or rock with a higher probability of grass
		            rand_val = random.random()
		            if rand_val < waterchance:  # Adjust the probability as needed
		                self.grid[x][y] = Terrain.WATER
		            elif rand_val < rockchance:  # Adjust the probability as needed
		                self.grid[x][y] = Terrain.ROCK
		            else:
		                self.grid[x][y] = Terrain.GRASS


class Terrain(Enum) :
	
	MOUNTAIN = 0
	GRASS = 1
	ROCK = 2 
	WATER = 3

T = Terrain