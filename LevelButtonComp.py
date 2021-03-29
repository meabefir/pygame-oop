from ButtonComp import ButtonComp
from GameData import GameData
from Sprite import Sprite


class LevelButtonComp(ButtonComp):
    def __init__(self, x, y, width, height, text='', font_size=32, background_color=(255, 255, 255), color=(0, 0, 0),
                 outline_color=None, callback=None, *args):
        ButtonComp.__init__(self, x, y, width, height, text, font_size, background_color, color,
                            outline_color, callback, *args)

        self.init()

    def init(self):
        if self.text in GameData.user.data["completed_levels"]:
            # create checkmark
            new_checkmark = Sprite("check", self.height, self.height, self.x + self.width - self.height, self.y,
                                   ui_sprite=True)
            self.add_component(new_checkmark)
