import pygame
import time

pygame.init()
display_x = 800
display_y = 600
scale_x = (display_x * 0.1)
scale_y = (display_y * 0.1)
apple_scale_x = (display_x * 0.06)
apple_scale_y = (display_y * 0.08)

gameDisplay = pygame.display.set_mode((display_x,display_y))
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)

clock = pygame.time.Clock()
collided = False
snakeImg = pygame.image.load("./snake.png")
snakeImg = pygame.transform.scale(snakeImg, (scale_x, scale_y))
snakeRect = snakeImg.get_rect()
appleImg = pygame.image.load("./apple.png")
appleImg = pygame.transform.scale(appleImg, (apple_scale_x,apple_scale_y))
appleRect = appleImg.get_rect()
def snake(x,y):
    snakeRect = snakeImg.get_rect()
    snakeRect = snakeRect.move((x, y))
    gameDisplay.blit(snakeImg, snakeRect)
def apple(x,y):
    appleRect = appleImg.get_rect()
    appleRect = appleRect.move((x,y))
    gameDisplay.blit(appleImg,appleRect)

x =  (display_x * 0.45)
y = (display_y * 0.8)
applex =  (display_x * 0.35)
appley = (display_y * 0.9)
while not collided:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            collided = True
    gameDisplay.fill(white)
    snake(x,y)
    apple(applex,appley)

    pygame.display.update()
    clock.tick(60)
