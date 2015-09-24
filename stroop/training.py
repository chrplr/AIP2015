import pygame, random, sys, time


def create_pseudorand_run(liste, rep):
    l = len(liste)
    run = random.sample(liste, l)
    for i in range(rep-1):
        add = random.sample(liste, l)
        while add[0]==run[len(run)-1]:
            add = random.sample(liste, l)
        run.extend(add)
    return run
    
    
W, H = 800, 600

pygame.init()
screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)


fr = open("french_stims.txt").read().splitlines()
random.shuffle(fr)

en = open("english_stims.txt").read().splitlines()
random.shuffle(en)

ba = open("basque_stims.txt").read().splitlines()
random.shuffle(ba)


conditions = create_pseudorand_run(['fr','en','ba'],1)

msgsurf = pygame.Surface((W, H))
font_size = 60
font = pygame.font.Font( 'Arial_Bold.ttf' ,font_size)


resf = open("results_stroop.dat", 'a+')
resf.write("#\n")
resf.write("# Started at " + time.asctime() + "\n")


def show_ready():
    msgsurf.fill((0,0,0))
    msgsurf.blit(font.render("+",True,(255,255,255)),(1024/2+10,768/2+10))
    screen.blit(msgsurf,(0,0))
    pygame.display.flip()
    stop = False
    while (not stop):
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                stop = True
    screen.fill((0,0,0))
    pygame.display.flip()
    pygame.time.wait(1000)


def stim(cond, fname):
    
    s = pygame.image.load(fname)
    screen.blit(s,((1024-W)/2,(768-H)/2))
    pygame.event.clear()
    pygame.display.flip()
    t0 = pygame.time.get_ticks()
    stop = False
    quit = False
    while (not stop):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit = True
                stop = True
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    quit = True
                    stop = True
            elif e.type == pygame.MOUSEBUTTONDOWN:
                stop = True
    t1 = pygame.time.get_ticks()  
    screen.fill((0,0,0))
    pygame.display.flip()
    resf.write("%s %s %d\n" % (cond, fname, t1-t0))
    if quit:
        sys.exit()
    
for f in conditions:
    show_ready()
    if f == 'fr': stim('fr', fr.pop())
    elif f == 'en': stim('en', en.pop())
    elif f == 'ba': stim('ba', ba.pop())
    pygame.time.wait(1500)
    
resf.close()
pygame.quit()
