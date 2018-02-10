import pygame
pygame.init()

BLACK = 0, 0, 0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
WHITE = 255,255,255



class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y, speed):
        super(pygame.sprite.Sprite, self).__init__()

        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y):
        super(pygame.sprite.Sprite, self).__init__()

        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collision(self, player):

        if self.rect.colliderect(player.rect):

            if player.move_x > 0:
                # moving right
                player.rect.right = self.rect.left

            elif player.move_x < 0:
                #moving left
                player.rect.left = self.rect.right

            elif player.move_y < 0:
                # moving up
                player.rect.top = self.rect.bottom

            elif player.move_y >0:
                #moving down
                player.rect.bottom = self.rect.top


class Game():

    def __init__( self, x, y, fps ):

        #initialize
        self.x = x
        self.y = y

        self.screen = pygame.display.set_mode( ( x,y ) )
        self.running = True

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.fpsFont = pygame.font.SysFont('mono', 22)

        self.player = Player(BLUE, 50, 50, 400, 400, 5)
        self.wall = wall = Wall(1220,40,0,0)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Get keydowns and adjust player speed  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move_x += self.player.speed
                if event.key == pygame.K_LEFT:
                    self.player.move_x -= self.player.speed
                if event.key == pygame.K_UP:
                    self.player.move_y -= self.player.speed
                if event.key == pygame.K_DOWN:
                    self.player.move_y += self.player.speed

            # Get keyups and resets vector
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.move_x = 0
                if event.key == pygame.K_LEFT:
                    self.player.move_x = 0
                if event.key == pygame.K_UP:
                    self.player.move_y = 0
                if event.key == pygame.K_DOWN:
                    self.player.move_y = 0

    def draw_rects(self):
        # draw all the images to the screen
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.screen.blit(self.wall.image, (self.wall.rect.x, self.wall.rect.y))     

    def draw_fps(self):
        #Displays an fps counter
        text = "FPS: " + str(round(self.clock.get_fps()))
        self.renderedFPS = self.fpsFont.render(text, True, BLACK)
        self.screen.blit(self.renderedFPS, (0 , self.y - self.y / 20))

    def mainloop(self):
        #Game loop
        while self.running == True:

            # Event loop
            self.on_event()

            # Game Logic
            self.player.move()
            self.wall.collision(self.player)


            # Draw everything
            self.screen.fill( WHITE )
            self.draw_fps()
            self.draw_rects()
            pygame.display.flip()

            # Limit FPS to 60
            self.clock.tick(self.fps)


if __name__ == "__main__":  

    game = Game(1220, 720, 60)
    game.mainloop()