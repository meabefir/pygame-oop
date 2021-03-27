import pygame
from DynamicComp import DynamicComp
from CompContainer import CompContainer
from Vector2 import Vector2
from GameTime import GameTime
from Input import Input
from GameData import GameData
from Pathfinder import Pathfinder

directions = {
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
}


class Player(DynamicComp, CompContainer):
    def __init__(self, x, y, width, height, sprite):
        DynamicComp.__init__(self, x, y, width, height, sprite)
        CompContainer.__init__(self)
        self.input_vector = Vector2()
        self.speed = 300

        GameData.player = self

    def self_handle_event(self, event):
        if self.destination is None:
            free_cells = self.get_free_cells()
            for key in directions:
                if Input.is_held(key) and directions[key] in free_cells:
                    self.move_to_cell(directions[key])

    def self_update(self):
        # if it has a destination to reach
        if self.destination is not None:
            movement_vec = self.position.move_towards(self.destination, self.speed * GameTime.delta) - self.position

            # if reached destionation
            if self.position + movement_vec == self.destination:
                self.destination = None
                self.move(movement_vec)
                Pathfinder.update_table()
            else:
                self.move(movement_vec)