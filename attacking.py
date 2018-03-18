import pygame as pg
from settings import *
from sprites import *
import math

class SaberAttack(pg.sprite.Sprite):
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

class BusterAttack(pg.sprite.Sprite):
	def __init__(self,player,direction):
		pg.sprite.Sprite.__init__(self)
		self.sheet = pg.image.load("Sprites\megamanx.gif")
		self.cooldown = 100
		self.direction = direction
		self.player = player
		self.inicio = pg.time.get_ticks()
		self.final = pg.time.get_ticks() + self.cooldown
		
		
		self.setup_position()
		self.rect.centery = self.player.rect.centery
		self.centroycons = self.rect.centery
	def setup_position(self):
		if self.direction == "RIGHT":
			self.image = get_image(self.sheet,5,377,12,382)
			self.rect = self.image.get_rect()
			self.rect.left = self.player.rect.right + 5
		if self.direction == "LEFT":
			self.image = get_image(self.sheet,5,377,12,382,True)
			self.rect = self.image.get_rect()
			self.rect.right = self.player.rect.left -5

	def update(self):
		if self.direction == "RIGHT":
			
			
			self.rect.x +=8
		if self.direction == "LEFT":
			self.rect.x -=8


def get_image(sheet, x, y, xf, yf,reverse = False):
        """Extracts image from sprite sheet"""
        width = xf - x
        height = yf - y
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale2x(image)
        if reverse:
        	image = pg.transform.flip(image,True,False)

        image = image.convert()

        return image