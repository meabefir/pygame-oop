import pygame
import os
from UIComp import UIComp
from LevelButtonComp import LevelButtonComp
from GameData import GameData
from CompContainer import CompContainer
from ButtonComp import ButtonComp


class LevelSelectorComp(CompContainer, UIComp):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

        self.levels = []

        self.load_level_buttons()

    def load_level_buttons(self):
        for f, sf, files in os.walk("levels"):
            for file in files:
                file_path = f + '\\' + file
                self.levels.append(file)

        size = (400, 70)
        y_start = 20
        margin = 10
        for i, level in enumerate(self.levels):
            level_name = level.split('.')[0]
            callback = self.load_level if level_name not in GameData.user.data["completed_levels"] and i <= len(
                GameData.user.data["completed_levels"]) else None
            background_color = pygame.Color("dodgerblue") if i <= len(
                GameData.user.data["completed_levels"]) else (255, 0, 0)

            new_level_button = LevelButtonComp(self.x + self.width / 2 - size[0] / 2,
                                               self.y + y_start + i * (size[1] + margin),
                                               size[0], size[1], level_name, 40,
                                               background_color, (255, 255, 255), None, callback,
                                               level_name)
            self.add_component(new_level_button)

        back_button = ButtonComp(self.x + self.width / 2 - size[0] / 2, self.y + self.height - size[1] - y_start,
                                 size[0],
                                 size[1],
                                 "Back", 40, pygame.Color("dodgerblue"), callback=self.load_menu, color=(255, 255, 255))
        self.add_component(back_button)

    def load_menu(self):
        self.parent.remove_component(self)
        self.parent.load_main_menu()

    def load_level(self, *args):
        GameData.game.load_level(args[0])
        self.parent.remove_component(self)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw_rect(win)

        self.draw(win)
