import pygame
import random
from DynamicComp import DynamicComp
from CompContainer import CompContainer
from Vector2 import Vector2
from GameTime import GameTime
from GameData import GameData


class Enemy(DynamicComp, CompContainer):
    def __init__(self, x, y, width, height, sprite):
        DynamicComp.__init__(self, x, y, width, height, sprite)
        CompContainer.__init__(self)
        self.input_vector = Vector2()
        self.speed = 100
        self.destination = None

    def self_handle_event(self):
        pass

    def self_update(self):
        if self.destination is None:
            random_dir = Vector2(random.randint(-1, 1), random.randint(-1, 1)) * GameData.tile_size
            self.destination = self.position + random_dir

        if self.destination is not None:
            movement_vec = self.position.move_towards(self.destination, self.speed * GameTime.delta) - self.position
            if self.position + movement_vec == self.destination:
                self.destination = None
            else:
                self.move(movement_vec)
