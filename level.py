import pygame as pg
from settings import *
from sprites import *


class Level(pg.sprite.Sprite):
	def __init__(self,game):
		pg.sprite.Sprite.__init__(self)
		self.map = []
		self.game = game
		self.x = 0
		self.y = 0

	def map_design_1(self):
		
		self.map = [
		"WWWWWWWWWWWWWWWW",
		"W  W   W   W W W",
		"W              W",
		"W              W",
		"WWWWW   W  WWW W",
		"W              W",
		"W          WW  W",
		"WWW            W",
		"W           WWWW",
		"WW             W",
		"W          WWWWW",
		"W  W   W   W W W",
		"W              W",
		"W              W",
		"WWWWW   W  WWW W",
		"W              W",
		"W          WWWWW",
		"WWWWWWW        W",
		"W           WWWW",
		"WWWWWWWWWWWWWWWW",
		]
		for fila in self.map:
			for col in fila:
				if col == "W":
					Plat = Platform(self.x,self.y,30,30)
					self.game.platforms.add(Plat)
					self.game.all_sprites.add(Plat)
				self.x+=30
			self.y+=30
			self.x=0


