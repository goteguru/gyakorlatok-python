#!/usr/bin/python

import math
import pygame
from random import randint 
from pygame.locals import *

def main():
    scrw, scrh = 1024,1024

    # Initialise screen
    pygame.init()
    #screen = pygame.display.set_mode((scrw, scrh), SRCALPHA)
    screen = pygame.display.set_mode((scrw, scrh))
    pygame.display.set_caption('Python speedtest')

    # filled test backgrounds

    # hardware (in GPU) surface 
    hwsurface = pygame.Surface(screen.get_size(), HWSURFACE)
    hwsurface = hwsurface.convert()
    hwsurface.fill((0, 0, 0))

    # standard (in memory) surface 
    memsurface = pygame.Surface(screen.get_size(), SRCALPHA)
    memsurface = memsurface.convert()
    memsurface.fill((0, 0, 0))

    # alpha surface
    alphasurface = pygame.Surface(screen.get_size(), SRCALPHA)
    alphasurface.fill((0, 0, 0))

    # test sprite (turtle)
    teki = pygame.image.load('turtle.png')
    spr_mem = teki
    spr_hw_conv = teki.convert(32,HWSURFACE)
    spr_conv = teki.convert()
    spr_conv.set_colorkey(Color(0,0,0))
    spr_alpha = teki.convert_alpha()   #  <------------ Ez a lényeg

    clock = pygame.time.Clock()
    tx,ty = 0,0
    pause = False
    counter = 0
    number_of_sprites = 2000
    sprite = teki
    background = memsurface
    memoryblit = False

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_SPACE: 
                    pause = not pause

                if event.key == K_a: 
                    print ("memory background")
                    background = memsurface
                if event.key == K_b: 
                    print ("hardware background")
                    background = hwsurface
                if event.key == K_c: 
                    print ("alpha background")
                    background = alphasurface

                if event.key == K_1: 
                    print ("memory sprite, no conversion")
                    sprite = spr_mem
                if event.key == K_2: 
                    print ("hardware sprite")
                    sprite = spr_hw_conv
                if event.key == K_3: 
                    print("memory sprite, with colorkey")
                    sprite = spr_conv
                if event.key == K_4: 
                    print("memory sprite, convert_alpha")
                    sprite = spr_alpha
                
                if event.key == K_m: 
                    memoryblit = not memoryblit
                    print("In memory blit:", memoryblit )

        ### speedtest core ###

        if not pause:
            if memoryblit:
                for i in range(number_of_sprites):
                    background.blit(sprite, (randint(0,scrw), randint(0,scrh)))
                screen.blit(background,(0,0))
            else:
                screen.blit(background,(0,0))
                for i in range(number_of_sprites):
                    screen.blit(sprite, (randint(0,scrw), randint(0,scrh)))

        ####

        pygame.display.flip()
        clock.tick(100)
        counter+=1
        if not pause:
            if not counter % 20 : print(clock.get_fps())


if __name__ == '__main__': main()

