import pygame as pg

from setting import *

class Bird:
    def __init__(self):
        super().__init__()

        bird = pg.image.load('Flappy Bird Assets/Player/StyleBird1/Bird1-1.png')
        self.image = bird.subsurface(pg.Rect(0 ,0 ,16 ,16))
        self.image = pg.transform.scale(self.image, ( 32,32))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.velocity_y = 0
        self.gravity = 1
    def update(self):
        self.velocity_y += self.gravity
        if pg.mouse.get_pressed()[0]:
            self.velocity_y = -10
        self.rect.y += self.velocity_y

    def draw(self,screen):
        screen.blit(self.image, self.rect)


