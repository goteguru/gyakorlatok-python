#!/usr/bin/python

import math
import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption('proba')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))


    # turtle
    turtle = pygame.image.load('turtle.png').convert()

    # Display some text
    print (pygame.font.match_font('arial'))
    font = pygame.font.Font(None, 36)
    text = font.render("éáőúűóüöí", 1, (10, 80, 110))
    textpos = text.get_rect()
    textpos.center = background.get_rect().center
    shadow = font.render("éáőúűóüöí", 1, (10, 10, 10))
    shadowpos = textpos.copy()
    shadowpos.center = (shadowpos.centerx + 2, shadowpos.centery + 2)
    background.blit(shadow, shadowpos)
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    print("flags:",screen.get_flags())

    clock = pygame.time.Clock()

    tx,ty = 0,0
    dx = 0
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            if event.type == KEYDOWN:
                if event.key == K_LEFT:     tx -= 1
                elif event.key == K_RIGHT:  tx += 1
                elif event.key == K_UP:     ty -= 1
                elif event.key == K_DOWN:   ty += 1

        screen.blit(background, (0, 0))
        #screen.blit(background, (math.sin(dx)*100.0, 0))
        dx = (dx+0.01) 

        screen.blit(turtle, (tx,ty) )

        pygame.display.flip()
        print(clock.tick(20))


if __name__ == '__main__': main()

