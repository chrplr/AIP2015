
#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Use pygame to display a window
with a rotating cross spangled rotating background
"""

# importing useful modules
import sys
import pygame


# defining constants
WINDOW_SIZE = (400,300)
WINDOW_COLOR = (0,0,0)

SIDE_CIRCLES_COLOR = (255,255,0)
SIDE_CIRCLES_RADIUS = 5
SIDE_CIRCLES_CENTERS = [(280, 150), (200, 230), (120, 150), (200, 70)]

CENTRAL_CIRCLE_CENTER = (200,150)
CENTRAL_CIRCLE_COLORS = [(0,255,0),(255,0,0)]
CENTRAL_CIRCLE_RADIUS = 3

CROSS_TILE_SIZE = (30,30)
CROSS_TILE_COLOR = (0,0,0)
CROSS_COLOR = (0,0,255)
CROSS_RECTANGLES = [(8,14,14,2),(14,8,2,14)]

BACKGROUND_SIZE = (210,210)
BACKGROUND_COLOR = (0,0,0)

ANGLE_MAX = 2000
ANGLE_STEP = 1

def initialization():
    """initialize the different modules wihtin pygame"""
    pygame.init()

def open_a_window(dimensions):
    """actually opens a pygame surface (i.e. a window) with given dimensions
       returns the surface object
    """
    the_window = pygame.display.set_mode(dimensions)
    return the_window

def apply_background_color(surface,color):
    """apply the background color on the whole surface"""
    surface.fill(color)

def make_surface(surface_size,surface_color):
    the_surface = pygame.Surface(surface_size)
    the_surface.fill(surface_color)
    return the_surface

def centerize(surface,window):
    surface_position = surface.get_rect()
    surface_position.center = window.get_rect().center
    return surface_position

def close_everything_properly():
    """close the pygame window and clean afterwards"""
    pygame.quit()
    sys.exit()

def main():
    initialization()
    MY_WINDOW = open_a_window(WINDOW_SIZE)
    apply_background_color(MY_WINDOW, WINDOW_COLOR)


    BACKGROUND = make_surface(BACKGROUND_SIZE, BACKGROUND_COLOR)

    CROSS_TILE = make_surface(CROSS_TILE_SIZE, CROSS_TILE_COLOR)
    for r in CROSS_RECTANGLES:
        pygame.draw.rect(CROSS_TILE,CROSS_COLOR,r)

    for horizontal_position in range(0, BACKGROUND.get_width(), CROSS_TILE.get_width()):
        for vertical_position in range(0, BACKGROUND.get_height(), CROSS_TILE.get_height()):
            BACKGROUND.blit(CROSS_TILE, (horizontal_position, vertical_position))

    index_color = 0

    for degres in range(0,ANGLE_MAX,ANGLE_STEP):
        MY_ROTATED_BACKGROUND = pygame.transform.rotate(BACKGROUND, degres)

        MY_ROTATED_BACKGROUND_POSITION = centerize(MY_ROTATED_BACKGROUND, MY_WINDOW)

        apply_background_color(MY_WINDOW, WINDOW_COLOR)

        MY_WINDOW.blit(MY_ROTATED_BACKGROUND, MY_ROTATED_BACKGROUND_POSITION)

        for center in SIDE_CIRCLES_CENTERS:
            pygame.draw.circle(MY_WINDOW, SIDE_CIRCLES_COLOR, center, SIDE_CIRCLES_RADIUS)

        if not degres%100:
            index_color = 1 - index_color

        pygame.draw.circle(MY_WINDOW, CENTRAL_CIRCLE_COLORS[index_color], MY_WINDOW.get_rect().center, CENTRAL_CIRCLE_RADIUS)

        pygame.display.flip()

    close_everything_properly()


if __name__ == '__main__':
    main()
