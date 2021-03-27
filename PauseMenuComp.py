import pygame
from UIComp import UIComp
from LabelComp import LabelComp


class PauseMenuComp(UIComp):
    def __int__(self, x, y, width, height):
        UIComp.__init__(x, y, width, height)

        self.init()

    def init(self):
        size = (400, 200)
        start_y = 100
        new_label = LabelComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y, size[0], size[1],
                              "Press ESCAPE to\nunpause the game", 32)
        self.add_component(new_label)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw_rect(win)
        self.draw_full_rect(win, (255, 255, 255, 120))
        self.draw(win)
