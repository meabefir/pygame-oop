from Vector2 import Vector2


class Camera:
    def __init__(self, size, follows=None):
        self.follows = None
        self.size = size
        self.position = follows.position if follows is not None else Vector2()

    def self_handle_event(self, event):
        pass

    def self_update(self):
        if self.follows is not None:
            self.position = self.follows.position - self.size / 2

    def self_draw(self, win):
        pass
