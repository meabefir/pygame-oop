from CompContainer import CompContainer
from UIComp import UIComp
from Sprite import Sprite
from LabelComp import LabelComp
from GameData import GameData
from Events import Events


class CoinsComp(CompContainer, UIComp):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

        self.init()

        Events.connect("coin_picked", self, self.coin_picked)

    def init(self):
        # create coin sprite
        coins_sprite = Sprite('coins', GameData.tile_size, GameData.tile_size, self.x, self.y, ui_sprite=True)
        coins_label = LabelComp(self.x + GameData.tile_size, self.y, GameData.tile_size, GameData.tile_size, '0', 40,
                                color=(255, 255, 255))
        self.add_component(coins_sprite)
        self.add_component(coins_label)

    def coin_picked(self, *args):
        coins_label = self.has_component_of_class(LabelComp)
        coins_label.text = str(int(coins_label.text) + 1)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw(win)
