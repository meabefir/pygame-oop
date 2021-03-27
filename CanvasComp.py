from GameData import GameData
from LoginComp import LoginComp
from LevelSelectorComp import LevelSelectorComp
from UIComp import UIComp
from Events import Events
from PauseMenuComp import PauseMenuComp


class CanvasComp(UIComp):
    def __init__(self, x, y, width, height):
        UIComp.__init__(self, x, y, width, height)

        Events.connect("toggle_pause_menu", self, self.toggle_pause_menu)

        # self.load_login_menu()
        # self.load_level_selector()

    def self_handle_event(self, event):
        self.handle_event(event)
        pass

    def self_update(self):
        self.update()
        pass

    def self_draw(self, win):
        self.draw(win)
        pass

    def load_login_menu(self):
        new_login = LoginComp(0, 0, GameData.window_size[0], GameData.window_size[1])
        self.add_component(new_login)

    def load_main_menu(self):
        if GameData.user is None:
            return
        self.load_level_selector()

    def load_level_selector(self):
        size = (500, 700)
        level_selector = LevelSelectorComp(self.x + self.width / 2 - size[0] / 2,
                                           self.y + self.height / 2 - size[1] / 2, size[0], size[1])
        self.add_component(level_selector)

    def toggle_pause_menu(self):
        pause_menu_comp = self.has_component_of_class(PauseMenuComp)
        if pause_menu_comp is None:
            size = (500, 600)
            start_y = 100
            new_pause_menu = PauseMenuComp(self.x + self.width / 2 - size[0] / 2, self.y + start_y, size[0], size[1])
            self.add_component(new_pause_menu)
        else:
            self.remove_component(pause_menu_comp)
