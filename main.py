import random

import pygame as pg

from bird import Bird
from colona import Colona
from setting import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pg.image.load('Flappy Bird Assets/Background/Background6-Sheet.png')
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score = 0
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 72)
        self.game_score = self.font.render(str(self.score), True, (115, 81, 132))
        self.game_score_rect = self.game_score.get_rect(topleft=(10, 10))
        self.game_over_text = self.font.render("Вы проиграли", True, (25, 100, 100))
        self.game_over_text_rect = self.game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        self.setup()
        self.run()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.draw()
            self.event()
            self.update()
            self.clock.tick(40)

    def setup(self):
        self.bird = Bird()
        self.score = 0
        self.speed = 5
        self.game_score = self.font.render(str(self.score), True, (115, 81, 132))
        self.game_score_rect = self.game_score.get_rect(topleft=(10, 10))
        self.colona = pg.sprite.Group()
        self.mode = "game"
        self.timer = pg.time.get_ticks()
        self.delay = 1000

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            if self.mode == "end":
                if event.type == pg.KEYDOWN:
                    self.setup()

    def update(self):
        if self.bird.rect.y > SCREEN_HEIGHT:
            self.mode = "end"
            return
        if pg.sprite.spritecollide(self.bird, self.colona, False):
            self.mode = "end"
            return

        self.bird.update()
        self.colona.update()

        if pg.time.get_ticks() - self.timer > self.delay:
            self.score += 1
            self.speed += 1
            self.game_score = self.font.render(str(self.score), True, (115, 81, 132))
            gap = random.randint(50, 100)
            y = random.randint(128, SCREEN_HEIGHT - 256)
            self.colona.add(Colona(y - gap, self.speed))
            self.colona.add(Colona(y + gap + 128, self.speed))
            self.timer = pg.time.get_ticks()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.draw(self.screen)
        self.colona.draw(self.screen)
        self.screen.blit(self.game_score, self.game_score_rect)

        if self.mode == "end":
            self.screen.fill(pg.Color(0, 0, 0, 100))
            self.game_score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            self.screen.blit(self.game_score, self.game_score_rect)

            self.screen.blit(self.game_over_text, self.game_over_text_rect)
        pg.display.flip()


if __name__ == "__main__":
    game = Game()
