import pygame as pg
from settings import *
from sprites import *


class Attack(pg.sprite.Sprite):
	def __init__(self,player):
		pg.sprite.Sprite.__init__(self)
		self.cooldown = 200
		self.player = player
		self.inicio = pg.time.get_ticks()
		self.final = pg.time.get_ticks() + self.cooldown
		self.image = pg.Surface((10,10))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.left = self.player.rect.right + 5
		self.rect.centery = self.player.rect.centery
		

	"""
	def update(self):
		self.rect.left = self.player.rect.right
		self.rect.centery = self.player.rect.centery"""
		
