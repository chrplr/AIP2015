#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Draw four yellow dots on a pygame window
"""

import pygame
import sys
import math

WINDOW_DIMENSIONS = (400,300)
BACKGROUND_COLOR = (0,0,0)
DISPLAY_DURATION = 2000
SIDE_CIRCLES = {'color': (255,255,0),
                'radius': 5,
                'initial_angle': -math.pi / 2,
                'number': 7,
                'distance_from_center': 100}

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

def positions_many_centered_shapes(surface, start_angle,number_of_shapes,how_far):
    """computes the positions of n positions evenly distributed
       at a given distance from the center of a surface
       """
    center=[side/2 for side in surface.get_size()]
    positions=list()
    for dot in range(0,number_of_shapes):
        angle = start_angle + 2 * math.pi * dot / number_of_shapes
        projection = [math.cos(angle), math.sin(angle)]
        relative_positions=[int(round(how_far * circle)) for circle in projection]
        coordinates=[width + height for width, height in zip(center, relative_positions)]
        positions.append(coordinates)
    return positions

def main():

    # preparation
    initialization()

    MY_WINDOW = open_a_window(WINDOW_DIMENSIONS)

    apply_background_color(MY_WINDOW, BACKGROUND_COLOR)

    SIDE_CIRCLES_CENTERS = positions_many_centered_shapes(MY_WINDOW,
                                        SIDE_CIRCLES['initial_angle'],
                                        SIDE_CIRCLES['number'],
                                        SIDE_CIRCLES['distance_from_center'])

    for center in SIDE_CIRCLES_CENTERS:
        pygame.draw.circle(MY_WINDOW, SIDE_CIRCLES['color'], center, SIDE_CIRCLES['radius'])

    pygame.display.flip()
    pygame.time.wait(2000)


    close_everything_properly()

if __name__ == '__main__':
    main()
