import pygame
pygame.init()
import os
import random

#makes window and sets main menu background
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()

bgInit = pygame.image.load(os.path.join("./", "background.png"))
bg = pygame.transform.scale(bgInit, (w, h))

instructbgInit = pygame.image.load(os.path.join("./", "instructionsBackground.jpg"))
instructbg = pygame.transform.scale(instructbgInit, (w, h))

tcQRInit = pygame.image.load(os.path.join("./", "tcQR.png"))
tcQR = pygame.transform.scale(tcQRInit, (h, h))

#quit button all initialized and scaled here
quitInit = pygame.image.load(os.path.join("./", "quit.png"))
quit = pygame.transform.scale(quitInit, (w * 600/1600, h * 120/900))
quitHovInit = pygame.image.load(os.path.join("./", "quitHov.png"))
quitHov = pygame.transform.scale(quitHovInit, (w * 600/1600, h * 120/900))

#quit button all initialized and scaled here
backInit = pygame.image.load(os.path.join("./", "back.png"))
back = pygame.transform.scale(backInit, (w * 600/1600, h * 120/900))
backHovInit = pygame.image.load(os.path.join("./", "backHov.png"))
backHov = pygame.transform.scale(backHovInit, (w * 600/1600, h * 120/900))

#Start button, instruction button, and the cause button all initialized and scaled here
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

#main background
mainbgInit = pygame.image.load(os.path.join("./", "mainBackground.png"))
mainbg = pygame.transform.scale(mainbgInit, (w, h))

#tree
treeInit = pygame.image.load(os.path.join("./", "tree.png"))
tree = pygame.transform.scale(treeInit, (w * 320/1600, h * 370/900))

#fire
fireInit = pygame.image.load(os.path.join("./", "fire.png"))
fire = pygame.transform.scale(fireInit, (w, w * 350/2000))

#fireball
fireballInit = pygame.image.load(os.path.join("./", "fireball.png"))
fireball = pygame.transform.scale(fireballInit, (w * 350/1600, h * 350/2000))

#All of bob animations
bobStandingInit = pygame.image.load(os.path.join("./", "bobStanding.png"))
bobStanding = pygame.transform.scale(bobStandingInit, (w * 70/1600, h * 175/900))

bobRightInit = pygame.image.load(os.path.join("./", "bobRight.png"))
bobRight = pygame.transform.scale(bobRightInit, (w * 70/1600, h * 175/900))

bobLeftInit = pygame.image.load(os.path.join("./", "bobLeft.png"))
bobLeft = pygame.transform.scale(bobLeftInit, (w * 70/1600, h * 175/900))

bobSeedLeftInit = pygame.image.load(os.path.join("./", "bobSeedLeft.png"))
bobSeedLeft = pygame.transform.scale(bobSeedLeftInit, (w * 70/1600, h * 175/900))

bobSeedRightInit = pygame.image.load(os.path.join("./", "bobSeedRight.png"))
bobSeedRight = pygame.transform.scale(bobSeedRightInit, (w * 70/1600, h * 175/900))

#Font for winning or losing text/info on top right
font = pygame.font.Font('freesansbold.ttf', int(w * 50/1600))
winLoseFont = pygame.font.Font('freesansbold.ttf', int(w * 200/1600))
winText = winLoseFont.render('YOU WON!', True, (0,0,0), None)
loseText = winLoseFont.render('YOU LOST!', True, (0,0,0), None)

#some important parameters
play = True #Basically says that the program is running
start_ticks = pygame.time.get_ticks() #Starts the timer for the game during the main menu, to remove later
screen = 0 #Sets this variable to 0, meaning that the screen that it's on is on the main menu by default

#Scaled to be proportionate to monitor size, and is not currently moving right or left.
playerX = w * 40/1600
moveRight = False
moveLeft = False

#Not planting any seeds either.
plantingSeed = False

#Arrays all used for later.
trees = [tree]
treesPos = [w * 1200/1600]
treesTime = []

maxCooldown = 2
currCooldown = maxCooldown #Cooldown for tree planting
firstPlant = False

temp = 0.3 #Used for global warming

