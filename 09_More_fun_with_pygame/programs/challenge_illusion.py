
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame to display a window
Put an image within and then rotate it nicely in the center
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_DIMENSIONS = (400,300)
BACKGROUND_COLOR = (0,0,0)

CROSS_COLOR = (0,0,255)

SIDE_CIRCLES_COLOR = (255,255,0)
SIDE_CIRCLES_CENTERS = [(150,100), (250,100), (150,200), (250,200)]
SIDE_CIRCLES_RADIUS = 5

CENTRAL_CIRCLE_COLORS = [(0,255,0), (255,0,0)]
CENTRAL_CIRCLE_CENTER = (200,150)
CENTRAL_CIRCLE_RADIUS = 3

DISPLAY_DURATION = 2000

ANGLE_MAX = 1000
ANGLE_STEP = 2

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

def centerize(surface,window):
    surface_position = surface.get_rect()
    surface_position.center = window.get_rect().center
    return surface_position




def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)
    clean_the_window(MY_WINDOW, BACKGROUND_COLOR)

    for centers in SIDE_CIRCLES_CENTERS:
        pygame.draw.circle(MY_WINDOW, SIDE_CIRCLES_COLOR, centers, SIDE_CIRCLES_RADIUS)


    for color in CENTRAL_CIRCLE_COLORS:
        pygame.draw.circle(MY_WINDOW, color , CENTRAL_CIRCLE_CENTER, CENTRAL_CIRCLE_RADIUS)
        pygame.display.flip()
        pygame.time.wait(DISPLAY_DURATION)


    # finally we close everything properly
    pygame.quit()
    sys.exit()

"""
    for degres in range(0,ANGLE_MAX,ANGLE_STEP):
        MY_ROTATED_IMAGE = pygame.transform.rotate(MY_IMAGE, degres)

        MY_ROTATED_IMAGE_POSITION = centerize(MY_ROTATED_IMAGE, MY_WINDOW)

        clean_the_window(MY_WINDOW, BACKGROUND_COLOR)

        MY_WINDOW.blit(MY_ROTATED_IMAGE, MY_ROTATED_IMAGE_POSITION)
        pygame.display.flip()
"""




if __name__ == '__main__':
    main()
