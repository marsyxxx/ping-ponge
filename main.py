
from random import randint
from pygame import *
from time import time as timer

window = display.set_mode((700, 500))
background = transform.scale(image.load("4.png"), (700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if key_pressed[K_s] and self.rect.y < 500 - 150 - 5:
            self.rect.y += 5
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if key_pressed[K_DOWN] and self.rect.y < 500 - 150 - 5:
            self.rect.y += 5

palka1 = Player("palk.png", 5, 20, 50, 10, 150)
sharik = GameSprite("sharik.png", 5, 350,250, 50, 50)
palka2 = Player("palk.png", 5, 680, 50, 10, 150)

speed_x = 3
speed_y = -3

clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0,0))

    sharik.rect.x += speed_x
    sharik.rect.y += speed_y

    if sharik.rect.x > 700 - 50 - 5:
        window.fill((255, 0, 0))

    if sharik.rect.y > 500 - 50 - 5:
        speed_y *= -1

    if sharik.rect.y < 0:
        speed_y *= -1

    sharik.reset()
    palka1.reset()
    palka2.reset()
    palka1.update_l()
    palka2.update_r()
    sharik.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
