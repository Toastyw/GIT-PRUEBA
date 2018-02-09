#Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2
class Player(pg.sprite.Sprite):

	def __init__(self,game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.Surface((30,40))
		self.image.fill(YELLOW)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT/2)
		self.pos = vec(WIDTH/2,HEIGHT/2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def jump(self):
		#jump only if standing
		
		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		
		if hits:
			self.vel.y =-20

	def update(self):
		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		if hits:
			self.acc = vec(0,0)
			
		else:
			self.acc = vec(0,GRAVITY)
		keys = pg.key.get_pressed()

		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC

		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC

	
		#apply friction
		self.acc.x += self.vel.x*PLAYER_FRICTION
		#equations of position
		self.vel += self.acc

		self.pos.y += self.vel.y + 0.5*self.acc.y
		self.pos.x += self.vel.x + 0.5*self.acc.x
		self.rect.midbottom = self.pos
		self.status()

	def status(self):
		if self.vel.y > 0:
			self.state = "CAENDO"
		if self.vel.y < 0:
			self.state = "SUBIENDO"
		if self.vel.y == 0:
			self.state = "IDLE VERTICAL"
		
	def movement(self):
		pass
class Platform(pg.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y