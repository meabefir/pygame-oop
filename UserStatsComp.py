import pygame
from UIComp import UIComp
from CompContainer import CompContainer
from ButtonComp import ButtonComp
from GameData import GameData
from LabelComp import LabelComp
from Database import Database

class UserStatsComp(UIComp, CompContainer):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

        self.init()

    def init(self):
        user_data = GameData.user.data
        y_start = 20
        size = (400, 200)

        username_label = LabelComp(self.x + self.width / 2 - size[0] / 2, self.y + y_start, size[0], 50,
                                   f'{user_data["username"]}', 44)
        self.add_component(username_label)

        # levels completed label
        text = "Levels completed:\n"
        for level_name in user_data["completed_levels"]:
            text += f'{level_name}\n'
        if len(user_data["completed_levels"]) == 0:
            text += "No levels completed"

        levels_label = LabelComp(self.x + self.width / 2 - size[0] / 2, username_label.bottom + y_start, size[0],
                                 size[1], text, 32)
        self.add_component(levels_label)

        coins_label = LabelComp(self.x + self.width / 2 - size[0] / 2, levels_label.bottom + y_start, size[0],
                                size[1] / 2,
                                f'Coins collected: {user_data["coins"]}', 32)
        self.add_component(coins_label)

        level_label = LabelComp(self.x + self.width / 2 - size[0] / 2, coins_label.bottom + y_start, size[0],
                                size[1] / 2,
                                f'Level: {user_data["level"]}', 32)
        self.add_component(level_label)

        # back button
        size = (400, 70)
        back_button = ButtonComp(self.x + self.width / 2 - size[0] / 2, self.y + self.height - size[1] - y_start,
                                 size[0],
                                 size[1],
                                 "Back", 40, pygame.Color("dodgerblue"), callback=self.load_menu, color=(255, 255, 255))
        self.add_component(back_button)

    def load_menu(self):
        self.parent.remove_component(self)
        self.parent.load_main_menu()

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw(win)
        self.draw_rect(win)
