from GameTime import GameTime
from UIComp import UIComp
from LabelComp import LabelComp
from CompContainer import CompContainer


class FPSCounter(UIComp, CompContainer):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

        self.init()

    def init(self):
        self.label_comp = LabelComp(self.x, self.y, self.width, self.height, "FPS: ", 32, center = False)

        self.add_component(self.label_comp)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.label_comp.text = f'FPS: {int(1 / GameTime.delta if GameTime.delta != 0 else 1)}'

    def self_draw(self, win):
        self.draw(win)
