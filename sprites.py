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
		self.rect_ground_detector=pg.Rect(0,0,self.rect.width,4)

	def jump(self):
		#jump only if standing
		for plat in self.game.platforms:
			if self.rect_ground_detector.colliderect(plat.rect):
				print "saltando"
				self.vel.y =-15
		"""
		hits = pg.sprite.spritecollide(self.rect_ground_detector,self.game.platforms,False)
		if self.rect_ground_detector.colliderect(self.game.platforms[0].rect):
			print "saltando"
			self.vel.y =-10
		if hits:
			print "saltando"
			self.vel.y =-10 """
		

	def update(self):
		"""
		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		if hits:
			self.acc = vec(0,0)
			
		else:
			self.acc = vec(0,GRAVITY)"""
		self.rect_ground_detector.centerx = self.rect.centerx
		self.rect_ground_detector.centery = self.rect.bottom +2
		keys = pg.key.get_pressed()

		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
			self.movement(-4)
		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
			self.movement(4)
		self.gravity(GRAVITY)
		"""
		#apply friction
		self.acc.x += self.vel.x*PLAYER_FRICTION
		#equations of position
		self.vel += self.acc

		self.pos.y += self.vel.y + 0.5*self.acc.y
		self.pos.x += self.vel.x + 0.5*self.acc.x
		self.rect.midbottom = self.pos
		self.status()"""

	def status(self):
		if self.vel.y > 0:
			self.state = "CAENDO"
		if self.vel.y < 0:
			self.state = "SUBIENDO"
		if self.vel.y == 0:
			self.state = "IDLE VERTICAL"
	def movement(self,velx):
		if velx != 0:
			self.move_single_axis(velx)
		
	def move_single_axis(self,velx):
		
		
		velx += self.acc.x
		self.rect.x+=velx
		

		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		if hits:
			if velx>0:
				self.rect.right = hits[0].rect.left
			if velx<0:
				self.rect.left=hits[0].rect.right
			
	def gravity(self,gravity):
		
		self.vel.y +=  gravity
		self.rect.y += self.vel.y
		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		if hits:
			
			if self.vel.y>0:
				self.vel.y = 0
				self.rect.bottom = hits[0].rect.top
				
			if self.vel.y<0:
				self.vel.y = 0
				self.rect.top = hits[0].rect.bottom 
				



class Platform(pg.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y