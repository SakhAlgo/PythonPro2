import pygame

pygame.init()

LIGHT_BLUE = (200, 200, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((700, 500))
window.fill(LIGHT_BLUE)
clock = pygame.time.Clock()
isGame = True

class Sprite:
    def __init__(self, filename, x, y):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class RacketLeft(Sprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_a] and self.rect.y < 365:
            self.rect.y += 5
class RacketRight(Sprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < 365:
            self.rect.y += 5

class Ball(Sprite):
    def __init__(self, filename, x, y, speed_x=5, speed_y=5):
        super().__init__(filename, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):

        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y

racket_left = RacketLeft('racket.png', 30, 100)
racket_right = RacketRight('racket.png', 630, 300)
ball = Ball('tenis_ball.png', 300, 200, 5, -5)

font = pygame.font.SysFont('Arial', 40)
leftWinLabel = font.render('LEFT WIN', True, GREEN)
rightWinLabel = font.render('RIGHT WIN', True, GREEN)


gameStatus = 1
while isGame:
    if gameStatus == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGame = False
                quit()

        window.fill(LIGHT_BLUE)

        racket_right.draw()
        racket_left.draw()
        racket_left.move()
        racket_right.move()

        if ball.rect.y < 0 or ball.rect.y > 450:
            ball.speed_y *= -1
        if ball.rect.colliderect(racket_right.rect) or ball.rect.colliderect(racket_left.rect):
            ball.speed_x *= -1

        if ball.rect.x < 0:
            window.blit(rightWinLabel, (300, 200))
            gameStatus = 2
        if ball.rect.x > 650:
            window.blit(leftWinLabel, (300,200))
            gameStatus = 2
        ball.move()
        ball.draw()
    elif gameStatus == 2:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                isGame = False
                quit()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    gameStatus = 1
                    racket_left = RacketLeft('racket.png', 30, 100)
                    racket_right = RacketRight('racket.png', 630, 300)
                    ball = Ball('tenis_ball.png', 300, 200, 5, -5)

    clock.tick(60)
    pygame.display.update()