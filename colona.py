import random
from setting import *

import pygame as pg


class Colona(pg.sprite.Sprite):
    def __init__(self,y,speed_x):
        super().__init__()
        colona = pg.image.load("Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png")
        self.image = colona.subsurface(pg.Rect(0,0, 32, 80))
        self.image = pg.transform.scale(self.image, (64, 128))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = SCREEN_WIDTH
        self.speed_x = speed_x


    def update(self):
        self.rect.x -= self.speed_x


