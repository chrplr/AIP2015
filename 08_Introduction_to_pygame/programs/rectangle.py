#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Affiche un rectangle
"""

import sys
import pygame

WHITE=(255,255,255)
BLUE=(0,0,255)
WINDOW_DIMENSIONS = (400,300)


def main():
    pygame.init()
    MY_WINDOW=pygame.display.set_mode(WINDOW_DIMENSIONS)
    MY_WINDOW.fill(WHITE)
    pygame.draw.rect(MY_WINDOW,BLUE,(200,150,100,50))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
