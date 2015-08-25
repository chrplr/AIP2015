#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Time-stamp: <2012-09-22 15:38 christophe@pallier.org>

import pygame, random

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
r = screen.get_rect()
W, H = r.width, r.height

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ntrials = 10
reaction_times = []

try:
    for t in range(ntrials):

        waiting_time=random.randint(1000,2000)
        pygame.time.delay(waiting_time)
        pygame.event.clear()
        t0 = pygame.time.get_ticks()

        pygame.draw.circle(screen, WHITE, (W/2, H/2), 4)
        pygame.display.update()

        buttonpressed = False
        while not(buttonpressed):
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    t1 = pygame.time.get_ticks()
                    buttonpressed = True
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                    raise Exception()
        reaction_times.append(t1-t0)

        screen.fill(BLACK)
        pygame.display.update()

except:
    pass

finally:
    saveresults = file('reaction_times.csv','w')
    for t,r in enumerate(reaction_times):
        saveresults.write(str(t) + ", " + str(r) +"\n")
    saveresults.close()
    pygame.quit()











                
        

    
