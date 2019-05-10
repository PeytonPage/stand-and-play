import pygame
from gyro import *
from random import randint
from time import time, sleep

pygame.init()

WIDTH = 800
HEIGHT = 480

timerLength = 60

selectionTime = 1.5

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,165,0)
purple = (128, 0, 128)


colors = [[white,"white"], [black, "black"], [red, "red"], [green, "green"], \
          [blue, "blue"], [yellow, "yellow"], [orange, "orange"], [purple, "purple"]]


menu_bg = pygame.image.load("MainMenu.gif")
menu_bg_center = pygame.image.load("MainMenu-Center.gif")
menu_bg_left = pygame.image.load("MainMenu-Left.gif")
menu_bg_right = pygame.image.load("MainMenu-Right.gif")
menu_bg_up = pygame.image.load("MainMenu-Up.gif")
menu_bg_down = pygame.image.load("MainMenu-Down.gif")

difficulty_bg = pygame.image.load("DifficultySelect.gif")
easy_difficulty_bg = pygame.image.load("DifficultySelect-Easy.gif")
medium_difficulty_bg = pygame.image.load("DifficultySelect-Medium.gif")
hard_difficulty_bg = pygame.image.load("DifficultySelect-Hard.gif")

game_bg = pygame.image.load("GameDefault.gif")
game_bg_left = pygame.image.load("GameLeft.gif")
game_bg_right = pygame.image.load("GameRight.gif")
#gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Stand and Play!')

pygame.mouse.set_visible(False)
pygame.display.update()

font = pygame.font.Font('/home/pi/.fonts/COURIER.TTF',28)
largeFont = pygame.font.Font('/home/pi/.fonts/COURIER.TTF',48)

def rotationTest():
    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)
     
    acceleration_xout_scaled = acceleration_xout / 16384.0
    acceleration_yout_scaled = acceleration_yout / 16384.0
    acceleration_zout_scaled = acceleration_zout / 16384.0

    x_rotation = get_x_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    y_rotation = get_y_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)

    if(x_rotation < 20 and x_rotation > -20 and y_rotation < 20 and y_rotation > -20):
        return "none"    
    elif (x_rotation > 0 and y_rotation < 20 and y_rotation > -20):
        return "right"        
    elif (x_rotation < 0 and y_rotation < 20 and y_rotation > -20):
        return "left"
    elif (x_rotation < 20 and x_rotation > -20 and y_rotation > 0):
        return "forward"
    elif (x_rotation < 20 and x_rotation > -20 and y_rotation < 0):
        return "back"
     
running = True

lean = "none"
score = 0

i = 0

numbersNeeded = True
falseSolutionNeeded = True
solutionPosNeeded = True
answerGiven = False
timerStarted = False
difficultySelected = False
colorNeeded = True

start_ticks = pygame.time.get_ticks()

selection = "none"
previousTime = time()

