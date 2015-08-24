#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Time-stamp: <2013-09-16 21:05 christophe@pallier.org>


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
rtfile = file("reaction-times.csv", "w")
for r in reaction_times:
    rtfile.write(str(r)+"\n")
rtfile.close()

def mean(l):
    sum = 0.0
    for x in l:
        sum = sum + x
    return sum/len(l)

import math

def stderr(l):
    m = mean(l)
    n = len(l)
    sumsq = 0.0
    for x in l:
        sumsq = sumsq + (x - m)**2
    return math.sqrt(sumsq/n)/math.sqrt(n)

def tmean(l, percentage=0.25):
    sl = sorted(l)
    trimmed = int(len(l) * percentage/2.0)
    clean = []
    for i in range(trimmed, len(l)-1-trimmed):
        clean.append(sl[i])
    return (mean(clean), stderr(clean))


print("Trimmed mean = " + str(tmean(reaction_times)))

pygame.quit()



                
        

    
