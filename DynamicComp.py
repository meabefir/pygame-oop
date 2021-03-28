import pygame
from CompContainer import CompContainer
from Vector2 import Vector2
from Physics import Physics
from GameData import GameData
import random


class DynamicComp(CompContainer):
    def __init__(self, x, y, width, height, sprite):
        CompContainer.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.sprite = sprite
        self.position = Vector2(x, y)
        self.velocity = Vector2()
        self.destination = None

        self.add_component(self.sprite)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw(win)

    def move(self, move_vec):
        # horizontal collisions
        self.position.x += move_vec.x
        self.rect.left = int(self.position.x)
        collisions = Physics.get_collisions(self)

        for collided_with in collisions:
            if move_vec.x > 0:
                self.rect.right = collided_with.rect.left
                self.position.x = self.rect.x
            if move_vec.x < 0:
                self.rect.left = collided_with.rect.right
                self.position.x = self.rect.x

        # vertical collision
        self.position.y += move_vec.y
        self.rect.top = int(self.position.y)
        collisions = Physics.get_collisions(self)

        for collided_with in collisions:
            if move_vec.y > 0:
                self.rect.bottom = collided_with.rect.top
                self.position.y = self.rect.y
            if move_vec.y < 0:
                self.rect.top = collided_with.rect.bottom
                self.position.y = self.rect.y

        # self.position = self.position.to_int()
        self.sprite.position = self.position
        self.rect = pygame.Rect(int(self.position.x), int(self.position.y), self.rect.width, self.rect.height)

    def move_to_random_free_cell(self):
        free_cells = self.get_free_cells()
        if len(free_cells):
            self.move_to_cell(free_cells[random.randint(0, len(free_cells) - 1)])

    def get_free_cells(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        free_cells = []
        for direction in directions:
            temp_rect = pygame.Rect(self.position.x + direction[0] * GameData.tile_size,
                                    self.position.y + direction[1] * GameData.tile_size,
                                    self.rect.width,
                                    self.rect.height)
            temp_collisions = Physics.get_rect_collisions(temp_rect)
            if len(temp_collisions) == 0:
                free_cells.append(direction)
        return free_cells

    def move_to_cell(self, cell):
        movement = Vector2(cell[0], cell[1]) * GameData.tile_size
        self.destination = self.position + movement
