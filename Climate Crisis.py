import pygame
pygame.init()
import os

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = screen.get_size()
bgInit = pygame.image.load(os.path.join("./", "background.png"))
bg = pygame.transform.scale(bgInit, (w, h))

startButInit = pygame.image.load(os.path.join("./", "startBut.png"))
startBut = pygame.transform.scale(startButInit, (w * 600/1600, h * 120/900))
startButHovInit = pygame.image.load(os.path.join("./", "startButHov.png"))
startButHov = pygame.transform.scale(startButHovInit, (w * 600/1600, h * 120/900))

instructionButInit = pygame.image.load(os.path.join("./", "instructionsBut.png"))
instructionBut = pygame.transform.scale(instructionButInit, (w * 600/1600, h * 120/900))
instructionButHovInit = pygame.image.load(os.path.join("./", "instructionsButHov.png"))
instructionButHov = pygame.transform.scale(instructionButHovInit, (w * 600/1600, h * 120/900))

tcButInit = pygame.image.load(os.path.join("./", "causeBut.png"))
tcBut = pygame.transform.scale(tcButInit, (w * 600/1600, h * 120/900))
tcButHovInit = pygame.image.load(os.path.join("./", "causeButHov.png"))
tcButHov = pygame.transform.scale(tcButHovInit, (w * 600/1600, h * 120/900))

mainbgInit = pygame.image.load(os.path.join("./", "mainBackground.png"))
mainbg = pygame.transform.scale(mainbgInit, (w, h))

treeInit = pygame.image.load(os.path.join("./", "tree.png"))
tree = pygame.transform.scale(treeInit, (w * 320/1600, h * 370/900))

play = True
start_ticks=pygame.time.get_ticks()

started = False

while play:
    
    if(started):
        screen.blit(mainbg, (0, 0))
        screen.blit(tree, (w * 1200/1600, h * 400/900))
        pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(w * 40/1600, h * 675/900, w * 40/1600, h * 100/900))
    else:
        screen.blit(bg, (0, 0))
    
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    
    x, y = pygame.mouse.get_pos();
    
    if (started) == False:
        #start button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 400/900  and y < h * 500/900):
            screen.blit(startButHov, (w * 500/1600, h * 390/900))
        else:
            screen.blit(startBut, (w * 500/1600, h * 390/900))
        #instructions button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 560/900 and y < h * 660/900):
            screen.blit(instructionButHov, (w * 500/1600, h * 550/900))
        else:
            screen.blit(instructionBut, (w * 500/1600, h * 550/900))
        #the cause button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 720/900 and y < h * 820/900):
            screen.blit(tcButHov, (w * 500/1600, h * 710/900))
        else:
            screen.blit(tcBut, (w * 500/1600, h * 710/900))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            play = False   
        #game starts    
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 400/900  and y < h * 500/900 and event.type == pygame.MOUSEBUTTONDOWN):
            started = True
            
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 560/900 and y < h * 660/900 and event.type == pygame.MOUSEBUTTONDOWN):
            play = False
            
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 720/900 and y < h * 820/900 and event.type == pygame.MOUSEBUTTONDOWN):
            play = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                play = False
    
    pygame.display.update()