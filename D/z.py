import pygame
import time
from pygame.locals import *

class Snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resourses/block.jpg").convert()
        self_x = 100
        self_y = 100
        block_x,block_y = 100,100

    def draw(self):
        self.parent_screen.blit(self.block,(self.x,self.y))

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill((110,110,5))

    def run(self):
        pass

def draw_block():
    surface.fill((110,110,5))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()




    pygame.init()


    surface = pygame.display.set_mode((1000,500))
    surface.fill((110,110,5))



    pygame.display.flip()

    time.sleep(5)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running == False
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block
            elif event.type ==QUIT:
                running == False






