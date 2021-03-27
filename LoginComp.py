import pygame
from CompContainer import CompContainer
from UIComp import UIComp
from InputComp import InputComp
from ButtonComp import ButtonComp


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
        new_input = InputComp(100, 100, 200, 50, "username", 44, 5)
        self.add_component(new_input)
        # register input
        new_register = InputComp(100, 200, 200, 50, "password", 44, 5)
        self.add_component(new_register)
        # login button
        new_login_button = ButtonComp(100, 300, 200, 50, "Login", 44, pygame.Color("dodgerblue"), pygame.Color("Black"),
                                      pygame.Color("lightskyblue3"),
                                      self.attempt_login)
        self.add_component(new_login_button)
        # register button
        new_register_button = ButtonComp(100, 400, 200, 50, "Register", 44, pygame.Color("dodgerblue"),
                                         pygame.Color("Black"), pygame.Color("lightskyblue3"), self.attempt_register)
        self.add_component(new_register_button)

    def attempt_login(self):
        print("login pressed")

    def attempt_register(self):
        print("Register")
