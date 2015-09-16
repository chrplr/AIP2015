#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Affiche un rectangle
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

    pygame.draw.rect(SURFACE_AFFICHAGE,BLUE,(200,150,100,50))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == '__main__':
    main()
