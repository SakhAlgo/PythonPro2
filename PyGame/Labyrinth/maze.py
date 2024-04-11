# создай игру "Лабиринт"!
import pygame

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((700, 500))
fon = pygame.image.load('background.jpg').convert()
fon = pygame.transform.scale(fon, (700, 500))
window.blit(fon, (0, 0))

pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

kick = pygame.mixer.Sound('kick.ogg')
money = pygame.mixer.Sound('money.ogg')
class Wall:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

class Sprite:
    def __init__(self, filename, x, y, width, height):
        image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.flag = 'left'

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 650:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < 450:
            self.rect.y += 5

class Enemy(Sprite):
    def move(self):
        if self.flag == 'left':
            self.speed = -5
        elif self.flag == 'right':
            self.speed = 5

        if self.flag == 'left' and self.rect.x < 500:
            self.flag = 'right'
        if self.rect.x > 630 and self.flag == 'right':
            self.flag = 'left'
        self.rect.x += self.speed

hero = Player('hero.png', 20, 400, 50, 50)
cyborg = Enemy('cyborg.png', 630, 300, 50, 50)
treasure = Sprite('treasure.png', 630, 400, 50, 50)

itterations_enemy = 0

walls = []

wall1 = Wall(100, 100, 20, 400, (25,0,0))
wall2= Wall(400, 100, 20, 400, (25,0,0))
wall3 = Wall(400, 300, 200, 20, (25,0,0))
wall4 = Wall(250, 0, 20, 300, (25,0,0))

walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)

font = pygame.font.SysFont('verdana', 40)
win_label = font.render('YOU WIN', True, (255,0,0))
lose_label = font.render('OPPS!!', True, (0,255,0))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    window.blit(fon, (0, 0))
    for wall in walls:
        wall.draw()
        if wall.rect.colliderect(hero.rect) or hero.rect.colliderect(cyborg.rect):
            kick.play()
            window.blit(lose_label, (300, 200))
            hero.rect.x = 20
            hero.rect.y = 400
            # game = False

    if treasure.rect.colliderect(hero.rect):
        money.play()
        window.blit(win_label, (300, 200))
        # game = False

    hero.draw()
    hero.control()

    cyborg.draw()
    itterations_enemy += 1
    if itterations_enemy == 10:
        print(cyborg.rect.x)
        cyborg.move()
        cyborg.draw()
        itterations_enemy = 0
    treasure.draw()

    clock.tick(60)
    pygame.display.update()
