import pygame
import time
import random

pygame.init()

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)

display_x = 800
display_y = 600
scale_x = (display_x * 0.1)
scale_y = (display_y * 0.1)
apple_scale_x = (display_x * 0.06)
apple_scale_y = (display_y * 0.08)
gameDisplay=pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()
fontStyle = pygame.font.SysFont(None, 50)
gameOver = False
snakeBlock = 30
foodBlock = 20
snakeSpeed = 15

snakeImg = pygame.image.load("./snake.png")
snakeImg = pygame.transform.scale(snakeImg, (scale_x, scale_y))
#snakeRect = snakeImg.get_rect()
appleImg = pygame.image.load("./apple.png")
appleImg = pygame.transform.scale(appleImg, (apple_scale_x,apple_scale_y))
appleRect = appleImg.get_rect()

def message(msg,color):
    msg = fontStyle.render(msg, True, color)
    gameDisplay.blit(msg, [display_x/4, display_y/3])

def snake(x,y):
    snakeRect = snakeImg.get_rect()
    snakeRect = snakeRect.move((x, y))
    gameDisplay.blit(snakeImg, snakeRect)

def apple(x,y):
    appleRect = appleImg.get_rect()
    appleRect = appleRect.move((x,y))
    gameDisplay.blit(appleImg,appleRect)

def getSnake(snakeBlock, snake_list):
    for x in snake_list:
        #snakeRect = pygame.rect((x[0],x[1]),(snakeBlock,snakeBlock))
        snakeRect = snakeImg.get_rect()
        pygame.draw.rect(gameDisplay, snakeRect, [x[0],x[1], snakeBlock, snakeBlock])

def show_score(color, size, cscore):
    score_font = pygame.font.SysFont(None, size)
    score_surface = score_font.render('Score : ' + str(cscore), True, color)
    gameDisplay.blit(score_surface, [0,0])

def gameLoop():
    game_over = False
    menu = False
    snakeX = display_x/2
    snakeY = display_y/2
    snakeX_change = 0
    snakeY_change = 0
    snakeList = []
    length = 1
    foodX = round(random.randrange(0, display_x - snakeBlock) / 10.0) * 10.0
    foodY = round(random.randrange(0, display_x - snakeBlock) / 10.0) * 10.0

    while not game_over:
        while menu == True:
            gameDisplay.fill(white)
            message("Game Over! Play again: P", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        menu = False
                    if event.key == pygame.K_p:
                        gameLoop()  
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN: #check for key presses
                if event.key == pygame.K_a:
                    snakeX_change = -10
                    snakeY_change = 0
                if event.key == pygame.K_d:
                    snakeX_change = 10
                    snakeY_change = 0
                if event.key == pygame.K_w:
                    snakeX_change = 0
                    snakeY_change = -10
                if event.key == pygame.K_s:
                    snakeX_change = 0
                    snakeY_change = 10
        if snakeX >= display_x or snakeX < 0 or snakeY >= display_y or snakeY < 0:
            menu = True
        snakeX += snakeX_change
        snakeY += snakeY_change
        gameDisplay.fill(white)
        #foodRect = pygame.Rect((foodX, foodY), (foodBlock, foodBlock))
        apple(foodX,foodY)

        #pygame.draw.rect(gameDisplay, foodRect, [foodX, foodY, foodBlock, foodBlock])
        snakeHead = []
        snakeHead.append(snakeX)
        snakeHead.append(snakeY)      
        snakeList.append(snakeHead)
        if len(snakeList) > length:
            del snakeList[0]
        for x in snakeList[:-1]:
            if x == snakeHead:
                menu = True
        snakeheadrect = pygame.Rect((snakeX, snakeY),(snakeBlock,snakeBlock))    
        getSnake(snakeBlock ,snakeList)
        show_score(blue, 35, length -1)
        pygame.display.update()
 
        if (snakeheadrect.colliderect(appleRect) == True):
            print("collide")
            foodX = round(random.randrange(0, display_x - snakeBlock) / 10.0) * 10.0
            foodY = round(random.randrange(0, display_y - snakeBlock) / 10.0) * 10.0
            length += 1
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()
gameLoop()
