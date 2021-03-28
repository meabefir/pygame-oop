import pygame
from Vector2 import Vector2
from TextureLoader import textures


class Sprite:
    def __init__(self, texture_name, width, height, x, y, alpha=255):
        self.name = texture_name
        self.surface = textures[texture_name]
        self.width = width
        self.height = height
        self.alpha = alpha
        self.position = Vector2(x, y)

    def set_alpha(self, value):
        self.alpha = value

    def draw(self, win):
        win.blit(pygame.transform.scale(self.surface, (self.width, self.height)),
                 (int(self.position.x), int(self.position.y)))

    def self_handle_event(self, event):
        pass

    def self_update(self):
        pass

    def self_draw(self, win, offset=(0, 0)):
        surface_to_draw = pygame.transform.scale(self.surface, (self.width, self.height))
        if self.alpha != 255:
            temp_s = pygame.Surface((self.width, self.height))
            temp_s.set_alpha(self.alpha)
            temp_s.blit(surface_to_draw, (0, 0))
            win.blit(temp_s, (int(self.position.x + offset[0]), int(self.position.y + offset[1])),
                     special_flags=pygame.BLEND_RGBA_ADD)
        else:
            win.blit(surface_to_draw,
                     (int(self.position.x + offset[0]), int(self.position.y + offset[1])))
