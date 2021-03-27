from GameTime import GameTime


class Timer():
    def __init__(self, callback):
        self.time = None
        self.time_passed = None
        self.callback = callback

    def start(self, time):
        self.time = time
        self.time_passed = 0

    def self_handle_event(self, event):
        pass

    def self_update(self):
        if self.time is not None:
            self.time_passed += GameTime.delta
            if self.time_passed >= self.time:
                self.time = None
                self.time_passed = None
                self.callback()

    def self_draw(self, win):
        pass
