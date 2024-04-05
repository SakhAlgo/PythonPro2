from pygame import *
init()
window = display.set_mode((700,500))
display.set_caption('Догонялки')

background = transform.scale(image.load('./images/fon.png'), (700, 500))
window.blit(background, (0, 0))

ball = transform.scale(image.load('./images/ball.png'), (50,50))
ball_rect = Rect(100, 400, 50, 50)
window.blit(ball, (100, 400))

enemy = transform.scale(image.load('./images/enemy.png'), (50,50))
enemy_rect = Rect(400, 400, 50, 50)
window.blit(enemy, (400, 400))

clock = time.Clock()
isgame = True
while isgame:
    for e in event.get():
        if e.type == QUIT:
            isgame = False
            quit()

        keys_pressed = key.get_pressed()

        if keys_pressed[K_j] and enemy_rect.x > 0:
            enemy_rect.x += -5
        if keys_pressed[K_l] and enemy_rect.x < 650:
            enemy_rect.x += 5
        if keys_pressed[K_i] and enemy_rect.y > 0:
            enemy_rect.y += -5
        if keys_pressed[K_k] and enemy_rect.y < 450:
            enemy_rect.y += 5

        if keys_pressed[K_a] and ball_rect.x > 0:
            ball_rect.x += -5
        if keys_pressed[K_d] and ball_rect.x < 650:
            ball_rect.x += 5
        if keys_pressed[K_w] and ball_rect.y > 0:
            ball_rect.y += -5
        if keys_pressed[K_s] and ball_rect.y < 450:
            ball_rect.y += 5

    window.blit(background, (0, 0))
    window.blit(enemy, (enemy_rect.x, enemy_rect.y))
    window.blit(ball, (ball_rect.x, ball_rect.y))

    if ball_rect.colliderect(enemy_rect):
        isgame = False

    clock.tick(60)
    display.update()