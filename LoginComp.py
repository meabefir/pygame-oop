import pygame
from CompContainer import CompContainer
from UIComp import UIComp
from InputComp import InputComp
from ButtonComp import ButtonComp
from Database import Database
from User import User
from GameData import GameData
from ErrorComp import ErrorComp


class LoginComp(UIComp, CompContainer):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)
        self.min_len = 6

        self.init()

    def self_handle_event(self, event):
        self.handle_event(event)
        pass

    def self_update(self):
        self.update()
        pass

    def self_draw(self, win):
        self.draw(win)
        pass

    def init(self):
        # login input
        self.username_input = InputComp(100, 100, 200, 50, "username", 44, 5, "")
        self.add_component(self.username_input)
        # register input
        self.password_input = InputComp(100, 200, 200, 50, "password", 44, 5, "")
        self.add_component(self.password_input)
        # login button
        new_login_button = ButtonComp(100, 300, 200, 50, "Login", 44, pygame.Color("dodgerblue"), pygame.Color("Black"),
                                      pygame.Color("lightskyblue3"),
                                      self.attempt_login)
        self.add_component(new_login_button)
        # register button
        new_register_button = ButtonComp(100, 400, 200, 50, "Register", 44, pygame.Color("dodgerblue"),
                                         pygame.Color("Black"), pygame.Color("lightskyblue3"), self.attempt_register)
        self.add_component(new_register_button)

    def attempt_login(self, *args):
        login_data = {
            "username": self.username_input.text,
            "password": self.password_input.text,
        }

        result = Database.attempt_login(login_data)

        if result is None:
            # create error comp
            self.create_error_comp("Wrong credentials!")

        if result is not None:
            user = User(result)
            GameData.user = user

            self.parent.remove_component(self)
            self.parent.load_main_menu()

    def attempt_register(self, *args):
        register_data = {
            "username": self.username_input.text,
            "password": self.password_input.text,
        }

        if len(register_data['username']) < self.min_len:
            self.create_error_comp("Username must have\nat least 6 characters")
            return
        if len(register_data['password']) < self.min_len:
            self.create_error_comp("Password must have\nat least 6 characters")
            return

        result = Database.attempt_register(register_data)

        if result is None:
            self.create_error_comp("Username not available!")

        if result is not None:
            user = User(result)
            GameData.user = user

            self.parent.remove_component(self)
            self.parent.load_main_menu()

    def create_error_comp(self, text):
        error_comp = self.has_component_of_class(ErrorComp)
        if error_comp:
            self.remove_component(error_comp)
        size = (400, 100)
        new_error_comp = ErrorComp(GameData.window_size[0] / 2 - size[0] / 2, 50, size[0], size[1],
                                   text)
        self.add_component(new_error_comp)