mainMenu = True
Colors = False
Shapes = False
Math = False
Platformer = False
while(running):
    while(mainMenu):
        selection = "none"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

        lean = rotationTest()

        # update background to highlight selection
        if (lean == "left"):
            gameDisplay.blit(menu_bg_left,(0,0))
        elif (lean == "right"):
            gameDisplay.blit(menu_bg_right,(0,0))
        elif (lean == "forward"):
            gameDisplay.blit(menu_bg_up,(0,0))
        elif (lean == "back"):
            gameDisplay.blit(menu_bg_down,(0,0))
        else:
            gameDisplay.blit(menu_bg_center,(0,0))

        if(lean == "none"):
            previousTime = time()
        
        if (time() - previousTime >= selectionTime):
            if (lean == "left"):
                selection = "left"
            elif (lean == "right"):
                selection = "right"
            elif (lean == "back"):
                selection = "back"
            elif (lean == "forward"):
                selection = "forward"            
        else:
            selection = "none"

        if (selection == "left"):
            mainMenu = False
            Colors = True
            Math = False
            Shapes = False
            Platformer = False
        elif (selection == "right"):
            mainMenu = False
            Colors = False
            Math = False
            Shapes = True
            Platformer = False
        elif (selection == "back"):
            mainMenu = False
            Colors = False
            Math = True
            Shapes = False
            Platformer = False
        elif (selection == "forward"):
            mainMenu = False
            Colors = False
            Math = False
            Shapes = False
            Platformer = True

        pygame.display.update()




        
    
    while(Math):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

        while (difficultySelected == False):
            if(i == 0):
                previousTime = time()
                i += 1

            lean = rotationTest()
            
            if (lean == "left"):
                gameDisplay.blit(easy_difficulty_bg,(0,0))
            elif (lean == "back"):
                gameDisplay.blit(medium_difficulty_bg,(0,0))
            elif (lean == "right"):
                gameDisplay.blit(hard_difficulty_bg,(0,0))
            else:
                gameDisplay.blit(difficulty_bg,(0,0))
            pygame.display.update()

            if(lean == "none") or (lean == "forward"):
                previousTime = time()
        
            if (time() - previousTime >= selectionTime):
                if (lean == "left"):
                    difficulty = "easy"
                elif (lean == "back"):
                    difficulty = "medium"
                elif (lean == "right"):
                    difficulty = "hard"       

                difficultySelected = True




        if (timerStarted == False):
            start_ticks = pygame.time.get_ticks()
            timerStarted = True
                    
        # get direction of lean
        lean = rotationTest()

        # update background to highlight selection
        if (lean == "left"):
            gameDisplay.blit(game_bg_left,(0,0))
        elif (lean == "right"):
            gameDisplay.blit(game_bg_right,(0,0))
        else:
            gameDisplay.blit(game_bg,(0,0))


        # get random numbers for question/solution
        if (numbersNeeded):
            num1 = randint(1,10)
            num2 = randint(1,10)
            if (difficulty == "hard"):
                num1 = randint(1,5)
                num2 = randint(1,5)
            numbersNeeded = False

        # show difficulty on screen
        difficultyText = font.render(difficulty, True, white)
        difficultyRect = difficultyText.get_rect()
        if(difficulty == "medium"):
            difficultyRect.center = (325, 35)
        else:
            difficultyRect.center = (300, 35)
        gameDisplay.blit(difficultyText, difficultyRect)

        # generate countdown timer
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if (seconds <= timerLength):
            countdown = timerLength - seconds
        else:
            questionText = largeFont.render("Game Over!", True, black)
            solution = ""
            falseSolution = ""
            
            mainMenu = True
            Math = False
            

            #math = False
        timerText = font.render(str(countdown), True, white)
        timerRect = timerText.get_rect()
        timerRect.center = (160,447)
        gameDisplay.blit(timerText, timerRect)

        # generate question text and solution based on difficulty if timer != 0
        if(countdown != 0):
            if (difficulty == "easy"):
                questionText = largeFont.render("What is {} + {}?".format(num1, num2), True, black)
                solution = num1 + num2
            elif (difficulty == "medium"):
                questionText = largeFont.render("What is {} * {}?".format(num1, num2), True, black)
                solution = num1 * num2
            elif (difficulty == "hard"):
                questionText = largeFont.render("What is {} ^ {}?".format(num1, num2), True, black)
                solution = num1 ** num2
            else:
                questionText = largeFont.render("ERROR", True, black)
        
        # show question on screen
        questionRect = questionText.get_rect()
        questionRect.center = (WIDTH / 2, 150)
        gameDisplay.blit(questionText, questionRect)

        # generate false solution
        if (falseSolutionNeeded):
            falseSolution = solution + (randint(-5,-1) or randint(1,5))
            if (difficulty == "easy"):
                while (falseSolution < 1):
                    falseSolution = solution + (randint(-5,-1) or randint(1,5))
            falseSolutionNeeded = False
            
        falseSolutionText = largeFont.render(str(falseSolution), True, black)    
        solutionText = largeFont.render(str(solution), True, black)
        
        # determine where correct answer goes
        if (solutionPosNeeded):
            solutionRect = solutionText.get_rect()
            falseSolutionRect = falseSolutionText.get_rect()
            solPos = randint(0,1)
            if (solPos == 0):
                solutionRect.center = (180,325)
                falseSolutionRect.center = (620,325)
                solutionPosition = "left"
            else:
                solutionRect.center = (620,325)
                falseSolutionRect.center = (180,325)
                solutionPosition = "right"
            solutionPosNeeded = False

        

        gameDisplay.blit(solutionText, solutionRect)
        gameDisplay.blit(falseSolutionText, falseSolutionRect)

        # generate score
        scoreText = font.render(str(score), True, white)
        scoreRect = scoreText.get_rect()
        scoreRect.center = (650, 444)
        gameDisplay.blit(scoreText, scoreRect)

        # get user selection
        if(lean == "none") or (lean == "forward") or (lean == "back"):
            previousTime = time()
        
        if (time() - previousTime >= 2):
            if (lean == "left"):
                selection = "left"
            elif (lean == "right"):
                selection = "right"
            answerGiven = True
        else:
            selection = "none"

        # determine if user is correct
        if (answerGiven):
            if (selection == solutionPosition):
                score += 1
            else:
                score -= 1
            if (score <= 0):
                score = 0
            answerGiven = False
            previousTime = time()

            numbersNeeded = True
            falseSolutionNeeded = True
            solutionPosNeeded = True
        
        pygame.display.update()

