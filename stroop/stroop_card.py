#! /usr/bin/env python
# Time-stamp: <2015-09-24 10:58 christophe@pallier.org>
# Author: Christophe Pallier (see http://www.pallier.org)

""" Generates cards for a Stroop task """

import pygame
import random


def share(list1, list2):
    """ returns True if list1 and list2 have at least
        one element in common, at the same position."""
    share = False
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            share = True
            break
    return share


def create_stroop_card(items, nrow = 8, W=800, H=600):
    """ input: a dictionary associating words to colors, for example:
    items = {'rouge':'red', 'bleu':'blue',
             'vert':'green', 'jaune':'yellow'}

    returns:
    a grid of colored words, as a pygame surface of size (W, H) in pixels.
    The grid has 'len(items)' columns, and 'row' rows
    """

    ncol = len(items)
    words = items.keys()
    colors = items.values()

    grid = pygame.Surface((W, H))
    label = pygame.Surface((W, H))

    fontfile = 'Inconsolata.ttf'
    font_size = 44
    font = pygame.font.Font(fontfile, font_size)

    oldcol = [-1] * ncol # var to keep track of colors in previous row 
    for i in range(nrow):
        # pick up random permutations of words and colors
        # making sure they do not match, and avoiding repetitions across rows 
        it = random.sample(range(ncol), ncol)
        col = random.sample(range(ncol), ncol)
        while share(it, col) or share(oldcol, col):
            col = random.sample(range(ncol), ncol)
        oldcol = col

        # blitting the colored words on the grid
        for j in range(ncol):
            x = j * W / ncol + 20
            y = i * H / nrow
            string = words[it[j]]
            color = colors[col[j]]
            label.fill((0, 0, 0))
            label.blit(font.render(string, True, pygame.color.Color(color)),
                       (0, 0))
            grid.blit(label, (x, y))

    return grid


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.mouse.set_visible(False)

    grid = create_stroop_card({'rouge': 'red',
                               'bleu': 'blue',
                               'vert': 'green',
                               'jaune': 'yellow'} )

    screen.blit(grid, ((1024 - 800) / 2, (768 - 600) / 2))
    pygame.display.flip()
    pygame.time.wait(5000)

pygame.quit()
