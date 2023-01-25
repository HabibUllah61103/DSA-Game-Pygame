from setting import *
import pygame as pg
import math

class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = Player_pos
        self.angle = Player_angle

    def move(self, direction, rotation):
        pass

    def update(self):
        self.move()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
