from setting import *
import pygame as pg
import math

class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = Player_pos
        self.angle = Player_angle

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = Player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx -= speed_sin
            dy += speed_cos
        if keys[pg.K_d]:
            dx += speed_sin
            dy -= speed_cos

        self.x += dx
        self.y += dy

        if keys[pg.K_LEFT]:
            self.angle -= Player_rotation * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += Player_rotation * self.game.delta_time
        self.angle %= 2 * math.pi


    def draw(self):
        pg.draw.line(self.game.screen, 'RED', (self.x*100, self.y*100),
                     (self.x*100 + WIDTH*math.cos(self.angle), self.y*100 + WIDTH*math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'Green', (int(self.x*100), int(self.y*100)), 15)


    def update(self):
        self.move()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
