#!/usr/bin/python

import math
import pygame
from shadow import *
from pygame.locals import *
import polygons

polygons = polygons.polygons


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

newpoly = []

while runme:
    for event in pygame.event.get():
        if event.type == QUIT:
            runme = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                runme = False
            if event.key == K_RETURN:
                polygons.append(newpoly)
                pygame.draw.polygon(polysurf, white, newpoly, 0)
                newpoly = []
            if event.key == K_s:
                with open("polygons.py","w") as f:
                    f.write("polygons = ")
                    f.write(repr(polygons))

        if event.type == MOUSEBUTTONDOWN:
            point = pygame.mouse.get_pos()
            newpoly.append(point)
            

    screen.blit(polysurf, (0,0))
    light = pygame.mouse.get_pos()

    ### draw shadows
    #shadows.fill((0, 0, 0, 0))
    #for p in polygons:
    #    for t in shadows(p, light, 500 ):
    #        pygame.draw.polygon(shadows, (0,0,255,255), t, 0)

    ### draw active edges
    for p in filter(ccw, edges2(polygons, light)):
        pygame.draw.line(screen,(255,0,0), 
                (p[0][0] + light[0], p[0][1] + light[1]) , 
                (p[1][0] + light[0], p[1][1] + light[1]),3)


    pygame.draw.circle(screen, (0,255,0), light, 10, 2) 
    screen.blit(shadows, (0,0))

    # show newpoly
    if len(newpoly) > 0 : pp = newpoly[0]
    for p in newpoly:
        pygame.draw.line(screen,(255,0,0), pp,p)
        pp = p
        

    pygame.display.flip()
    clock.tick(50)
    counter+=1
    if not counter % 20 : print(clock.get_fps())

