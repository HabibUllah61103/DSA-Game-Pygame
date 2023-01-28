import pygame as pg
import sys
from setting import *
from maps import *
from player import *
from raycasting import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Maps(self)
        self.player = Player(self)
        self.ray_casting = RayCasting(self)

    def update(self):
        self.player.update()
        self.ray_casting.update()
        pg.display.flip()
        self.clock.tick(FPS)
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps():.2f}") 

    def draw(self):
        self.screen.fill('BLACK')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()