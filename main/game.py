import pygame as pg
from sys import exit
from random import randint


pg.init()

# tamanho da tela
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PLAYER_WIDTH = 20  # largura dos jogadores
PLAYER_HEIGHT = 150  # altura dos jogadores

clock = pg.time.Clock()

game = True  # loop do jogo
victory = [0, 0]  # vitorias dos jogadores
running = True  # loop do jogo até que alguem ganhe

# tela
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Player:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(
            x, y, width, height
        )  # classe Rect para usar o colliderect para a colisão

        self.width = width  # largura do jogador(retangulo)
        self.height = height  # altura do jogador(retangulo)
        self.x = x  # posição x do jogador(retangulo)
        self.y = y  # posição y do jogador(retangulo)
        self.vel = 10  # velocidade do jogador (retangulo)  só consegue se mover para cima ou para baixo

    def render(self, screen):
        pg.draw.rect(screen, "white", self.rect)  # desenha os jogadores(retangulos)

    def move_up(self):
        self.rect.y -= self.vel  # move os jogadores(retangulos) para cima

    def move_down(self):
        self.rect.y += self.vel  # move os jogares(retangulos) para baixo

    def move_right(self):
        self.rect.x += self.vel

    def move_left(self):
        self.rect.x -= self.vel


class Ball:
    def __init__(self, x, y, radius):
        self.rect = pg.Rect(
            x - radius, y - radius, radius * 2, radius * 2
        )  # classe Rect para usar o colliderect para a colisão

        self.radius = radius  # raio do a bola
        self.x = x  # posição x da bola
        self.y = y  # posição y da bola
        self.vel_x = 3  # velocidade horizontal da bola
        self.vel_y = 3  # velocidade vertical da bola
        self.rand = randint(0, 1)  # rng para qual posição a bola irá no inicio do jogo

    def render(self, screen):
        pg.draw.circle(screen, "white", (self.x, self.y), self.radius)  # desenha a bola
        pg.draw.circle(screen, "red", (self.x - self.radius, self.y - self.radius), 5)

    def update(self):
        if self.rand == 1:
            self.x += self.vel_x
            self.y += self.vel_y
        else:  # rng
            self.x -= self.vel_x
            self.y -= self.vel_y

        if (
            self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT
        ):  # colisão da bola com o teto e o chão da tela + ela rebater para o lado contrario
            self.vel_y = -self.vel_y

        self.rect = pg.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2,  # atualiza a posição da bola
        )

        if (self.rect.colliderect(rect1.rect)) or (
            self.rect.colliderect(rect2.rect)
        ):  # verifica a colisao da bola com os jogadores(retangulos)
            self.vel_x = (
                -self.vel_x
            )  # rebate a bola para direção contraria depois da colisao

            if self.vel_y > 0:
                self.vel_y += 1
            else:
                self.vel_y -= 1  # aumenta a velocidade da bola depois da colisao

            if self.vel_x > 0:
                self.vel_x += 1
            else:
                self.vel_x -= 1


while game:
    rect1 = Player(0, (SCREEN_HEIGHT / 2) - 35, PLAYER_WIDTH, PLAYER_HEIGHT)
    rect2 = Player(
        SCREEN_WIDTH - PLAYER_WIDTH,
        (SCREEN_HEIGHT / 2) - 75,
        PLAYER_WIDTH,
        PLAYER_HEIGHT,
    )
    circle = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30)

    font = pg.font.Font("freesansbold.ttf", 50)

    victory1_text = font.render(f"{victory[0]}", True, "white", "black")
    victory1_Rect_text = victory1_text.get_rect()
    victory1_Rect_text.center = (350, 50)

    victory2_text = font.render(f"{victory[1]}", True, "white", "black")
    victory2_Rect_text = victory2_text.get_rect()
    victory2_Rect_text.center = (950, 50)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill("black")

        screen.blit(victory1_text, victory1_Rect_text)
        screen.blit(victory2_text, victory2_Rect_text)

        pg.display.set_caption("gamezada")

        keys = pg.key.get_pressed()

        if rect1.rect.y > 0:
            if keys[pg.K_w]:
                rect1.move_up()

        if rect1.rect.y < SCREEN_HEIGHT - 150:
            if keys[pg.K_s]:
                rect1.move_down()

        if rect1.rect.x < SCREEN_WIDTH / 2 - 100:
            if keys[pg.K_d]:
                rect1.move_right()

        if rect1.rect.x > 0:
            if keys[pg.K_a]:
                rect1.move_left()

        if rect2.rect.y > 0:
            if keys[pg.K_UP]:
                rect2.move_up()

        if rect2.rect.y < SCREEN_HEIGHT - 150:
            if keys[pg.K_DOWN]:
                rect2.move_down()

        if rect2.rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
            if keys[pg.K_RIGHT]:
                rect2.move_right()

        if rect2.rect.x > SCREEN_WIDTH / 2 + 100:
            if keys[pg.K_LEFT]:
                rect2.move_left()

        rect1.render(screen)
        rect2.render(screen)

        circle.update()
        circle.render(screen)

        if circle.x > SCREEN_WIDTH - circle.radius:
            victory[0] += 1
            break
        elif circle.x < 0 + circle.radius:
            victory[1] += 1
            break

        clock.tick(100)
        pg.display.flip()
