#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Display a central dot alternating between two colors
"""

import pygame
import sys

WINDOW_DIMENSIONS = (400,300)
WINDOW_BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 1000
CENTRAL_CIRCLE_CENTER = (200,150)
CENTRAL_CIRCLE_RADIUS = 100
CENTRAL_CIRCLE_COLORS = [(0,255,0),(255,0,0)]
NUMBER_OF_ALTERNATIONS = 4

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
    apply_background_color(MY_WINDOW, WINDOW_BACKGROUND_COLOR)

    # and the alternating dot
    for color in CENTRAL_CIRCLE_COLORS * NUMBER_OF_ALTERNATIONS:
        pygame.draw.circle(MY_WINDOW, color, CENTRAL_CIRCLE_CENTER, CENTRAL_CIRCLE_RADIUS)
        pygame.display.flip()
        pygame.time.wait(DISPLAY_DURATION)

    close_everything_properly()

if __name__ == '__main__':
    main()
