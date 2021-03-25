import pygame
from Vector2 import Vector2
from Physics import Physics


class StaticComp:
    def __init__(self, x, y, width, height, sprite):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.sprite = sprite
        self.position = Vector2(x, y)

        Physics.add_solid(self)

    def self_draw(self, win):
        self.sprite.draw(win)

    def self_handle_event(self):
        pass

    def self_update(self):
        pass
