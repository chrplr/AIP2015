import sys
import pygame
pygame.init()

MY_WINDOW = pygame.display.set_mode((400,300))

pygame.display.flip()

background_pattern = pygame.Surface((280,280))

cross = pygame.Surface((40,40))

cross.fill((0,0,0))

pygame.draw.rect(cross, (0,0,255), (18,6,4,28))
pygame.draw.rect(cross, (0,0,255), (6,18,28,4))


background_pattern.fill((255,0,0))
for x in range(0,40*7,40):
    for y in range(0,40*7,40):
        background_pattern.blit(cross,(x,y))



MY_WINDOW.fill((255,255,255))

position=background_pattern.get_rect()

position.center = MY_WINDOW.get_rect().center

MY_WINDOW.blit(background_pattern, position)



pygame.display.flip()


for degres in range(0,1000,1):
    MY_ROTATED_IMAGE = pygame.transform.rotate(background_pattern, degres)
    rotpos=MY_ROTATED_IMAGE.get_rect()
    rotpos.center = MY_WINDOW.get_rect().center
    MY_WINDOW.fill((0,0,0))
    MY_WINDOW.blit(MY_ROTATED_IMAGE, rotpos)
    pygame.draw.circle(MY_WINDOW,(255,255,0), (150,100), 3 )
    pygame.draw.circle(MY_WINDOW,(255,255,0), (250,100), 3 )
    pygame.draw.circle(MY_WINDOW,(255,255,0), (150,200), 3 )
    pygame.draw.circle(MY_WINDOW,(255,255,0), (250,200), 3 )

    if not degres%100:
        color = (0,255,0)
    else:
        color = (255,0,0)

    pygame.draw.circle(MY_WINDOW,color, (200,150), 2 )

    pygame.display.flip()

pygame.quit()
sys.exit()
