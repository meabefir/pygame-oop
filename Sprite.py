import pygame
from Vector2 import Vector2
from TextureLoader import textures
from Camera import Camera


class Sprite:
    def __init__(self, texture_name, width, height, x, y, alpha=255, ui_sprite=False):
        self.name = texture_name
        self.surface = textures[texture_name]
        self.width = width
        self.height = height
        self.alpha = alpha
        self.ui_sprite = ui_sprite
        self.position = Vector2(x, y)

    def set_alpha(self, value):
        self.alpha = value

    def draw(self, win):
        draw_x = int(self.position.x)
        draw_y = int(self.position.y)
        if self.ui_sprite is False:
            draw_x = int(self.position.x - Camera.position.x)
            draw_y = int(self.position.y - Camera.position.y)
        win.blit(pygame.transform.scale(self.surface, (self.width, self.height)),
                 (draw_x, draw_y))

    def self_handle_event(self, event):
        pass

    def self_update(self):
        pass

    def self_draw(self, win, offset=(0, 0)):
        surface_to_draw = pygame.transform.scale(self.surface, (self.width, self.height))
        draw_x = int(self.position.x + offset[0])
        draw_y = int(self.position.y + offset[1])
        if self.ui_sprite is False:
            draw_x = int(self.position.x + offset[0] - Camera.position.x)
            draw_y = int(self.position.y + offset[1] - Camera.position.y)
        if self.alpha != 255:
            temp_s = pygame.Surface((self.width, self.height))
            temp_s.set_alpha(self.alpha)
            temp_s.blit(surface_to_draw, (0, 0))
            win.blit(temp_s, (draw_x, draw_y),
                     special_flags=pygame.BLEND_RGBA_ADD)
        else:
            win.blit(surface_to_draw,
                     (draw_x, draw_y))
