import pygame
import time
import random

pygame.init()

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)

window_width = 800
window_height = 600
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()
fontStyle = pygame.font.SysFont(None, 50)
snakeBlock = 30
foodBlock = 20
snakeSpeed = 15

def message(msg,color):
    msg = fontStyle.render(msg, True, color)
    window.blit(msg, [window_width/4, window_height/3])

def getSnake(snakeBlock, snake_list):
    for x in snake_list:
        #snakeRect = pygame.rect((x[0],x[1]),(snakeBlock,snakeBlock))
        
        pygame.draw.rect(window, green, [x[0],x[1], snakeBlock, snakeBlock])

def show_score(color, size, cscore):
    score_font = pygame.font.SysFont(None, size)
    score_surface = score_font.render('Score : ' + str(cscore), True, color)
    window.blit(score_surface, [0,0])

def gameLoop():
    game_over = False
    menu = False
    snakeX = window_width/2
    snakeY = window_height/2
    snakeX_change = 0
    snakeY_change = 0
    snakeList = []
    length = 1
    foodX = round(random.randrange(0, window_width - snakeBlock) / 10.0) * 10.0
    foodY = round(random.randrange(0, window_width - snakeBlock) / 10.0) * 10.0

    while not game_over:
        while menu == True:
            window.fill(white)
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
        if snakeX >= window_width or snakeX < 0 or snakeY >= window_height or snakeY < 0:
            menu = True
        snakeX += snakeX_change
        snakeY += snakeY_change
        window.fill(white)
        foodRect = pygame.Rect((foodX, foodY), (foodBlock, foodBlock))
        pygame.draw.rect(window, red, [foodX, foodY, foodBlock, foodBlock])
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
 
        if (snakeheadrect.colliderect(foodRect) == True):
            print("collide")
            foodX = round(random.randrange(0, window_width - snakeBlock) / 10.0) * 10.0
            foodY = round(random.randrange(0, window_height - snakeBlock) / 10.0) * 10.0
            length += 1
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()
gameLoop()
