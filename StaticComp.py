import pygame
from Vector2 import Vector2
from CompContainer import CompContainer


class StaticComp(CompContainer):
    def __init__(self, x, y, width, height, sprite):
        CompContainer.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.sprite = sprite
        self.position = Vector2(x, y)

    def self_draw(self, win):
        self.draw(win)
        self.sprite.draw(win)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()
