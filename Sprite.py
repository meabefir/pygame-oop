import pygame
from Vector2 import Vector2
from TextureLoader import textures


class Sprite:
    def __init__(self, texture_name, width, height, x, y):
        self.name = texture_name
        self.surface = textures[texture_name]
        self.width = width
        self.height = height
        self.position = Vector2(x, y)

    def draw(self, win):
        win.blit(pygame.transform.scale(self.surface, (self.width, self.height)),
                 (int(self.position.x), int(self.position.y)))

    def self_handle_event(self, event):
        pass

    def self_update(self):
        pass

    def self_draw(self, win):
        win.blit(pygame.transform.scale(self.surface, (self.width, self.height)),
                 (int(self.position.x), int(self.position.y)))
