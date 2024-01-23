
def movementPlayer(rect1, rect2, pg, SCREEN_HEIGHT):
        keys = pg.key.get_pressed()
        if rect1.rect.y > 0:
            if keys[pg.K_w]:
                rect1.move_up()

        if rect1.rect.y < SCREEN_HEIGHT - 150:
            if keys[pg.K_s]:
                rect1.move_down()

        if rect2.rect.y > 0:
            if keys[pg.K_UP]:
                rect2.move_up()

        if rect2.rect.y < SCREEN_HEIGHT - 150:  
            if keys[pg.K_DOWN]:
                rect2.move_down()

def victoriesText (pg, screen, victory):
    font = pg.font.Font("freesansbold.ttf", 50)

    x_text_victory1 = 350
    x_text_victory2 = 950
    y_text_victory2 = 50
    y_text_victory1 = 50


    victory1_text = font.render(f"{victory[0]}", True, "white", "black")
    victory1_Rect_text = victory1_text.get_rect()
    victory1_Rect_text.center = (x_text_victory1, y_text_victory1)

    victory2_text = font.render(f"{victory[1]}", True, "white", "black")
    victory2_Rect_text = victory2_text.get_rect()
    victory2_Rect_text.center = (x_text_victory2, y_text_victory2)

    screen.blit(victory1_text, victory1_Rect_text)
    screen.blit(victory2_text, victory2_Rect_text)

def checkVictory(circle, victory, SCREEN_WIDTH):
    if circle.x > SCREEN_WIDTH - circle.radius:
        victory[0] += 1
        return True
    elif circle.x < 0 + circle.radius:
        victory[1] += 1
        return True