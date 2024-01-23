from random import randint
import pygame as pg
from player import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
            

PLAYER_WIDTH = 20  # largura dos jogadores
PLAYER_HEIGHT = 150  # altura dos jogadores


class Ball:
    def __init__(self, x, y, radius):
        self.rect = pg.Rect(
            x - radius, y - radius, radius * 2, radius * 2
        )

        self.radius = radius  # raio do a bola
        self.x = x  # posição x da bola
        self.y = y  # posição y da bola
        self.vel_x = 3  # velocidade horizontal da bola
        self.vel_y = 3  # velocidade vertical da bola
        self.rand = randint(0, 1)  # rng para qual posição a bola irá no inicio do jogo
        self.acceleration = 1

    def render(self, screen):
        pg.draw.ellipse(screen, "white", self.rect)  # desenha a bola


    def update(self):
        if self.rand == 1:
            self.x += self.vel_x
            self.y += self.vel_y
        else:  # rng
            self.x -= self.vel_x
            self.y -= self.vel_y

        if (self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT): # colisão da bola com o teto e o chão da tela + ela rebater para o lado contrario
            self.vel_y = -self.vel_y

        self.rect = pg.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2,  # atualiza a posição da bola
        )

        if (self.rect.colliderect(player1)) or (self.rect.colliderect(player2)):  # verifica a colisao da bola com os jogadores(retangulos)
            self.vel_x = (-self.vel_x)  # rebate a bola para direção contraria depois da colisao

            if self.vel_y > 0:
                self.vel_y += self.acceleration
            else:
                self.vel_y -= self.acceleration  # aumenta a velocidade da bola depois da colisao

            if self.vel_x > 0:
                self.vel_x += self.acceleration
            else:
                self.vel_x -= self.acceleration



