#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Template for pygame programs
   Thanks to Juliette
"""

import pygame
import sys

WINDOW_DIMENSIONS = (400,300)
WINDOW_BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 2000

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
    pygame.display.flip()
    pygame.time.wait(2000)
    close_everything_properly()

if __name__ == '__main__':
    main()
