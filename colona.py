import random
from setting import *

import pygame as pg


class Colona(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        colona = pg.image.load("Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png")
        self.image = colona.subsurface(pg.Rect(0,0, 32, 80))
        self.image = pg.transform.scale(self.image, (64, 128))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,500)
        self.rect.x = SCREEN_WIDTH
        self.speed_x = 5


    def update(self):
        self.rect.x -= self.speed_x

