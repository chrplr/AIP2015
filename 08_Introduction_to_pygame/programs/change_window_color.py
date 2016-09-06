#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame to display a window and then
cycle through different background colors
while displaying on standard output the name of the background color
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_DIMENSIONS = (400,300)

MY_COLORS = {'WHITE': (255,255,255),
             'BLUE': (0,0,255),
             'RED': (255,0,0)}

DISPLAY_DURATION = 2000

def initialization():
    """initialize the different modules within pygame"""
    pygame.init()

def open_a_window(dimensions):
    """actually opens a pygame surface (i.e. a window) with given dimensions
       returns the surface object
    """
    the_window=pygame.display.set_mode(dimensions)
    return the_window

def change_the_background_color(surface,color):
    """change the color of the whole surface and display it"""
    surface.fill(color)
    pygame.display.flip()

def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)

    # we use a nice property of dictionaries to iterate through keys and values
    for background_color in MY_COLORS.iteritems():
        change_the_background_color(MY_WINDOW,background_color[1])
        print("now the background color should be " + background_color[0])
        pygame.time.wait(DISPLAY_DURATION)

    # finally we close everything properly
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
