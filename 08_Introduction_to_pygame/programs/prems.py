#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Open a pygame window then close it properly
"""

import pygame
import sys

WINDOW_DIMENSIONS=(400,300)

def initialisation():
    pygame.init()

def ouverture_de_fenetre(size):
    MY_WINDOW=pygame.display.set_mode(size)

def main():
    initialisation()
    ouverture_de_fenetre(WINDOW_DIMENSIONS)
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()
