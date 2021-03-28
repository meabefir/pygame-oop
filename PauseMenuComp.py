import pygame
from UIComp import UIComp
from LabelComp import LabelComp
from CompContainer import CompContainer
from ButtonComp import ButtonComp
from GameData import GameData


class PauseMenuComp(CompContainer, UIComp):
    def __init__(self, x, y, width, height):
        UIComp.__init__(self, x, y, width, height)
        CompContainer.__init__(self)

        self.init()

    def init(self):
        size = (200, 100)
        start_y = 50
        new_label = LabelComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y, size[0], size[1]*2,
                              "Press ESCAPE to\nunpause the game", 45)
        self.add_component(new_label)

        menu_button = ButtonComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y + 300, size[0], size[1],
                                 "Main Menu", 40, pygame.Color("dodgerblue"), (0, 0, 0), None, self.load_main_menu)
        self.add_component(menu_button)

    def load_main_menu(self):
        self.parent.load_main_menu()
        self.parent.remove_component(self)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw_rect(win)
        self.draw_full_rect(win, (255, 255, 255, 120))
        self.draw(win)
