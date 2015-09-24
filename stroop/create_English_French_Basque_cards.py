#! /usr/bin/env python
# Time-stamp: <2007-06-28 18:20:08 pallier>
# Author: Christophe Pallier (see http://www.pallier.org)

import pygame, stroop_card

def create_cards(items, ncards, template):
    for i in range(ncards):
        grid = stroop_card.create_stroop_card(items)
        pygame.image.save(grid, template % (i))



pygame.init()
screen = pygame.display.set_mode((800, 600))


create_cards({'rouge':'red', 'blanc':'white', 'vert':'green', 'jaune':'yellow'}, 32, "Stroop_French_%02d.bmp")
create_cards({'red':'red', 'white':'white', 'green':'green', 'yellow':'yellow'}, 32, "Stroop_English_%02d.bmp")
create_cards({'gorri':'red', 'zuri':'white', 'berde':'green', 'horri':'yellow'}, 32, "Stroop_Basque_%02d.bmp")


pygame.quit()



