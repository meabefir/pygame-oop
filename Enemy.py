import pygame
import random
from DynamicComp import DynamicComp
from CompContainer import CompContainer
from Vector2 import Vector2
from GameTime import GameTime
from Pathfinder import Pathfinder
from GameData import GameData
from Physics import Physics
from Input import Input


class Enemy(DynamicComp, CompContainer):
    def __init__(self, x, y, width, height, sprite):
        DynamicComp.__init__(self, x, y, width, height, sprite)
        CompContainer.__init__(self)
        self.input_vector = Vector2()
        self.speed = 200
        self.follow_distance = 3

    def self_handle_event(self):
        pass

    def self_update(self):
        # choose random destination
        # if self.destination is None:
        #     free_cells = self.get_free_cells()
        #     if len(free_cells) == 0:
        #         return
        #     random_free_cell = free_cells[random.randint(0, len(free_cells) - 1)]
        #     self.move_to_cell(random_free_cell)

        # follow player if ready to move
        if self.destination is None:
            dir = Pathfinder.get_smaller_cell_dir(self.position)
            cell_value = Pathfinder.get_cell_value(self.position)
            if dir is not None and cell_value <= self.follow_distance:
                self.move_to_cell(dir)

        # if it has a destination
        if self.destination is not None:
            # print(self.position,self.destination)
            movement_vec = self.position.move_towards(self.destination, self.speed * GameTime.delta) - self.position
            if self.position + movement_vec == self.destination:
                self.destination = None
                self.move(movement_vec)
            else:
                self.move(movement_vec)
