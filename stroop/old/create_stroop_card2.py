import pygame, random

items = {'gorri':'red', 'zuria':'blue', 'berde':'green', 'beltz':'yellow'}

words = items.keys()
colors = items.values()

ncards = 10
temp_fname = "stroop_basque_%02d.bmp"

ncol = 4
nrow = 8
W, H = 800, 600
font = 'Arial_Bold.ttf' 
font_size = 44


# find the longest word
longest = ""
for x in items.keys():
    if len(x)>len(longest): longest = x
    

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)

#screen = pygame.display.set_mode((W, H))

pygame.mouse.set_visible(False)

msgsurf = pygame.Surface((W, H))
font = pygame.font.Font(font,font_size)

def share(list1, list2):
    share = False
    for i in range(len(list1)):
            if list1[i] == list2[i]:
                share = True
                break
    return share

def create_matrix(nrow, ncol):
    oldcol = [99] * ncol
    mat = []
    mat2 = []
    for i in range(nrow):
        it = random.sample(range(ncol), ncol)
        col = random.sample(range(ncol), ncol)
        while share(it, col) or share(oldcol, col):
            col = random.sample(range(ncol), ncol)
        oldcol = col
        mat.append(col)
        mat2.append(it)
    for j in 
    return mat


for ff in range(10):
    oldcol = [5 , 5, 5,  5]
    for i in range(nrow):
        it = random.sample(range(ncol), ncol)
        col = random.sample(range(ncol), ncol)
        while share(it, col) or share(oldcol, col):
            col = random.sample(range(ncol), ncol)
        oldcol = col
        for j in range(ncol):
            x = j * W / ncol + 20
            y = i * H / nrow
            string = words[it[j]]
            color = colors[col[j]]
            msgsurf.fill((0,0,0))
            msgsurf.blit(font.render(string,True,pygame.color.Color(color)),(0,0))
            screen.blit(msgsurf,(x,y))
    pygame.display.flip()
    pygame.time.wait(1000)

    fname = temp_fname % (ff)
    pygame.image.save(screen, fname)

pygame.quit()
