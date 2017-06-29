import pygame
import time
import sys
import main
import templatemaker
import analytics
rect=pygame.Rect(300,120,400,175)       #sets params for play game button
rect2=pygame.Rect(300,450,400,175)      #sets params for analytics button
select1=pygame.Rect(225,95,525,250)     #sets params for on hover play button
select2=pygame.Rect(225,425,525,225)    #sets params for on hover analytics button
pygame.init()
screen_dimensions=[1000,1000]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255) #sets background value
screen.fill(screencolor)
def write(str,location,font,color):
    myfont = font
    gmovr = myfont.render(str, 1, color)
    screen.blit(gmovr,location)
def namefunc():
    name=""
    while True:
        write('PRESS ENTER TO CONFIRM',[400, 100], pygame.font.Font(pygame.font.match_font('vgafix'),60),(0,0,255))
        write('WHAT IS YOUR NAME? :',[400, 200], pygame.font.Font(pygame.font.match_font('vgafix'),60),(0,0,255))
        write(name,[400,300],pygame.font.Font(pygame.font.match_font('vgafix'),60),(0,0,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        keysdown=pygame.key.get_pressed()
        if keysdown[pygame.K_a]:
            name +=('a')
            time.sleep(0.15)
        if keysdown[pygame.K_b]:
            name +=('b')
            time.sleep(0.15)
        if keysdown[pygame.K_c]:
            name +=('c')
            time.sleep(0.15)
        if keysdown[pygame.K_d]:
            name +=('d')
            time.sleep(0.15)
        if keysdown[pygame.K_e]:
            name +=('e')
            time.sleep(0.15)
        if keysdown[pygame.K_f]:
            name +=('f')
            time.sleep(0.15)
        if keysdown[pygame.K_g]:
            name +=('g')
            time.sleep(0.15)
        if keysdown[pygame.K_e]:
            name +=('e')
            time.sleep(0.15)
        if keysdown[pygame.K_f]:
            name +=('f')
            time.sleep(0.15)
        if keysdown[pygame.K_g]:
            name +=('g')
            time.sleep(0.15)
        if keysdown[pygame.K_h]:
            name +=('h')
            time.sleep(0.15)
        if keysdown[pygame.K_i]:
            name +=('i')
            time.sleep(0.15)
        if keysdown[pygame.K_j]:
            name +=('j')
            time.sleep(0.15)
        if keysdown[pygame.K_k]:
            name +=('k')
            time.sleep(0.15)
        if keysdown[pygame.K_l]:
            name +=('l')
            time.sleep(0.15)
        if keysdown[pygame.K_m]:
            name +=('m')
            time.sleep(0.15)
        if keysdown[pygame.K_n]:
            name +=('n')
            time.sleep(0.15)
        if keysdown[pygame.K_o]:
            name +=('o')
            time.sleep(0.15)
        if keysdown[pygame.K_p]:
            name +=('p')
            time.sleep(0.15)
        if keysdown[pygame.K_q]:
            name +=('q')
            time.sleep(0.15)
        if keysdown[pygame.K_r]:
            name +=('r')
            time.sleep(0.15)
        if keysdown[pygame.K_s]:
            name +=('s')
            time.sleep(0.15)
        if keysdown[pygame.K_t]:
            name +=('t')
            time.sleep(0.15)
        if keysdown[pygame.K_u]:
            name +=('u')
            time.sleep(0.15)
        if keysdown[pygame.K_v]:
            name +=('v')
            time.sleep(0.15)
        if keysdown[pygame.K_w]:
            name +=('w')
            time.sleep(0.15)
        if keysdown[pygame.K_x]:
            name +=('x')
            time.sleep(0.15)
        if keysdown[pygame.K_y]:
            name +=('y')
            time.sleep(0.15)
        if keysdown[pygame.K_z]:
            name+=('z')
            time.sleep(0.15)
        if keysdown[pygame.K_RETURN]:
            f=open("usernames.txt","a")
            f.write(name)
            f.write("\n")
            f.close()
            return name
        if keysdown[pygame.K_BACKSPACE]:
            del(name[-1])
        pygame.display.update()




def menu():
    namefunc()
    while True:
        mousex=(pygame.mouse.get_pos()[0])                   #return mouse position
        mousey=(pygame.mouse.get_pos()[1])
        opt1 = (mousex in range(300, 700) and mousey in range(120, 295)) #checks if mouse is in range of button 1
        opt2 = (mousex in range(300, 700) and mousey in range(450, 625)) #checks if mouse is in range of button 2
        if opt1==False:                                    #restores normal view (no hover)
            screen.fill((100,200,255))
        if opt2==False:
            screen.fill((100,200,255))
        if opt1==True:
            pygame.draw.rect(screen, (0,0,255), select1) #increases button size on hover
            if pygame.mouse.get_pressed()[0]:
                print main.main(templatemaker.template_selection())
        if opt2==True:
            pygame.draw.rect(screen, (0,0,255), select2)     #increases button2 size on hover
            if pygame.mouse.get_pressed()[0]:
                analytics.analytics()
        pygame.draw.rect(screen, (0,0,255), rect)            #draws menu buttons
        pygame.draw.rect(screen,(0,0,255),rect2)
        write('PLAY GAME', [425, 195], pygame.font.Font(pygame.font.match_font('vgafix'), 40), (0, 255, 0))
        write('ANALYTICS', [425, 525], pygame.font.Font(pygame.font.match_font('vgafix'), 40), (0, 255, 0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.display.update()
menu()