#for wildfire
fireTimeChosen = False
timeToFire = 0

ballX = w * 1800/1600
ballY = h * -200/900
ballTimeChosen = False
timeToFireBall = 0

while play:
    
    seconds = (pygame.time.get_ticks() - start_ticks)/1000 #Sets what seconds will be
    
    if (not firstPlant):
        startPlantTime = seconds
    if (currCooldown < maxCooldown):
        currCooldown = int(seconds - startPlantTime)

#Gets x, y of mouse position
    x, y = pygame.mouse.get_pos()

    if (screen == 0): #Just overlays all buttons and things together to work well
        window.blit(bg, (0, 0))
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 740/900 and y < h * 860/900):
            window.blit(quitHov, (w * 500/1600, h * 740/900))
        else:
            window.blit(quit, (w * 500/1600, h * 740/900))
        #start button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 260/900  and y < h * 380/900):
            window.blit(startButHov, (w * 500/1600, h * 260/900))
        else:
            window.blit(startBut, (w * 500/1600, h * 260/900))
        #instructions button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 420/900 and y < h * 540/900):
            window.blit(instructionButHov, (w * 500/1600, h * 420/900))
        else:
            window.blit(instructionBut, (w * 500/1600, h * 420/900))
        #the cause button
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 580/900 and y < h * 700/900):
            window.blit(tcButHov, (w * 500/1600, h * 580/900))
        else:
            window.blit(tcBut, (w * 500/1600, h * 580/900))

    elif (screen == 1): #game starts

        if ((int(seconds) > prevTime) and (temp > 0)):
            temp -= (len(trees) - 3) * 0.01 #For temperature change
        prevTime = seconds

        yearText = font.render('Year: ' + str(int(seconds - gameStartTime) + 2023), True, (0,0,0), None)
        tempText = font.render('Temp: +' + str(temp - temp % 0.01)[0:4] + '°C', True, (0,0,0), None)

        window.blit(mainbg, (0, 0))

        if (x > w * 10/1600  and x < w * 10/1600 and y > h * 610/900 and y < h * 130/900):
            window.blit(quitHov, (w * 10/1600, h * 10/900))
        else:
            window.blit(quit, (w * 10/1600, h * 10/900))
        
        window.blit(yearText, (w * 1320/1600, h * 100/900))
        window.blit(tempText, (w * 1225/1600, h * 30/900))

        length = len(trees) #Makes trees slowly decay after some time
        for ind in range(len(trees)):
            i = (length - 1) - ind
            trees[i].set_alpha(int((treesTime[i] - seconds) * 25.5))
            window.blit(trees[i], (treesPos[i], h * 400/900))
            if (int(treesTime[i] - seconds <= 0)):
                trees.pop(i)
                treesPos.pop(i)
                treesTime.pop(i)

        if (plantingSeed and currCooldown == maxCooldown): #Makes sure that player can properly plant trees
            startPlantTime = seconds
            window.blit(bobSeedRight, (playerX, h * 600/900))
            for i in range(len(treesPos)):
                if((treesPos[i] - playerX) > w * -200/1600 and (treesPos[i] - playerX) < w * 200/1600):
                    plantingSeed = False
                    currCooldown = maxCooldown
            if (plantingSeed):
                trees.append(tree)
                treesPos.append(playerX)
                treesTime.append(int(seconds + 10))
                currCooldown = 0
            plantingSeed = False
        elif ((moveRight and not moveLeft) and (playerX <= w * 1530/1600)):
            playerX += w * 20/1600
            window.blit(bobRight, (playerX, h * 600/900))
        elif ((moveLeft) and (playerX >= w * 20/1600)):
            playerX -= w * 20/1600
            window.blit(bobLeft, (playerX, h * 600/900))           
        else:
            window.blit(bobStanding, (playerX, h * 600/900))

        #wildfires
        rand = (random.random() * int((4-temp) * 2)) 
        if (not fireTimeChosen):
            nextFire = seconds + ((int)(random.random()*11) + 5)
            fireTimeChosen = True
        elif (seconds >= nextFire):
            timeToFire = seconds - nextFire
            if (rand < 1):
                window.blit(fire, (0, h * 500/900))
        if (timeToFire >= 1):
            if (rand < 1):
                trees.clear()
                treesPos.clear()
                treesTime.clear()
            timeToFire = 0
            fireTimeChosen = False
            
        #fireball 
        if (not ballTimeChosen):
            nextFireBall = seconds + ((int)(random.random()*11) + 10)
            ballTimeChosen = True
        elif (seconds >= nextFireBall):
            timeToFireBall = seconds - nextFireBall
            if ((ballY < 450) and (int(seconds) % prevTime >= 1)):
                window.blit(fireball, (ballX, ballY))
                ballX -= w * 200/1600
                ballY += h * 200/1600
            else:
                window.blit(fire, (0, h * 500/900))
                timeToFire = 1
            prevBallTime = int(seconds)
        if (timeToFireBall >= 3):
            timeToFireBall = 0
            ballTimeChosen = False

    elif (screen == 2):
        window.blit(instructbg, (0, 0))
        if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 415/900 and y < h * 535/900):
            window.blit(backHov, (w * 950/1600, h * 415/900))
        else:
            window.blit(back, (w * 950/1600, h * 415/900))
    elif (screen == 3):
        pygame.draw.rect(window, (0,0,0), pygame.Rect(0, 0, w, h))
        if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 415/900 and y < h * 535/900):
            window.blit(backHov, (w * 950/1600, h * 415/900))
        else:
            window.blit(back, (w * 950/1600, h * 415/900))
        window.blit(tcQR, (0, 0))        
    
    #for any event that happens in the game (mainly refers to keybinds)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN: #Escape button quits the game
            if (event.key == pygame.K_ESCAPE):
                play = False

        if (screen == 1):
            if (x > w * 10/1600  and x < w * 10/1600 and y > h * 610/900 and y < h * 250/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
        
        #game screens
        if (screen == 0):
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 260/900  and y < h * 380/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 1
                treesTime.append(seconds + 10)
                prevTime = seconds
                gameStartTime = seconds
                nextFire = seconds + ((int)(random.random()*11) + 5)
                
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 420/900 and y < h * 540/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 2
                
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 580/900 and y < h * 700/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 3
            
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 740/900 and y < h * 860/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False;
                
        elif (screen == 1):
            if event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (not (event.key == pygame.K_a or event.key == pygame.K_LEFT))):
                    moveLeft = False
                    moveRight = True
                elif ((event.key == pygame.K_a or event.key == pygame.K_LEFT)):
                    moveLeft = True
                    moveRight = False
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE):
                    firstPlant = True
                    plantingSeed = True
            elif (event.type == pygame.KEYUP):
                if ((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (not (event.key == pygame.K_a or event.key == pygame.K_LEFT))):
                    moveLeft = False
                    moveRight = False
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    moveRight = False
                    moveLeft = False
                elif ((event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE)):
                    plantingSeed = False
        elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 415/900 and y < h * 535/900  and event.type == pygame.MOUSEBUTTONDOWN):
            screen = 0

    #print("Position:" + str(playerX) + ", boundaryLeft:" + str(w * 20/1600), " boundaryRight:" + str(w * 1580/1600))
    #print("cool:" + str(currCooldown) + ", sec:" + str(seconds) + ", temp:" + str(temp))  
    #print("trees:" + ''.join(trees) + ", pos:" + ''.join(treesPos) + ", time:" + ''.join(treesTime))
    #print("wfCon:" + str(wfCon) + ", ran:" + str(ran) + ", picked:" + str(picked) + ", seconds: " + str(seconds) + ", wildfireTime: " + str(wildfireTime))
    
    if (screen == 1):
        if (temp >= 2 and (int(seconds - gameStartTime) + 2023) >= 2200):
            screen = 4
        elif (temp <= 0):
            screen = 5

    if (screen == 4):
        window.blit(loseText, (w * 250/1600, h * 400/900))
    elif (screen == 5):
        window.blit(winText, (w * 300/1600, h * 400/900))
        
    pygame.display.update()