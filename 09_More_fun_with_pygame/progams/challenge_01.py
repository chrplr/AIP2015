#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Draw four yellow dots on a pygame window
"""

import pygame
import sys

WINDOW_DIMENSIONS = (400,300)
BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 2000
SIDE_CIRCLES_COLOR = (255,255,0)
SIDE_CIRCLES_RADIUS = 5
SIDE_CIRCLES_CENTERS = [(300, 150), (200, 250), (100, 150), (200, 50)]

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

    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)

    apply_background_color(MY_WINDOW, BACKGROUND_COLOR)

    for center in SIDE_CIRCLES_CENTERS:
        pygame.draw.circle(MY_WINDOW, SIDE_CIRCLES_COLOR, center, SIDE_CIRCLES_RADIUS)

    pygame.display.flip()
    pygame.time.wait(2000)


    close_everything_properly()

if __name__ == '__main__':
    main()
