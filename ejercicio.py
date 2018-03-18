import pygame as pg 

pg.init()

ventana = pg.display.set_mode((800,600))
pg.display.set_caption("test")

image = pg.image.load("Sprites\zerox3.gif")

def wdd():
	x = 5
	y = 7
	z = 3
	return x,y,z

def get_image(sheet, x, y, xf, yf):
        
        width = xf - x
        height = yf - y
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0))

        image = pg.transform.scale2x(image)

        image = image.convert()

        return image

spritelist_2 =[]
"""
image_1 = get_image(image,4,407,43,458)
image_2 = get_image(image,52,405,89,456)
image_3 = get_image(image,98,404,131,454)
image_4 = get_image(image,146,405,179,455)"""

image_1 =  get_image(image,6,201,42,243)
spritelist_2.append(image_1)

image_1 =  get_image(image,47,201,81,243)
spritelist_2.append(image_1)

image_1 =  get_image(image,91,200,136,242)
spritelist_2.append(image_1)

image_1 =  get_image(image,152,198,200,241)
spritelist_2.append(image_1)

image_1 =  get_image(image,283,191,362,242)
spritelist_2.append(image_1)

image_1 =  get_image(image,376,198,455,239)
spritelist_2.append(image_1)

image_1 =  get_image(image,464,204,543,238)
spritelist_2.append(image_1)

image_1 =  get_image(image,552,203,627,237)
spritelist_2.append(image_1)

image_1 =  get_image(image,635,203,704,237)
spritelist_2.append(image_1)

image_1 =  get_image(image,716,205,760,239)
spritelist_2.append(image_1)

image_1 =  get_image(image,771,197,815,239)
spritelist_2.append(image_1)


"""
spritelist_2.append(image_1)
spritelist_2.append(image_2)
spritelist_2.append(image_3)
spritelist_2.append(image_4)"""
x = 0
sprite_list = []

for a in range(0,13):
	x -= 50
	ground = pg.Surface((50,50))
	ground.blit(image,(x,-5))
	ground = pg.transform.scale2x(ground)
	ground = ground.convert()
	sprite_list.append(ground)

status = "IDLE"


ground.blit(image,(-550,-5))
rect=ground.get_rect()


font = pg.font.SysFont(None,40)


ground.convert()
ground = pg.transform.scale2x(ground)
rect=ground.get_rect()

d = 0
c = 0
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

time = pg.time.Clock()
bol = False

while True:
	time.tick(60)
	pg.display.flip()
	ventana.fill((0,0,0))
	d,imagenes,recta = animation(d,spritelist_2,0.5,0)
	a,b = wdd()[0:2]
	c = wdd()[2]
	print "lul", c
	print a,b
	ventana.blit(imagenes,(200,200))
	if bol:
		c = animation(c,sprite_list,ventana)

	
	

	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_x:
				bol = True

