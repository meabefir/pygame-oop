import pygame
from CompContainer import CompContainer
from UIComp import UIComp
from InputComp import InputComp
from ButtonComp import ButtonComp
from Database import Database
from User import User
from GameData import GameData


class LoginComp(UIComp, CompContainer):
    def __init__(self, x, y, width, height):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)

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
        self.username_input = InputComp(100, 100, 200, 50, "username", 44, 5, "test")
        self.add_component(self.username_input)
        # register input
        self.password_input = InputComp(100, 200, 200, 50, "password", 44, 5, "test")
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
        result = Database.attempt_register(register_data)

        if result is not None:
            user = User(result)
            GameData.user = user

            self.parent.remove_component(self)
            self.parent.load_main_menu()
