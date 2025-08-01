# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 
    Player.containers = (updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
       
       updatable.update(dt)
       
       screen.fill('black')
       for object in drawable:
           object.draw(screen)
       
       pygame.display.flip()

       # wait 1/60s between ticks
       dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
