#Создай собственный Шутер!
import pygame

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
while isGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGame = False
            exit()

    window.blit(galaxy, (0, 0))

    speed_enemies += 1
    for i in enemies:
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
        speed_enemies = 0

    hitPoint.setText(str(numHit))
    hitPoint.draw()

    losePoint.setText(str(numLose))
    losePoint.draw()

    point_label.draw()
    lose_point_label.draw()
    rect.draw()
    rect.move()
    clock.tick(60)
    pygame.display.update()