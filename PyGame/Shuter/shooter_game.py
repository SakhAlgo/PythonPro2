#Создай собственный Шутер!
import pygame
from time import sleep, time

pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Shooter')
galaxy = pygame.image.load('galaxy.jpg')
galaxy = pygame.transform.scale(galaxy, (700, 500))
window.blit(galaxy, (0, 0))
clock = pygame.time.Clock()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.02)

fire = pygame.mixer.Sound('fire.ogg')
fire.set_volume(0.05)

class Sprite:
    def __init__(self, filename, x, y):
        image = pygame.image.load(filename)
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 650:
            self.rect.x += 5

class TextArea:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fillColor = color

    def setText(self, text, size=30):
        self.font = pygame.font.Font(None, size)
        self.label = self.font.render(text, True, self.fillColor)

    def draw(self, shiftX=0, shiftY=0):
        window.blit(self.label, (self.rect.x + shiftX, self.rect.y + shiftY))

from random import randint
class Enemy(Sprite):
    def __init__(self, filename, x, y, speed):
        super().__init__(filename, x, y)
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

class Bullet(Sprite):
    def __init__(self, filename, x, y, speed=0):
        super().__init__(filename, x, y)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.speed = speed
        self.rect.x += 10
        self.rect.y -= 10

    def move(self):
        self.rect.y -= self.speed
        # pygame.draw.rect(window, WHITE, self.rect, 1)

    def draw(self, shiftX=10, shiftY=20):
        window.blit(self.image, (self.rect.x + shiftX, self.rect.y + shiftY))


asteroids = []
for i in range(3):
    aster = Enemy('asteroid.png', randint(0, 650), randint(-100, 0), randint(2, 5))
    asteroids.append(aster)

enemies = []
for i in range(5):
    enemy = Enemy('ufo.png', randint(0, 650), randint(-100, 0), randint(3, 7))
    enemies.append(enemy)


WHITE = (255, 255, 255)
rect = Player('rocket.png', 325, 450)
rect.draw()

numHit = 0
numLose = 0

point_label = TextArea(10, 10, 50,50, WHITE)
point_label.setText('Hit:')

hitPoint =TextArea(75, 10, 50,50, WHITE)


lose_point_label = TextArea(10, 55, 50,50, WHITE)
lose_point_label.setText('Lose:')
losePoint =TextArea(75, 55, 50,50, WHITE)

speed_enemies = 0
isGame = True

bullets = []
for i in range(6):
    bullet = Bullet('bullet.png', rect.rect.x, rect.rect.y)
    bullets.append(bullet)

amount_bullets = 6
font = pygame.font.SysFont('Arial', 30)

win_label = font.render('YOU WIN.', True, (0,250,0))
lose_label = font.render('YOU LOSE.', True, (0,250,0))
info_label = font.render('Press ESC to exit or TAB to continue.', True, (255,255,255))

stat = 0
gameStatus = 1
while isGame:
    if gameStatus == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGame = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bullet in bullets:
                        if bullet.speed == 0 and amount_bullets > 0:
                            bullet.speed = 10
                            fire.play()
                            amount_bullets -= 1
                            break
                        elif amount_bullets == 0:
                            amount_bullets -= 1
                            start = time()
                            break

        if amount_bullets < 0:
            end = time()
            if end - start > 3:
                amount_bullets = 6

        window.blit(galaxy, (0, 0))

        for enemy in enemies:
            for bullet in bullets:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.rect.x = randint(0, 650)
                    enemy.rect.y = randint(-100, 0)
                    enemy.speed = randint(3, 10)
                    bullet.rect.x = rect.rect.x
                    bullet.rect.y = rect.rect.y + 10
                    bullet.speed = 0
                    numHit += 1
                    # break
        for aster in asteroids:
            for bullet in bullets:
                if bullet.rect.colliderect(aster.rect):
                    bullet.rect.x = rect.rect.x
                    bullet.rect.y = rect.rect.y + 10
                    bullet.speed = 0

        for aster in asteroids:
            aster.draw()

        for bullet in bullets:
            bullet.move()
            bullet.draw()

            if bullet.speed == 0:
                bullet.rect.x = rect.rect.x
                bullet.rect.y = rect.rect.y + 10
            if bullet.rect.y < 0:
                bullet.rect.x = rect.rect.x
                bullet.rect.y = rect.rect.y + 10
                bullet.speed = 0

        speed_enemies += 1
        for i in enemies:
            i.draw()
            if i.rect.y > 450 or i.rect.colliderect(rect.rect):
                i.rect.x = randint(0, 650)
                i.rect.y = randint(-100, 0)
                i.speed = randint(3, 10)
                numLose += 1
                break
        for i in asteroids:
            i.draw()
            if i.rect.y > 450 or i.rect.colliderect(rect.rect):
                i.rect.x = randint(0, 650)
                i.rect.y = randint(-100, 0)
                i.speed = randint(3, 10)
                numLose += 1
                break

        if speed_enemies == 10:
            for i in enemies:
                i.move()
            for i in asteroids:
                i.move()
            speed_enemies = 0

        hitPoint.setText(str(numHit))
        hitPoint.draw()

        losePoint.setText(str(numLose))
        losePoint.draw()

        point_label.draw()
        lose_point_label.draw()
        rect.draw()
        rect.move()
    elif gameStatus == 2:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                isGame = False
                quit()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_TAB:
                    numHit = 0
                    numLose = 0
                    gameStatus = 1
                    pygame.mixer.music.play()
                if i.key == pygame.K_ESCAPE:
                    isGame = False


    if numHit == 10:
        window.blit(win_label, (300, 200))
        window.blit(info_label, (80, 250))
        pygame.mixer.music.stop()
        gameStatus = 2
    if numLose == 3:
        window.blit(lose_label, (300, 200))
        window.blit(info_label, (80, 250))
        pygame.mixer.music.stop()
        gameStatus = 2

    clock.tick(60)
    pygame.display.update()