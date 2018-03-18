import pygame as pg
import random
from settings import *
from level import *
from sprites import *
from pygame.locals import *
class Game:
    def __init__(self):
        # initialize game window, etc   
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT),pg.RESIZABLE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.player = Player(self)
        self.background = pg.image.load("Sprites\dackground.png")
        self.background = pg.transform.scale(self.background,(WIDTH,HEIGHT))
        self.background = self.background.convert()
        

        

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player_things = pg.sprite.Group()
        self.buster_bullets = pg.sprite.Group()

        self.first_level = Level(self)
        """self.first_level.map_design_1()"""
        self.first_level.map_design_2()

        self.player = Player(self)
        

        self.player_things.add(self.player)
        
        self.run()


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)  
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Game Loop - Update
        
        self.all_sprites.update()
        self.player_things.update()
        self.buster_bullets.update()
        #check if player hits platform - only if falling
        


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                    self.player.jump_wall()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:
                    self.player.saber_attack()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    self.player.buster_attack()
                    

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.background,(0,0))
        self.all_sprites.draw(self.screen)
        self.player_things.draw(self.screen)
        self.buster_bullets.draw(self.screen)
        pg.draw.rect(self.screen,Color('red'),self.player.rect,1)
        pg.draw.rect(self.screen,Color('blue'),self.player.hitbox,1)
        pg.draw.rect(self.screen,Color('green'),self.player.rect_ground_detector,1)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    
    g.new()
    g.show_go_screen()

pg.quit()