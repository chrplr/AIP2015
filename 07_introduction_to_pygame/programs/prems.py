#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Open a pygame window then close it properly
"""

import pygame
import sys

def main():
    pygame.init()
    WINDOW_DIMENSIONS=(400,300)
    MY_WINDOW=pygame.display.set_mode(WINDOW_DIMENSIONS)
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()
