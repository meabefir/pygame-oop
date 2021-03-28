import pygame
from UIComp import UIComp


class LabelComp(UIComp):
    def __init__(self, x, y, width, height, text="", font_size=32, color=pygame.Color("black"), center=True):
        UIComp.__init__(self, x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.color = color
        self.center = center

    def self_draw(self, win):
        if self.text != '':
            lines = self.text.split("\n")
            lines_count = len(lines)
            space_for_one = self.height / (lines_count + 1)
            for i, text_line in enumerate(lines):
                font = pygame.font.SysFont('comicsans', self.font_size)
                text = font.render(text_line, 1, self.color)
                draw_x = self.x + (self.width / 2 - text.get_width() / 2)
                draw_y = self.y + (i + 1) * (space_for_one - text.get_height() / 2)
                if self.center is False:
                    draw_x = self.x
                win.blit(text, (draw_x, draw_y))

    def self_handle_event(self, event):
        pass

    def self_update(self):
        pass
