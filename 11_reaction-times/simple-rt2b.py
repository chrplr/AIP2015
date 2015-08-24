#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Time-stamp: <2013-09-16 18:54 christophe@pallier.org>

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

pygame.time.delay(1000)

pygame.draw.circle(screen, WHITE, (W/2, H/2), 4)
pygame.display.update()

t0 = pygame.time.get_ticks()
pygame.event.clear()
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.MOUSEBUTTONDOWN:
        rt = pygame.time.get_ticks() - t0
        print(rt)
        break

screen.fill(BLACK)
pygame.display.update()

pygame.time.wait(1000)

pygame.quit()



                
        

    
