import pygame as pg
from sys import exit
from random import randint
from methods import *
from player import *
from ball import *



#Pong
#Thiago Miguel de Luna Andrade
#2023

pg.init()

# tamanho da tela
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



clock = pg.time.Clock()

game = True  # loop do jogo
victory = [0, 0]  # vitorias dos jogadores
running = True  # loop do jogo até que alguem ganhe

# tela
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Pong")



while game:
    circle = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30)
    player1 = Player(0, (SCREEN_HEIGHT / 2) - 35, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = Player(SCREEN_WIDTH - PLAYER_WIDTH, (SCREEN_HEIGHT / 2) - 75, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill("black")

        victoriesText(pg, screen, victory)

        movementPlayer(player1, player2, pg, SCREEN_HEIGHT)

        player1.render(screen)
        player2.render(screen)
        pg.draw.aaline(screen, "white", (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

        circle.update()
        circle.render(screen)

        if(checkVictory(circle, victory, SCREEN_WIDTH)):
            break

        clock.tick(100)
        pg.display.flip()
