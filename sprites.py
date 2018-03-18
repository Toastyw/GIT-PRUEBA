import pygame as pg
from settings import *
from attacking import *

vec = pg.math.Vector2
class Player(pg.sprite.Sprite):


	def __init__(self,game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		"""
		self.image = pg.Surface((30,30))
		self.image.fill(YELLOW)"""
		self.sheet = pg.image.load("Sprites\zerox3.gif")
		self.sprite_setup()
		self.image = self.sheet_idle_right[0]
		self.image = self.image.convert()
		self.rect = self.image.get_rect()       
		self.hitbox = self.rect.inflate(10,-2)

		self.not_ground = False
		

		self.pos = vec(60,60)
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		self.vel_y_max = 15
		self.rect_ground_detector=pg.Rect(0,0,self.rect.width,4)
		self.direction = "RIGHT"

		self.time_saber = 0
		self.time_buster = 0
		self.is_attacking_saber = False
		self.is_attacking_buster = False
		
		self.gravedad = GRAVITY

		

		self.another_bool = True
		self.setup_timers_frames()
	def setup_timers_frames(self):
		self.c = 0
		self.d = 0

		self.e = 0
		self.f = 0

		self.g = 0
		self.h = 0

		self.i = 0
		self.j = 0

		self.k = 0
		self.l = 0

		self.ll = 0
		self.o = 0

		self.p = 0
		self.q = 0

	def sprite_setup(self):
		#Moving Right
		self.sheet_moving_right = []
		

		self.image_1 =  get_image(self.sheet,48,12,93,55)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,101,10,142,53)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,148,9,187,53)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,199,9,237,52)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,253,8,293,50)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,304,9,345,51)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,352,7,392,50)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,398,8,438,52)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,445,9,491,52)
		self.sheet_moving_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,553,7,598,49)
		self.sheet_moving_right.append(self.image_1)

		#moving left
		self.sheet_moving_left = []

		self.image_1 =  get_image(self.sheet,48,12,93,55,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,101,10,142,53,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,148,9,187,53,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,199,9,237,52,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,253,8,293,50,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,304,9,345,51,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,352,7,392,50,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,398,8,438,52,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,445,9,491,52,True)
		self.sheet_moving_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,553,7,598,49,True)
		self.sheet_moving_left.append(self.image_1)

		

		self.sheet_idle_right = []

		self.image_1 =  get_image(self.sheet,3,12,40,55)

		self.sheet_idle_right.append(self.image_1)


		self.sheet_idle_left = []

		self.image_1 =  get_image(self.sheet,3,12,40,55,True)

		self.sheet_idle_left.append(self.image_1)
		
		#elevandose a la derecha
		self.sheet_ascending_right = []

		self.image_1 = get_image(self.sheet,4,407,43,458)
		self.image_2 = get_image(self.sheet,52,405,89,456)
		self.image_3 = get_image(self.sheet,98,404,131,454)
		self.image_4 = get_image(self.sheet,146,405,179,455)

		self.sheet_ascending_right.append(self.image_1)
		self.sheet_ascending_right.append(self.image_2)
		self.sheet_ascending_right.append(self.image_3)
		self.sheet_ascending_right.append(self.image_4)

		#elevandose a la izquierda
		self.sheet_ascending_left = []

		self.image_5 = get_image(self.sheet,4,407,43,458,True)
		self.image_6 = get_image(self.sheet,52,405,89,456,True)
		self.image_7 = get_image(self.sheet,98,404,131,454,True)
		self.image_8 = get_image(self.sheet,146,405,179,455,True)

		self.sheet_ascending_left.append(self.image_5)
		self.sheet_ascending_left.append(self.image_6)
		self.sheet_ascending_left.append(self.image_7)
		self.sheet_ascending_left.append(self.image_8)
		#maxima elevacion derecha
		self.sheet_max_height_right = []

		self.image_9 = get_image(self.sheet,191,402,229,453)

		self.sheet_max_height_right.append(self.image_9)
		#maxima elevacion izquierda
		self.sheet_max_height_left = []

		self.image_10 = get_image(self.sheet,191,402,229,453,True)

		self.sheet_max_height_left.append(self.image_10)

		#descendiendo derecha
		self.sheet_descending_right = []

		self.image_11 = get_image(self.sheet,240,391,275,456)
		self.image_12 = get_image(self.sheet,285,391,318,457)

		self.sheet_descending_right.append(self.image_11)
		self.sheet_descending_right.append(self.image_12)

		#descendiendo izquierda
		self.sheet_descending_left = []

		self.image_13 = get_image(self.sheet,240,391,275,456,True)
		self.image_14 = get_image(self.sheet,285,391,318,457,True)

		self.sheet_descending_left.append(self.image_13)
		self.sheet_descending_left.append(self.image_14)

		#attacking right

		self.sheet_attacking_saber_standing_right = []
		
		self.image_1 =  get_image(self.sheet,6,201,42,243)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,47,201,81,243)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,91,200,136,242)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,152,198,200,241)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,283,191,362,242)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,376,198,455,239)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,464,204,543,238)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,552,203,627,237)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,635,203,704,237)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,716,205,760,239)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		self.image_1 =  get_image(self.sheet,771,197,815,239)
		self.sheet_attacking_saber_standing_right.append(self.image_1)

		#Attacking left

		self.sheet_attacking_saber_standing_left = []
		
		self.image_1 =  get_image(self.sheet,6,201,42,243,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,47,201,81,243,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,91,200,136,242,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,152,198,200,241,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,283,191,362,242,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,376,198,455,239,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,464,204,543,238,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,552,203,627,237,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,635,203,704,237,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,716,205,760,239,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)

		self.image_1 =  get_image(self.sheet,771,197,815,239,True)
		self.sheet_attacking_saber_standing_left.append(self.image_1)
		
		#Attacking Buster
		self.sheet_attacking_buster_standing_right = []

		self.image_1 =  get_image(self.sheet,462,143,507,186)
		self.sheet_attacking_buster_standing_right.append(self.image_1)

		self.sheet_attacking_buster_standing_left = []

		self.image_1 =  get_image(self.sheet,462,143,507,186,True)
		self.sheet_attacking_buster_standing_left.append(self.image_1)


		#Sliding Right
		self.sheet_sliding_right = []

		self.image_1 =  get_image(self.sheet,771,197,815,239,True)
		self.sheet_sliding_right.append(self.image_1)





	def comprov_falling(self):
		hits = pg.sprite.spritecollide(self,self.game.platforms,False,collided_1)
		if not hits:
			self.gravedad = GRAVITY
		else: self.gravedad = 0

	def jump(self):
		#jump only if standing
		
		hits1 = pg.sprite.spritecollide(self,self.game.platforms,False,collided_1)
		if hits1:
			self.vel.y =-15
		
	def jump_wall(self):
		hits1 = pg.sprite.spritecollide(self,self.game.platforms,False,collided)
		if self.not_ground and hits1:
			self.vel.y = -15
			

	def update(self):
		
		
		self.hitbox.center = self.rect.center
		self.rect_ground_detector.centerx = self.rect.centerx
		self.rect_ground_detector.centery = self.rect.bottom +2
		self.status()
		self.comprov_falling()

		keys = pg.key.get_pressed()
		self.attack_saber_comprobation()
		self.attack_buster_comprobation()
	

		if keys[pg.K_LEFT] and (not self.is_attacking_saber) and (not self.is_attacking_buster):
			self.acc.x = -PLAYER_ACC
			self.movement_x(-3)
			
			if not self.not_ground:
				self.state = "MOVING"
				
			self.direction = "LEFT"
		else:
			self.vel.x = 0

		if keys[pg.K_RIGHT] and (not self.is_attacking_saber) and (not self.is_attacking_buster):
			self.acc.x = PLAYER_ACC
			self.movement_x(3)
			
			if not self.not_ground:
				self.state = "MOVING"
				
			self.direction = "RIGHT"
		else:
			self.vel.x = 0

		if keys[pg.K_l]:
			self.rect.inflate_ip(1,0)
		if keys[pg.K_m]:
			self.rect.inflate_ip(-1,0)

		self.sprite_animation()
		
		
		


		self.gravity()
		self.collide_detection_y_axis()
		
	def sprite_animation(self):
		if self.state == "MOVING":
			if self.direction == "LEFT":
				self.d,self.image = animation(self.d,self.sheet_moving_left,0.5,1)[0:2]
			if self.direction == "RIGHT":
				self.c,self.image = animation(self.c,self.sheet_moving_right,0.5,1)[0:2]

		if self.state  == "IDLE HORIZONTAL" and (not self.is_attacking_saber) and (not self.is_attacking_buster):
			self.c = 0
			self.d = 0

			if self.direction == "LEFT":
				self.e,self.image = animation(self.e,self.sheet_idle_left,0.6,1)[0:2]
				
			if self.direction == "RIGHT":
				self.f,self.image = animation(self.f,self.sheet_idle_right,0.6,1)[0:2]
				self.c = 0
				self.d = 0
		

		if self.state == "SUBIENDO":
			if self.direction == "LEFT":
				self.g,self.image = animation(self.g,self.sheet_ascending_left,0.6,1)[0:2]
			if self.direction == "RIGHT":
				self.h,self.image = animation(self.h,self.sheet_ascending_right,0.6,1)[0:2]
		
		if self.state == "CAENDO":
			if self.direction == "LEFT":
				self.i,self.image = animation(self.i,self.sheet_descending_left,0.8,0)[0:2]
			if self.direction == "RIGHT":
				self.j,self.image = animation(self.j,self.sheet_descending_right,0.8,0)[0:2]

		if self.state == "ATTACKING_SABER":
			if self.direction == "LEFT":
				self.k,self.image = animation(self.k,self.sheet_attacking_saber_standing_left,0.4,0)[0:2]
				
			if self.direction == "RIGHT":
				self.l,self.image = animation(self.l,self.sheet_attacking_saber_standing_right,0.4,0)[0:2]

		if self.state == "ATTACKING_BUSTER":
			if self.direction == "LEFT":
				self.p,self.image = animation(self.l,self.sheet_attacking_buster_standing_left,0.4,0)[0:2]
			if self.direction == "RIGHT":
				self.q,self.image = animation(self.l,self.sheet_attacking_buster_standing_right,0.4,0)[0:2]

		if self.state == "IDLE VERTICAL":
			if self.direction == "LEFT":
				self.ll,self.image = animation(self.ll,self.sheet_max_height_left,0.6,0)[0:2]

			if self.direction == "RIGHT":
				self.o,self.image = animation(self.o,self.sheet_max_height_right,0.6,0)[0:2]


	def status(self):
		if self.vel.y >0.8: #0.8
			self.state = "CAENDO"
		elif self.vel.y < 0:
			self.state = "SUBIENDO"
		if self.vel.y > 0.8 or self.vel.y <0: #0.8
			self.not_ground = True

		if self.not_ground:
			
			if -1.4 <= self.vel.y and self.vel.y<= 0.2: #(0.6)Varia con la gravedad ATENCION!!!!!!!
				self.state = "IDLE VERTICAL"
		elif self.vel.x == 0:
			self.state = "IDLE HORIZONTAL"
	def movement_x(self,velx):
		
		self.rect.x+=velx

		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		if hits:
			
			if velx>0:
				self.rect.right = hits[0].rect.left
				
			if velx<0:
				self.rect.left= hits[0].rect.right
			
	def gravity(self):
		
		self.vel.y +=  self.gravedad
		if self.vel.y >= self.vel_y_max:
			self.vel.y = self.vel_y_max
		self.rect.y += self.vel.y

	def collide_detection_y_axis(self):
		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		

		if hits:
			self.not_ground = False 
			#IMPORTante
			
			if self.rect.bottom<hits[0].rect.bottom:
				
				self.vel.y = 0

				self.rect.bottom = hits[0].rect.top
				
				
				
			if self.rect.top>hits[0].rect.top:
				self.vel.y = 0
				self.rect.top = hits[0].rect.bottom
				

				
	def saber_attack(self):
		
		if self.time_saber +100 < pg.time.get_ticks():
			
			self.is_attacking_saber = True
			self.attack_saber = SaberAttack(self)
			self.game.all_sprites.add(self.attack_saber)



			
	def attack_saber_comprobation(self):	
		

		if self.is_attacking_saber:
			self.state = "ATTACKING_SABER"

			self.time_saber=pg.time.get_ticks()
			
			self.attack_saber.rect.left = self.rect.right + 5
			self.attack_saber.rect.centery = self.rect.centery
			if self.attack_saber.final < pg.time.get_ticks():
				self.k = 0
				self.l = 0
				self.attack_saber.kill()

				self.is_attacking_saber =False
	def buster_attack(self):
		if self.time_buster +50 < pg.time.get_ticks():
			
			self.attack_buster = BusterAttack(self,self.direction)
			self.game.buster_bullets.add(self.attack_buster)
			self.is_attacking_buster = True

	def attack_buster_comprobation(self):	
			

		if self.is_attacking_buster:
			self.state = "ATTACKING_BUSTER"

			self.time_saber=pg.time.get_ticks()
			
			
			if self.attack_buster.final < pg.time.get_ticks():
				self.p = 0
				self.q = 0

				self.is_attacking_buster =False
		if self.game.buster_bullets:
			bullet = pg.sprite.groupcollide(self.game.buster_bullets,self.game.platforms,True,False)
			if self.attack_buster.rect.x > self.rect.x +700:
				self.attack_buster.kill()
		
		
		
