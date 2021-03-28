from UIComp import UIComp
from LabelComp import LabelComp
from GameData import GameData
from CompContainer import CompContainer
from Events import Events


class XpComp(CompContainer, UIComp):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

        self.init()

        Events.connect("set_xp", self, self.set_xp)

    def init(self):
        self.xp_label = LabelComp(self.x, self.y, self.width, self.height, f'XP: {GameData.user.data["xp"]}')
        self.add_component(self.xp_label)

        self.level_label = LabelComp(self.x, self.y + GameData.tile_size, self.width, self.height,
                                     f'Level: {GameData.user.data["level"]}')
        self.add_component(self.level_label)

    def set_xp(self, xp, level):
        self.xp_label.text = f'XP: {xp}'
        self.level_label.text = f'Level: {level}'

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw(win)
