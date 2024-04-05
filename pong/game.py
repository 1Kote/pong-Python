import random
import sys
import pygame

def ballAnimation():
    global ballSpeedX, ballSpeedY

    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ballReset()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1

def playerAnimation():
    player.y += playerSpeed
    if player.top <= 0: 
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def opponentAi():
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentSpeed
    if opponent.top <= 0: 
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

def ballReset():
    global ballSpeedY, ballSpeedX
    ball.center = (WIDTH/2, HEIGHT/2)
    ballSpeedY *= random.choice((1, -1))
    ballSpeedX *= random.choice((1, -1))


#Setup Geral
pygame.init()
clock = pygame.time.Clock()

#Criando a janela
WIDTH = 920
HEIGHT = 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
FPS = 60

#retangulos do jogo
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT/2 - 70, 10, 140)

#cores
bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)

#movimento do Jogo
ballSpeedX = 7
ballSpeedY = 7
playerSpeed = 0 
opponentSpeed = 7

while True:
    #Recebendo os comandos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7


    ballAnimation()
    playerAnimation()
    opponentAi()
    
    #graficos
    WIN.fill(bgColor)
    pygame.draw.rect(WIN, lightGrey, player)
    pygame.draw.rect(WIN, lightGrey, opponent)
    pygame.draw.ellipse(WIN, lightGrey, ball)
    pygame.draw.aaline(WIN, lightGrey, (WIDTH/2,0), (WIDTH/2, HEIGHT) )



    #Atualizando o que e mostrado na janela
    pygame.display.flip()
    clock.tick(FPS)