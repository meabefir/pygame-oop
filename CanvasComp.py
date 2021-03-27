from CompContainer import CompContainer
from GameData import GameData
from LoginComp import LoginComp


class CanvasComp(CompContainer):
    def __init__(self):
        CompContainer.__init__(self)

        self.load_login_menu()

    def self_handle_event(self, event):
        self.handle_event(event)
        pass

    def self_update(self):
        self.update()
        pass

    def self_draw(self, win):
        self.draw(win)
        pass

    def load_login_menu(self):
        new_login = LoginComp(0, 0, GameData.window_size[0], GameData.window_size[1])
        self.add_component(new_login)
