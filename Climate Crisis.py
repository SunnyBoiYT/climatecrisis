import pygame
pygame.init()
import os

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()
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
screen = 0

playerX = w * 40/1600
moveRight = False
moveLeft = False

while play:
    
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    
    x, y = pygame.mouse.get_pos()

    if (screen == 0):
        window.blit(bg, (0, 0))
        #start button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 400/900  and y < h * 500/900):
            window.blit(startButHov, (w * 500/1600, h * 390/900))
        else:
            window.blit(startBut, (w * 500/1600, h * 390/900))
        #instructions button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 560/900 and y < h * 660/900):
            window.blit(instructionButHov, (w * 500/1600, h * 550/900))
        else:
            window.blit(instructionBut, (w * 500/1600, h * 550/900))
        #the cause button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 720/900 and y < h * 820/900):
            window.blit(tcButHov, (w * 500/1600, h * 710/900))
        else:
            window.blit(tcBut, (w * 500/1600, h * 710/900))
    elif (screen == 1):
        window.blit(mainbg, (0, 0))
        window.blit(tree, (w * 1200/1600, h * 400/900))

        if ((moveRight and not moveLeft) and (playerX <= w * 1530/1600)):
            playerX += w * 20/1600
        elif ((moveLeft) and (playerX >= w * 20/1600)):
            playerX -= w * 20/1600

        pygame.draw.rect(window, (200, 0, 0), pygame.Rect(playerX, h * 625/900, w * 70/1600, h * 150/900))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            play = False

        #game screens
        if (screen == 0):
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 400/900  and y < h * 500/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 1
                
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 560/900 and y < h * 660/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
                
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 720/900 and y < h * 820/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
        elif (screen == 1):
            moveRight = False
            moveLeft = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    play = False
                
                if ((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (not (event.key == pygame.K_a or event.key == pygame.K_LEFT))):
                    moveLeft = False
                    moveRight = True
                elif ((event.key == pygame.K_a or event.key == pygame.K_LEFT) and (not (event.key == pygame.K_d or event.key == pygame.K_RIGHT))):
                    moveLeft = True
                    moveRight = False
                #elif ((event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE)):
    print("Position:" + str(playerX) + ", boundaryLeft:" + str(w * 20/1600), " boundaryRight:" + str(w * 1580/1600))          
    pygame.display.update()