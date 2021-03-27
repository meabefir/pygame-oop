from Events import Events
from UIComp import UIComp
from GameData import GameData


class HeartsComp(UIComp):
    def __init__(self, x, y, width, height, sprite):
        UIComp.__init__(self, x, y, width, height)
        self.sprite = sprite
        self.hp = GameData.player_data["max_hp"]

        Events.connect("set_hp", self, self.set_hp)

    def set_hp(self, value):
        self.hp = value

    def self_handle_event(self, event):
        pass

    def self_update(self):
        pass

    def self_draw(self, win):
        for i in range(self.hp):
            self.sprite.self_draw(win, (i * self.sprite.width, 0))
