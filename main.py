
from random import randint
from pygame import *
from time import time as timer

window = display.set_mode((700, 500))
background = transform.scale(image.load("4.png"), (700, 600))


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
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if key_pressed[K_RIGHT] and self.rect.x < 700 - 65 - 5:
            self.rect.x += 5
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if key_pressed[K_RIGHT] and self.rect.x < 700 - 65 - 5:
            self.rect.x += 5


clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
