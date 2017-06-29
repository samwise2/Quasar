import pygame
import sys
import random
import time
import score
screen_dimensions = [600,600]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255)
screen.fill(screencolor)
def write(str,location,font,color):
    myfont = font
    gmovr = myfont.render(str, 1, color)
    screen.blit(gmovr,location)
def tracing(rectlist):
    save=pygame.Rect(0,0,50,25) #early function definitions
    tracelist=[] #list of rects from the traced line
    screen.fill(screencolor)
    m=0 #timer, to fix a bug. It's there for a reason, trust me
    while True:
        mousex = pygame.mouse.get_pos()[0] #getting mouse x and y
        mousey = pygame.mouse.get_pos()[1]

        if pygame.mouse.get_pressed()[0] and m>=50:
            if (mousex in range(50) and mousey in range(25)):
                n=[rectlist,tracelist] #stuff to return
                return n
            elif not (pygame.Rect(mousex,mousey,10,10) in tracelist):
                tracelist.append(pygame.Rect(mousex, mousey, 10, 10)) #draw with the mouse


        #Drawing stuff
        pygame.draw.rect(screen, (255, 0, 0), save)
        for item in range(len(rectlist)):
            pygame.draw.rect(screen, (0, 0, 0), rectlist[item])
        for item in range(len(tracelist)):
            pygame.draw.rect(screen, (255, 255, 255), tracelist[item])
        write('save', [5, 5], pygame.font.Font(pygame.font.match_font('vgafix'), 20), (0, 255, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        time.sleep(0.01)
        print m
        m+=1
def main(rectlist):
    tracing_and_stencil=tracing(rectlist)
    stencil=tracing_and_stencil[0]
    trace=tracing_and_stencil[1]
    stencil_length=len(stencil) #stencil length
    trace_length=len(trace) #trace length
    if trace_length>=stencil_length:
        length_diff= trace_length-stencil_length
        temp_lendiff = length_diff
        while temp_lendiff != 0:
            index = random.randint(0, (len(trace) - 1))
            del(trace[index])
            temp_lendiff -= 1
    elif stencil_length>trace_length and trace_length!=0:
        length_diff=stencil_length-trace_length
        temp_lendiff=length_diff
        while temp_lendiff != 0:
            index = random.randint(0, (len(stencil) - 1))
            del(stencil[index])
            temp_lendiff -= 1
    else:
        userScore=0
        f = open("userscores.txt", "a")
        f.write(str(userScore))
        f.write("\n")
        f.close()
        return str(int(score.score(trace, stencil))) + '%'
    userScore = score.score(trace,stencil)
    f = open("userscores.txt","a")
    f.write(str(userScore))
    f.write("\n")
    f.close()
    return str(int(score.score(trace,stencil)))+'%'