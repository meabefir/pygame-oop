import pygame
from UIComp import UIComp


class LabelComp(UIComp):
    def __init__(self, x, y, width, height, text="", font_size=32, color=pygame.Color("black")):
        UIComp.__init__(self, x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.color = color

    def self_draw(self, win):
        if self.text != '':
            lines = self.text.split("\n")
            for i, text_line in enumerate(lines):
                font = pygame.font.SysFont('comicsans', self.font_size)
                text = font.render(text_line, 1, self.color)
                win.blit(text,
                         (self.x + (self.width / 2 - text.get_width() / 2),
                          self.y + (self.height / 2 - text.get_height() * (len(lines) - i))))

    def self_handle_event(self):
        pass

    def self_update(self):
        pass
