#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
import os
import random

WINDOW_SIZE = (600,300)
WINDOW_BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 3000

# petite astuce pour forcer la position de la fenetre sur votre ecran
WINDOW_POSITION_ON_SCREEN = (0, 10)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % WINDOW_POSITION_ON_SCREEN

def initialization():
    """initialize the different modules within pygame"""
    pygame.init()

def open_a_window(dimensions):
    """actually open a pygame surface (i.e. a window) with given dimensions
       return the surface object
    """
    the_window = pygame.display.set_mode(dimensions)
    return the_window

def apply_background_color(surface,color):
    """apply the background color on the whole surface"""
    surface.fill(color)

def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_SIZE)
    apply_background_color(MY_WINDOW, WINDOW_BACKGROUND_COLOR)
    pygame.display.flip()

    pygame.draw.circle(MY_WINDOW, (255,255,255), (300,150), 20)
    pygame.time.wait(1000 + random.randint(0,2000))
    pygame.display.flip()

    t0 = pygame.time.get_ticks()
    pygame.event.clear()

    while pygame.time.get_ticks() < t0 + DISPLAY_DURATION:
        event_stack = pygame.event.get()
        delay = pygame.time.get_ticks() - t0

        if event_stack: # if the event stack is not empty
            print(type(event_stack))
            for event in event_stack:
                print(event)
                if event.type == KEYDOWN and event.key == K_SPACE:
                    print("Reaction time = " + str(delay) + " milliseconds")
                    break

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
