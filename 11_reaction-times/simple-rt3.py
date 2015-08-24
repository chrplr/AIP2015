#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Time-stamp: <2013-09-17 18:41 christophe@pallier.org>


import random, sys

# initialisation de pygame
import pygame
pygame.init()

fullscreen = False
if fullscreen:
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.DOUBLEBUF)
else:
    screen = pygame.display.set_mode((600,400),pygame.DOUBLEBUF)
    
r = screen.get_rect()
W, H = r.width, r.height
pygame.mouse.set_visible(False)

##################################

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(BLACK)
pygame.display.update()

reaction_times = []
NTRIALS = 32

for trial in range(NTRIALS):
    waitingtime = random.randint(1000, 2000)
    pygame.time.delay(waitingtime)

    pygame.draw.circle(screen, WHITE, (W/2, H/2), 4)
    pygame.display.update()

    t0 = pygame.time.get_ticks()
    pygame.event.clear()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            rt = pygame.time.get_ticks() - t0
            print(rt)
            break

    screen.fill(BLACK)
    pygame.display.update()

    reaction_times.append(rt)

# sauvegarde des temps de reaction
rtfile = file("reaction-times_l1.csv", "w")
for r in reaction_times:
    rtfile.write(str(r) + chr(10)) # chr(10) is a newline
rtfile.close()

pygame.quit()



                
        

    