##    while (Colors):
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                running = False
##                pygame.quit()
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_ESCAPE:
##                    running = False
##                    pygame.quit()
##
##        difficulty = "N/A"
##
##
##
##
##        if (timerStarted == False):
##            start_ticks = pygame.time.get_ticks()
##            timerStarted = True
##                    
##        # get direction of lean
##        lean = rotationTest()
##
##        # update background to highlight selection
##        if (lean == "left"):
##            gameDisplay.blit(game_bg_left,(0,0))
##        elif (lean == "right"):
##            gameDisplay.blit(game_bg_right,(0,0))
##        else:
##            gameDisplay.blit(game_bg,(0,0))
##
##
##        # get random numbers for question/solution
##        if (colorNeeded):
##            color1 = randint(0,7)
##            color2 = randint(0,7)
##            while(color1 == color2):
##                color2 = randint(0,7)
##            
##            colorNeeded = False
##
##        # show difficulty on screen
##        difficultyText = font.render(difficulty, True, white)
##        difficultyRect = difficultyText.get_rect()
##        difficultyRect.center = (300, 35)
##        gameDisplay.blit(difficultyText, difficultyRect)
##
##        # generate countdown timer
##        seconds = (pygame.time.get_ticks()-start_ticks)/1000
##        if (seconds <= timerLength):
##            countdown = timerLength - seconds
##        else:
##            questionText = largeFont.render("Game Over!", True, black)
##            solution = ""
##            falseSolution = ""
##            
##            mainMenu = True
##            Colors = False
##            
##
##            #math = False
##        timerText = font.render(str(countdown), True, white)
##        timerRect = timerText.get_rect()
##        timerRect.center = (160,447)
##        gameDisplay.blit(timerText, timerRect)
##
##        # generate question text and solution based on difficulty if timer != 0
##        if(countdown != 0):
##            questionText = font.render("Which color is {}?".format(colors[color1][1]), True, black)
##        
##        # show question on screen
##        questionRect = questionText.get_rect()
##        questionRect.center = (WIDTH / 2, 150)
##        gameDisplay.blit(questionText, questionRect)
##
##        # generate false solution
##        if (falseSolutionNeeded):
##            falseSolution = colors[color2][1]
##            falseSolutionNeeded = False
##            
##                # determine where correct answer goes
##        if (solutionPosNeeded):
##            solPos = randint(0,1)
##            if (solPos == 0):
##                pygame.draw.rect(gameDisplay, colors[color1][0], (70,270, 260, 380))         
##                pygame.draw.rect(gameDisplay, colors[color2][0],(460,270, 650, 380))
##                solutionPosition = "left"
##            else:
##                pygame.draw.rect(gameDisplay, colors[color1][0], (460,270, 650, 380))          
##                pygame.draw.rect(gameDisplay, colors[color2][0], (70,270, 260, 380))
##                solutionPosition = "right"
##            pygame.display.update()
##            sleep(5)
##            solutionPosNeeded = False
##
##        
##
##        # generate score
##        scoreText = font.render(str(score), True, white)
##        scoreRect = scoreText.get_rect()
##        scoreRect.center = (650, 444)
##        gameDisplay.blit(scoreText, scoreRect)
##
##        # get user selection
##        if(lean == "none") or (lean == "forward") or (lean == "back"):
##            previousTime = time()
##        
##        if (time() - previousTime >= 2):
##            if (lean == "left"):
##                selection = "left"
##            elif (lean == "right"):
##                selection = "right"
##            answerGiven = True
##        else:
##            selection = "none"
##
##        # determine if user is correct
##        if (answerGiven):
##            if (selection == solutionPosition):
##                score += 1
##            else:
##                score -= 1
##            if (score <= 0):
##                score = 0
##            answerGiven = False
##            previousTime = time()
##
##            colorsNeeded = True
##            falseSolutionNeeded = True
##            solutionPosNeeded = True
##        
##        pygame.display.update()
    while (Colors):
        pygame.quit()


    while (Shapes):
        pygame.quit()

    while (Platformer):
        pygame.quit()




