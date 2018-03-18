
# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 1
# Video link: https://www.youtube.com/watch?v=uWvb3QzA48c
# Project setup

import pygame as pg
from settings import *
from sprites import *
import random


class LevelEditor:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.posicion = pg.mouse.get_pos()
        self.cursor_hitbox = Box(self.posicion[0],self.posicion[1],2,2,RED)
        self.status = "IDLE"
        self.file = open ('txt\prueba3.txt','a')
        self.text = "none"

    def new(self):
        # start a new game
        self.ground_group = pg.sprite.Group()
        self.groundv2_group = pg.sprite.Group()


        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        
        self.all_sprites.add(self.cursor_hitbox)
        self.Platform_creator = Platform(0,0,50,50,"Sprites\ground16.png")
        self.Platform_creator_2 = Platform(50,0,50,50,"Sprites\groundv2.png")

        self.platforms.add(self.Platform_creator)
        self.platforms.add(self.Platform_creator_2)

        self.all_sprites.add(self.Platform_creator)
        self.all_sprites.add(self.Platform_creator_2)
        
       

        
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
        self.click_izquierdo = pg.mouse.get_pressed()[0]
        self.click_derecho = pg.mouse.get_pressed()[2]
        self.posicion = pg.mouse.get_pos()
        self.cursor_hitbox.rect.centerx = self.posicion[0]
        self.cursor_hitbox.rect.centery = self.posicion[1]
        """
        if self.status == "IDLE":
            if self.click_izquierdo:
                if pg.sprite.collide_rect(self.cursor_hitbox,self.Platform_creator):
                    self.status = "platform_added"
                    self.new_platform =Platform(self.posicion[0],self.posicion[1],50,50,GREEN)"""
                
                

        if self.status == "platform_added":
            self.x = self.posicion[0]-(self.posicion[0] % 50)
            self.y = self.posicion[1]-(self.posicion[1] % 50) 
            

            self.new_platform.rect.left = self.x
            self.new_platform.rect.top = self.y
            self.all_sprites.add(self.new_platform)
            
                

        #check if player hits platform - only if falling

    def save(self):
        self.all = [self.ground_group,self.groundv2_group]
        for groups in self.all:
            for sprite in groups:
                if self.all[0] == groups:
                    self.file.write("Sprites\ground16.png")
                    self.file.write(" ")
                if self.all[1] == groups:
                    self.file.write("Sprites\groundv2.png")
                    self.file.write(" ")
                x = str(sprite.rect.x)
                y = str(sprite.rect.y)
                
                self.file.write(x)
                self.file.write(" ")
                self.file.write(y)
                self.file.write(" ")
        
        


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if self.status == "IDLE":
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pg.sprite.collide_rect(self.cursor_hitbox,self.Platform_creator):
                            self.status = "platform_added"
                            self.new_platform =Platform(self.posicion[0],self.posicion[1],50,50,"Sprites\ground16.png")
                            self.text = "fig1"

                        if pg.sprite.collide_rect(self.cursor_hitbox,self.Platform_creator_2):
                            self.status = "platform_added"
                            self.new_platform =Platform(self.posicion[0],self.posicion[1],50,50,"Sprites\groundv2.png")
                            self.text = "fig2"

            if self.status == "platform_added":
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if self.text == "fig1":

                            self.platform_put = Platform(self.new_platform.rect.left,self.new_platform.rect.top,50,50,"Sprites\ground16.png")
                            self.all_sprites.add(self.platform_put)
                            self.ground_group.add(self.platform_put)

                        if self.text == "fig2":

                            self.platform_put = Platform(self.new_platform.rect.left,self.new_platform.rect.top,50,50,"Sprites\groundv2.png")
                            self.all_sprites.add(self.platform_put)
                            self.groundv2_group.add(self.platform_put)


            if self.status == "platform_added":
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        for plat in self.all_sprites:
                            if pg.sprite.collide_rect(self.cursor_hitbox,plat):
                                plat.kill()

            if self.status == "platform_added":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.new_platform.kill()
                        self.status ="IDLE"

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.save()
                    print 'p'
                        


            """if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:"""

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

g = LevelEditor()
g.show_start_screen()
while g.running:

    g.new()
    g.show_go_screen()

pg.quit()