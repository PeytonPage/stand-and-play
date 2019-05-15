import pygame
import RPi.GPIO as GPIO
from gyro import *
from random import randint
from time import time, sleep

pygame.init()

selectButton = 18
button2 = 13


sensitivity = 10


GPIO.setmode(GPIO.BCM)
GPIO.setup(selectButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
WIDTH = 800
HEIGHT = 480

timerLength = 5

selectionTime = 1.5

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,165,0)
purple = (128, 0, 128)


whiteBlock = pygame.image.load("whiteBlock.gif")
blackBlock = pygame.image.load("blackBlock.gif")
redBlock = pygame.image.load("redBlock.gif")
greenBlock = pygame.image.load("greenBlock.gif")
blueBlock = pygame.image.load("blueBlock.gif")
yellowBlock = pygame.image.load("yellowBlock.gif")
orangeBlock = pygame.image.load("orangeBlock.gif")
purpleBlock = pygame.image.load("purpleBlock.gif")

colors = [[whiteBlock,"white"], [blackBlock, "black"], [redBlock, "red"],\
          [greenBlock, "green"], [blueBlock, "blue"], [yellowBlock, "yellow"],\
          [orangeBlock, "orange"], [purpleBlock, "purple"]]

Triangle = pygame.image.load("Triangle.gif")
Star = pygame.image.load("Star.gif")
Square = pygame.image.load("Square.gif")
Rectangle = pygame.image.load("Rectangle.gif")
Oval = pygame.image.load("Oval.gif")
Circle = pygame.image.load("Circle.gif")
Pentagon = pygame.image.load("Pentagon.gif")
Hexagon = pygame.image.load("Hexagon.gif")

shapes = [[Triangle, "triangle"], [Star, "star"], [Square, "square"],\
          [Rectangle, "rectangle"], [Oval, "oval"], [Circle, "circle"],\
          [Pentagon, "pentagon"], [Hexagon, "hexagon"]]

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

math_bg = pygame.image.load("MathDefault.gif")
math_bg_left = pygame.image.load("MathLeft.gif")
math_bg_right = pygame.image.load("MathRight.gif")

game_bg = pygame.image.load("GameDefault.gif")
game_bg_left = pygame.image.load("GameLeft.gif")
game_bg_right = pygame.image.load("GameRight.gif")

GameOver_bg = pygame.image.load("GameOver.gif")

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

    if(x_rotation < (sensitivity) and x_rotation > -(sensitivity) and y_rotation < (sensitivity) and y_rotation > -(sensitivity)):
        return "none"    
    elif (x_rotation > 0 and y_rotation < (sensitivity) and y_rotation > -(sensitivity)):
        return "back"        
    elif (x_rotation < 0 and y_rotation < (sensitivity) and y_rotation > -(sensitivity)):
        return "forward"
    elif (x_rotation < (sensitivity) and x_rotation > -(sensitivity) and y_rotation > 0):
        return "left"
    elif (x_rotation < (sensitivity) and x_rotation > -(sensitivity) and y_rotation < 0):
        return "right"
     
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
answersShown = False
shapeNeeded = True

start_ticks = pygame.time.get_ticks()

selection = "none"
previousTime = time()

mainMenu = True
Colors = False
Shapes = False
Math = False
Platformer = False
gameOver = False

