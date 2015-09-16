#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Change the window background color
"""

import sys
import pygame
from pygame.locals import *

def main():
    pygame.init()

    SURFACE_AFFICHAGE=pygame.display.set_mode((400,300))

    WHITE=(255,255,255)
    BLUE=(0,0,255)


    SURFACE_AFFICHAGE.fill(WHITE)
    pygame.display.flip()

    pygame.time.wait(2000)

    SURFACE_AFFICHAGE.fill(BLUE)
    pygame.display.flip()

    pygame.time.wait(2000)


if __name__ == '__main__':
    main()