class Platform(pg.sprite.Sprite):
	def __init__(self,x,y,w,h,text):
		pg.sprite.Sprite.__init__(self)
		"""self.image = pg.Surface((w,h))
		self.image.fill(color)"""
		self.image = pg.image.load(text)
		self.image = pg.transform.scale(self.image,(w,h))
		self.image = self.image.convert()

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.hitbox = self.rect

class Box(pg.sprite.Sprite):
	def __init__(self,x,y,w,h,color):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(color)
		

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


		
def animation(c,group,velocidad,frame_iteracion):
	c+=0.1666666667
	
	k = c // velocidad
	k = int(k)
	if len(group) == 1:
		k = 0
	else:
	
		if k == len(group):
				c = frame_iteracion*velocidad
				k=frame_iteracion
	image = group[k]
	rect = image.get_rect()
	
	

	return c,image,rect


def load_sheet(sheet,reverse,x,weight,height,n_sprites): 
	"""archivo,reverso,inicio = 0,ancho=50,alto"""
	image = sheet

	
	sprite_list = []
	for a in range(0,n_sprites):
		x -= weight
		ground = pg.Surface((50,height))
		ground.blit(image,(x,-5))
		ground.set_colorkey(BLACK)
		ground = pg.transform.scale2x(ground)
		if reverse:
			ground = pg.transform.flip(ground,True,False)
		ground = ground.convert()
		sprite_list.append(ground)
	return sprite_list

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

def collided(this,other):
    return this.hitbox.colliderect(other.hitbox)

def collided_1(this,other,lmao =False):
    return this.rect_ground_detector.colliderect(other.rect)

def function_1(function):

	return function