#!/usr/bin/python

import math
import pygame
from random import randint 
from pygame.locals import *

def main():

    # Initialise screen
    pygame.init()
    dungeon = pygame.image.load('dungeon.jpg')
    screensize = dungeon.get_size()
    screen = pygame.display.set_mode(screensize, SRCALPHA)
    pygame.display.set_caption('Python alpha-test')

    # Generate darkness (double screen size)
    darksize = list(i*2 for i in screensize)
    darkness = pygame.Surface(darksize, SRCALPHA)
    darkness.fill((0, 0, 0))
    darkrect = darkness.get_rect()

    lightrect = Rect(0,0,200,200)
    lightrect.center = darkrect.center
    for i in range(250,0,-10):
        pygame.draw.ellipse(darkness, (0,0,0,i), lightrect, 0)
        lightrect = lightrect.inflate(-2,-2)
    
    darkness.convert_alpha()

    clock = pygame.time.Clock()
    counter = 0

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        ####

        screen.blit(dungeon,(0,0))
        cx,cy = pygame.mouse.get_pos()
        screen.blit(darkness,(cx-darkrect.centerx,cy-darkrect.centery))
        pygame.display.flip()
        clock.tick(100)
        counter+=1
        if not counter % 20 : print(clock.get_fps())


if __name__ == '__main__': main()

