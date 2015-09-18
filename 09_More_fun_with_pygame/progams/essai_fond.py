
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame to display a window
with a rotatin cross spangled rotating background
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_DIMENSIONS = (400,300)
WINDOW_COLOR = (0,0,0)

CROSS_SIZE = (40,40)
CROSS_BACKGROUND_COLOR = (255,255,255)


BACKGROUND_SIZE = (300,300)
BACKGROUND_COLOR = (110,110,110)
BACKGROUND_POSITION = (0,0)

DISPLAY_DURATION = 2000


def initialization():
    """initialize the different modules wihtin pygame"""
    pygame.init()

def open_a_window(dimensions):
    """actually opens a pygame surface (i.e. a window) with given dimensions
       returns the surface object
    """
    the_window = pygame.display.set_mode(dimensions)
    return the_window

def clean_the_window(surface,color):
    """apply the background color on the whole window"""
    surface.fill(color)

def make_surface(surface_size,surface_color):
    the_surface = pygame.Surface(surface_size)
    the_surface.fill(surface_color)
    return the_surface

def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)
    clean_the_window(MY_WINDOW, WINDOW_COLOR)


    BACKGROUND = make_surface(BACKGROUND_SIZE, BACKGROUND_COLOR)

    CROSS = make_surface(CROSS_SIZE, CROSS_BACKGROUND_COLOR)
    pygame.draw.rect(CROSS, (0,0,255), (18,6,4,28))
    pygame.draw.rect(CROSS, (0,0,255), (6,18,28,4))


    BACKGROUND.fill((255,0,0))
    for x in range(0,40*7,40):
        for y in range(0,40*7,40):
            BACKGROUND.blit(CROSS,(x,y))

    MY_WINDOW.blit(BACKGROUND, BACKGROUND_POSITION)

    pygame.display.flip()
    pygame.time.wait(DISPLAY_DURATION)


    # finally we close everything properly
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
