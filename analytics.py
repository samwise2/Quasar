import pygame
import sys
import os
import score
pygame.init()
screen_dimensions=[1000,1000]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255) #sets background value
screen.fill(screencolor)
def write(str, location, font, color):
        myfont = font
        gmovr = myfont.render(str, 1, color)
        screen.blit(gmovr, location)
def analytics():
    screen.fill(screencolor)
    x=150
    f = open("userscores.txt", "r")
    l = open("usernames.txt", "r")
    lines = f.readlines()
    lines2 = l.readlines()
    namescore=[]
    for item in range(len(lines) - 1):
        print float(lines[item].strip())
        namescore.append([int(float(lines[item].strip())), lines2[item]])
    namescore.sort(key=lambda x: x[0])
    namescore.reverse()
    x=150
    for item in range(len(namescore)):
        write((str(namescore[item][0])+"                          "+namescore[item][1]),[300,x],pygame.font.Font(pygame.font.match_font('vgafix'),60),(10,21,38))
        x+=100

    while True:
        #if os.path.exists("hackathon./userscores.txt"):
        write('Highscores', [390, 80], pygame.font.Font(pygame.font.match_font('vgafix'), 60), (10, 21, 38))
        #else
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()