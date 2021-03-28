import pygame
from UIComp import UIComp
from LabelComp import LabelComp
from ButtonComp import ButtonComp
from CompContainer import CompContainer


class MainMenuComp(CompContainer, UIComp):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

        self.init()

    def init(self):
        size = (300, 100)
        start_y = 50
        new_label = LabelComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y, size[0], size[1] * 2,
                              "Main Menu", 50)
        self.add_component(new_label)

        play_button = ButtonComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y + 300, size[0], size[1],
                                 "Play", 40, pygame.Color("dodgerblue"), (255, 255, 255), None,
                                 self.load_levels_selector,
                                 )
        self.add_component(play_button)

        stats_button = play_button = ButtonComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y + 420, size[0],
                                                size[1],
                                                "Stats", 40, pygame.Color("dodgerblue"), (255, 255, 255), None,
                                                self.load_user_stats,
                                                )
        self.add_component(stats_button)

        quit_button = ButtonComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y + 540, size[0],
                                                size[1],
                                                "Quit to login", 40, pygame.Color("dodgerblue"), (255, 255, 255), None,
                                                self.quit_to_login,
                                                )
        self.add_component(quit_button)

    def load_levels_selector(self):
        self.parent.remove_component(self)
        self.parent.load_level_selector()

    def load_user_stats(self):
        self.parent.remove_component(self)
        self.parent.load_user_stats()

    def quit_to_login(self):
        self.parent.remove_component(self)
        self.parent.load_login_menu()

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw(win)
        self.draw_rect(win)
