
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame to display the motion induced blindness stimuli
see http://www.michaelbach.de/ot/mot-mib/
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_DIMENSIONS = (400,300)
BACKGROUND_COLOR = (0,0,0)
CROSS_COLOR = (0,0,255)
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

def make_background_image(image_path):
    """"get a pygame surface from an image file"""
    the_image = pygame.image.load(image_path).convert()
    return the_image

def centerize(surface,window):
    surface_position = surface.get_rect()
    surface_position.center = window.get_rect().center
    return surface_position

def 

def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)

    MY_IMAGE = load_an_image(PYTHON_LOGO_PATH)

    for degres in range(0,ANGLE_MAX,ANGLE_STEP):
        MY_ROTATED_IMAGE = pygame.transform.rotate(MY_IMAGE, degres)

        MY_ROTATED_IMAGE_POSITION = centerize(MY_ROTATED_IMAGE, MY_WINDOW)

        clean_the_window(MY_WINDOW, BACKGROUND_COLOR)

        MY_WINDOW.blit(MY_ROTATED_IMAGE, MY_ROTATED_IMAGE_POSITION)
        pygame.display.flip()


    # finally we close everything properly
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
