# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 1
# Video link: https://www.youtube.com/watch?v=uWvb3QzA48c
# Project setup

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        

        self.player = Player(self)
        self.all_sprites.add(self.player)

        p1 = Platform(0,HEIGHT-40,WIDTH,40)
        self.all_sprites.add(p1)

        p2 = Platform(150,400,200,50)
        self.all_sprites.add(p2)

        

        p4 = Platform(400,HEIGHT-200,20,300)
        self.all_sprites.add(p4)

        self.platforms.add(p4)
        
        self.platforms.add(p2)
        self.platforms.add(p1)
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
        #check if player hits platform - only if falling
        if self.player.state == "CAENDO":
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                print self.player.state
                print self.player.acc.y
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top +1
                
                

        if self.player.state == "SUBIENDO":
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                print self.player.state
                print self.player.acc.y
                self.player.vel.y = 0
                self.player.rect.top = 0
        print self.player.rect.top                
                

       
        

        """hits = pg.sprite.spritecollide(self.player,self.platforms,False)
        if hits:
            if self.player.vel.y > 0:
                self.player.pos.y = hits[0].rect.top +1
                self.player.vel.y = 0

            if self.player.vel.y < 0:
                self.player.rect.top = hits[0].rect.bottom
                self.player.vel.y = 0

            if self.player.vel.x > 0:
                self.player.rect.right = hits[0].rect.left
                self.player.vel.x = 0"""


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

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
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