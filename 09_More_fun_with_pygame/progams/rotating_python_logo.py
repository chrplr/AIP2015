
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame to display a window
Put an image within and then rotate it
Exercice: use the MY_IMAGE.get_rect().center so that the
image does not wiggle about while rotating
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_DIMENSIONS = (400,300)
BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 2000
PYTHON_LOGO_PATH = '../images/Python-logo-notext.svg.png'
ANGLE_MAX = 1000
ANGLE_STEP = 2

def initialization():
    """initialize the different modules wihtin pygame"""
    pygame.init()

def open_a_window(dimensions):
    """actually opens a pygame surface (i.e. a window) with given dimensions
       returns the surface object
    """
    the_window=pygame.display.set_mode(dimensions)
    return the_window

def clean_the_window(surface,color):
    """apply the background color on the whole window"""
    surface.fill(color)

def load_an_image(image_path):
    the_image = pygame.image.load(image_path).convert()
    return the_image


def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)
    
    MY_IMAGE=load_an_image(PYTHON_LOGO_PATH)
    MY_IMAGE_POSITION=MY_IMAGE.get_rect()

    for degres in range(0,ANGLE_MAX,ANGLE_STEP):
        MY_ROTATED_IMAGE=pygame.transform.rotate(MY_IMAGE,degres)
        clean_the_window(MY_WINDOW,BACKGROUND_COLOR)
        MY_WINDOW.blit(MY_ROTATED_IMAGE,MY_IMAGE_POSITION)
        pygame.display.flip()


    # finally we close everything properly
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

for degres in range(0,2000,1):
    MY_ROTATED_IMAGE=pygame.transform.rotate(MY_IMAGE,degres)
    MY_WINDOW.blit(MY_ROTATED_IMAGE,MY_IMAGE_POSITION)
    pygame.display.flip()
