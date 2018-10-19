#!/usr/bin/python

import math
import pygame
from shadow import trapezok
from pygame.locals import *


polygons = [ 
    [(10,10),(30,30),(50,30)],
    [(200,200),(330,240),(380,90)],
    [(480,520),(475,410),(400,450)],
    [(300,300),(500,300),(500,330),(340,330),(340,450),(300,450)][::-1],
    ]


screensize = 800, 800
white = (255,255,255)

pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Python shadow test')

polysurf = pygame.Surface(screensize)
polysurf.fill((0, 0, 0))
# draw polys
for p in polygons :
    pygame.draw.polygon(polysurf, white, p, 0)

shadows = pygame.Surface(screensize, SRCALPHA)

#### Main loop ####
runme = True
clock = pygame.time.Clock()
counter = 0

while runme:
    for event in pygame.event.get():
        if event.type == QUIT:
            runme = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                runme = False

    ####

    light = pygame.mouse.get_pos()
    ### draw shadows
    shadows.fill((0, 0, 0, 0))
    for p in polygons:
        for t in trapezok(p, light, 900 ):
            pygame.draw.polygon(shadows, (255,0,0,255), t, 0)

    pygame.draw.circle(screen, (0,255,0), light, 10, 2) 

    screen.blit(polysurf, (0,0))
    screen.blit(shadows, (0,0))
    pygame.display.flip()
    clock.tick(50)
    counter+=1
    if not counter % 20 : print(clock.get_fps())

