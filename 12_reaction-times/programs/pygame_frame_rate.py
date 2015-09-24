#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame.time functions to control the window display duration
"""

import pygame
import sys
import os
import random

WINDOW_DIMENSIONS = (600,300)

# littkle trick to position the pygame window on your screen
WINDOW_POSITION_ON_SCREEN = (0, 10)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % WINDOW_POSITION_ON_SCREEN

WINDOW_BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 2000

FRAME_RATE = 60

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

def close_everything_properly():
    """close the pygame window and clean afterwards"""
    pygame.quit()
    sys.exit()

def main():

    # preparation
    initialization()

    clock = pygame.time.Clock()

    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)
    apply_background_color(MY_WINDOW, WINDOW_BACKGROUND_COLOR)

    pygame.display.flip()
    t0 = pygame.time.get_ticks()

    while pygame.time.get_ticks() < t0 + DISPLAY_DURATION:
        print("delay : " + str(pygame.time.get_ticks() - t0))
        color = [random.randint(0,255) for i in range(0,3)]
        position = [pos/2 for pos in WINDOW_DIMENSIONS]
        pygame.draw.circle(MY_WINDOW, color, position, 20)
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    print("Total delay : " + str(pygame.time.get_ticks() - t0))
    close_everything_properly()

if __name__ == '__main__':
    main()
