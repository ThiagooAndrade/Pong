import pygame as pg

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PLAYER_WIDTH = 20  # largura dos jogadores
PLAYER_HEIGHT = 150  # altura dos jogadores

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(
            x, y, width, height
        ) 

        self.width = width  # largura do jogador(retangulo)
        self.height = height  # altura do jogador(retangulo)
        self.x = x  # posição x do jogador(retangulo)
        self.y = y  # posição y do jogador(retangulo)
        self.vel = 10  # velocidade do jogador (retangulo)  só consegue se mover para cima ou para baixo

    def render(self, screen):
        pg.draw.rect(screen, "white", self.rect, 0, 7)  # desenha os jogadores(retangulos)

    def move_up(self):
        self.rect.y -= self.vel  # move os jogadores(retangulos) para cima

    def move_down(self):
        self.rect.y += self.vel  # move os jogares(retangulos) para baixo


player1 = Player(0, (SCREEN_HEIGHT / 2) - 35, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = Player(SCREEN_WIDTH - PLAYER_WIDTH, (SCREEN_HEIGHT / 2) - 75, PLAYER_WIDTH, PLAYER_HEIGHT)