while(running):
    while(mainMenu):
        numbersNeeded = True
        falseSolutionNeeded = True
        solutionPosNeeded = True
        answerGiven = False
        timerStarted = False
        difficultySelected = False
        colorNeeded = True
        answersShown = False
        shapeNeeded = True

        mainMenu = True
        Colors = False
        Shapes = False
        Math = False
        Platformer = False
        gameOver = False

        score = 0

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
        
        if (time() - previousTime >= selectionTime) or (GPIO.input(selectButton) == False):
            if (lean == "left"):
                selection = "left"
            elif (lean == "right"):
                selection = "right"
            elif (lean == "back"):
                selection = "back"
            elif (lean == "forward"):
                selection = "forward"

            if (GPIO.input(selectButton) == False):
                sleep(0.2)
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

        gameOver = False
        i = 0

        pygame.display.update()




        
    
    while(Math):
        if(i == 0):
                previousTime = time()
                i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

        while (difficultySelected == False):
            

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

            
            if (time() - previousTime >= selectionTime) or (GPIO.input(selectButton) == False):
                if (lean == "left"):
                    difficulty = "easy"
                    difficultySelected = True
                elif (lean == "back"):
                    difficulty = "medium"
                    difficultySelected = True
                elif (lean == "right"):
                    difficulty = "hard"
                    difficultySelected = True
                else:
                    difficultySelected = False

                if (GPIO.input(selectButton) == False):
                    sleep(0.2)

           




        if (timerStarted == False):
            start_ticks = pygame.time.get_ticks()
            timerStarted = True
                    
        # get direction of lean
        lean = rotationTest()

        # update background to highlight selection
        if (lean == "left"):
            gameDisplay.blit(math_bg_left,(0,0))
        elif (lean == "right"):
            gameDisplay.blit(math_bg_right,(0,0))
        else:
            gameDisplay.blit(math_bg,(0,0))


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
            gameOver = True
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
        
        if (time() - previousTime >= selectionTime) or (GPIO.input(selectButton) == False):
            if (lean == "left"):
                selection = "left"
            elif (lean == "right"):
                selection = "right"
            answerGiven = True

            if (lean == "forward") or (lean == "back") or (lean == "none"):
                answerGiven = False

            if (GPIO.input(selectButton) == False):
                sleep(0.2)
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

    while (Shapes):
        if(i == 0):
                previousTime = time()
                i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

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
        if (shapeNeeded):
            shape1 = randint(0,len(shapes)-1)
            shape2 = randint(0,len(shapes)-1)
            while(shape1 == shape2):
                shape2 = randint(0,len(shapes)-1)
            
            shapeNeeded = False

        # generate countdown timer
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if (seconds <= timerLength):
            countdown = timerLength - seconds
        else:
            questionText = largeFont.render("Game Over!", True, black)
            solution = ""
            falseSolution = ""
            
            gameOver = True
            Shapes = False
            

            #math = False
        timerText = font.render(str(countdown), True, white)
        timerRect = timerText.get_rect()
        timerRect.center = (160,447)
        gameDisplay.blit(timerText, timerRect)

        # generate question text and solution based on difficulty if timer != 0
        if(countdown != 0):
            if (shapes[shape1][1][0] == "a") or (shapes[shape1][1][0] == "e") or (shapes[shape1][1][0] == "i") or (shapes[shape1][1][0] == "o") or (shapes[shape1][1][0] == "u"):
                questionText = font.render("Which shape is an {}?".format(shapes[shape1][1]), True, black)
            else:
                questionText = font.render("Which shape is a {}?".format(shapes[shape1][1]), True, black)
        # show question on screen
        questionRect = questionText.get_rect()
        questionRect.center = (WIDTH / 2, 150)
        gameDisplay.blit(questionText, questionRect)

            
        # determine where correct answer goes
        if (solutionPosNeeded):
            solPos = randint(0,1)
            if (solPos == 0):
                solutionCoordinates = (125,275)
                falseSolutionCoordinates = (565,275)
                solutionPosition = "left"
            else:
                solutionCoordinates = (565,275)
                falseSolutionCoordinates = (125,275)
                solutionPosition = "right"
            solutionPosNeeded = False

            
        gameDisplay.blit(shapes[shape1][0], solutionCoordinates)
        gameDisplay.blit(shapes[shape2][0], falseSolutionCoordinates)
        

        # generate score
        scoreText = font.render(str(score), True, white)
        scoreRect = scoreText.get_rect()
        scoreRect.center = (650, 444)
        gameDisplay.blit(scoreText, scoreRect)

        # get user selection
        if(lean == "none") or (lean == "forward") or (lean == "back"):
            previousTime = time()
        
        if (time() - previousTime >= 2) or (GPIO.input(selectButton) == False):
            if (lean == "left"):
                selection = "left"
            elif (lean == "right"):
                selection = "right"
            answerGiven = True

            if (lean == "forward") or (lean == "back") or (lean == "none"):
                answerGiven = False

            if (GPIO.input(selectButton) == False):
                sleep(0.2)
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

            shapeNeeded = True
            falseSolutionNeeded = True
            solutionPosNeeded = True
            answersShown = False
        
        pygame.display.update()

    while (Colors):
        if(i == 0):
                previousTime = time()
                i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()





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
        if (colorNeeded):
            color1 = randint(0,len(colors)-1)
            color2 = randint(0,len(colors)-1)
            while(color1 == color2):
                color2 = randint(0,len(colors)-1)
            
            colorNeeded = False

        # generate countdown timer
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if (seconds <= timerLength):
            countdown = timerLength - seconds
        else:
            gameOver = True
            Colors = False
            

        
        timerText = font.render(str(countdown), True, white)
        timerRect = timerText.get_rect()
        timerRect.center = (160,447)
        gameDisplay.blit(timerText, timerRect)

        # generate question text and solution based on difficulty if timer != 0
        if(countdown != 0):
            questionText = font.render("Which color is {}?".format(colors[color1][1]), True, black)
        
        # show question on screen
        questionRect = questionText.get_rect()
        questionRect.center = (WIDTH / 2, 150)
        gameDisplay.blit(questionText, questionRect)

            
        # determine where correct answer goes
        if (solutionPosNeeded):
            solPos = randint(0,1)
            if (solPos == 0):
                solutionCoordinates = (125,275)
                falseSolutionCoordinates = (565,275)
                solutionPosition = "left"
            else:
                solutionCoordinates = (565,275)
                falseSolutionCoordinates = (125,275)
                solutionPosition = "right"
            solutionPosNeeded = False

            
        gameDisplay.blit(colors[color1][0], solutionCoordinates)
        gameDisplay.blit(colors[color2][0], falseSolutionCoordinates)
        

        # generate score
        scoreText = font.render(str(score), True, white)
        scoreRect = scoreText.get_rect()
        scoreRect.center = (650, 444)
        gameDisplay.blit(scoreText, scoreRect)

        # get user selection
        if(lean == "none") or (lean == "forward") or (lean == "back"):
            previousTime = time()
        
        if (time() - previousTime >= 2) or (GPIO.input(selectButton) == False):
            if (lean == "left"):
                selection = "left"
            elif (lean == "right"):
                selection = "right"
            answerGiven = True

            if (lean == "forward") or (lean == "back") or (lean == "none"):
                answerGiven = False

            if (GPIO.input(selectButton) == False):
                sleep(0.2)
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

            colorNeeded = True
            falseSolutionNeeded = True
            solutionPosNeeded = True
            answersShown = False
        
        pygame.display.update()

    while (Platformer):
        pygame.quit()

    while (gameOver):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

        gameDisplay.blit(GameOver_bg, (0,0))
        GameOverText = largeFont.render("Game Over!", True, black)
        GameOverRect = GameOverText.get_rect()
        GameOverRect.center = (WIDTH / 2, 150)
        gameDisplay.blit(GameOverText, GameOverRect)

        GameOverScoreText = largeFont.render("Your score was {}.".format(score), True, black)
        GameOverScoreRect = GameOverScoreText.get_rect()
        GameOverScoreRect.center = (WIDTH / 2, 325)
        gameDisplay.blit(GameOverScoreText, GameOverScoreRect)

        ContinueText = font.render("Press a button to continue...", True, white)
        ContinueRect = ContinueText.get_rect()
        ContinueRect.center = (WIDTH / 2, 450)
        gameDisplay.blit(ContinueText, ContinueRect)

        if (GPIO.input(selectButton) == False) or (GPIO.input(button2) == False):
            sleep(0.5)
            selection = "none"
            previousTime = time()
            gameOver = False
            mainMenu = True
        

        pygame.display.update()


