
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Build a surface and center it, step by step
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_DIMENSIONS = (400,300)
WHITE = (255,255,255)
DISPLAY_DURATION = 2000
PYTHON_LOGO_PATH = '../images/Python-logo-notext.svg.png'

def main():

    # initialize the different modules wihtin pygame
    pygame.init()

    # open a pygame surface (i.e. a window) with given dimensions
    MY_WINDOW = pygame.display.set_mode(WINDOW_DIMENSIONS)

    # prepare a white background
    MY_WINDOW.fill(WHITE)

    # display the white background
    pygame.display.flip()

    # give us time to see it
    pygame.time.wait(DISPLAY_DURATION)

    # load an image and display it on the window top left cornenr using blit
    MY_IMAGE = pygame.image.load(PYTHON_LOGO_PATH).convert()
    MY_WINDOW.blit(MY_IMAGE,(0,0))
    pygame.display.flip()
    pygame.time.wait(DISPLAY_DURATION)

    # get the rectangles of both the window and the image
    MY_WINDOW_POSITION = MY_WINDOW.get_rect()
    MY_IMAGE_POSITION = MY_IMAGE.get_rect()
    print("Initial image rectangle : " + str(MY_IMAGE_POSITION))
    print("Initial image center : " + str(MY_IMAGE_POSITION.center))

    # identify the center of the window
    MY_WINDOW_CENTER = MY_WINDOW_POSITION.center
    print("The window center : " + str(MY_WINDOW_CENTER))

    # then put the center of the image on the center of the window
    MY_IMAGE_POSITION.center = MY_WINDOW_CENTER
    print("Image newly defined center : " + str(MY_IMAGE_POSITION.center))

    # the position of the image has changed !
    print("New image rectangle : " + str(MY_IMAGE_POSITION))
    print("which has changed to accomodate the new center position")

    # now display the image at its centered position
    MY_WINDOW.fill(WHITE)
    MY_WINDOW.blit(MY_IMAGE, MY_IMAGE_POSITION)
    pygame.display.flip()
    pygame.time.wait(DISPLAY_DURATION)


    # finally we close everything properly
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
