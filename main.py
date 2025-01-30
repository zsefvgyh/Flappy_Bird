import pygame as pg

from bird import Bird

from colona import Colona

from setting import *




class Game(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bird = Bird()
        self.background = pg.image.load('Flappy Bird Assets/Background/Background6-Sheet.png')
        self.background = pg.transform.scale(self.background,(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.colona = pg.sprite.Group()
        self.timer = pg.time.get_ticks()
        self.delay = 1000


        self.run()




    def setup(self):
        pass

    def run(self):
        self.is_running = True
        while self.is_running:
            self.draw()
            self.event()
            self.update()
            self.clock.tick(10)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

    def update(self):
        self.bird.update()
        self.colona.update()
        if pg.time.get_ticks() - self.timer > self.delay:
            self.colona.add(Colona())
            self.timer = pg.time.get_ticks()


        pass


    def draw(self):
        self.screen.blit(self.background,(0, 0))
        self.bird.draw(self.screen)
        self.colona.draw(self.screen)
        pg.display.flip()





if __name__ == "__main__":
    game = Game()
