#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Ouvrir et fermer une fenetre avec pygame"""

import pygame

def main():
    pygame.init()
    MY_WINDOW = pygame.display.set_mode((400,300))
    pygame.time.wait(1000)
    pygame.quit()

if __name__ == '__main__':
    main()
