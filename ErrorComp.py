from UIComp import UIComp
from CompContainer import CompContainer
from LabelComp import LabelComp
from Timer import Timer


class ErrorComp(CompContainer, UIComp):
    def __init__(self, x, y, width, height, text):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)
        self.text = text
        self.duration = 1

        self.init()

    def init(self):
        new_label = LabelComp(self.x, self.y, self.width, self.height, self.text, 40)
        self.add_component(new_label)

        timer = Timer(self.free)
        self.add_component(timer)
        timer.start(self.duration)

    def free(self):
        self.parent.remove_component(self)

    def self_handle_event(self, event):
        self.handle_event(event)

    def self_update(self):
        self.update()

    def self_draw(self, win):
        self.draw_full_rect(win, (255, 0, 0, 180))
        self.draw(win)
