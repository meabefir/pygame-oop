import pygame, sys


class Input:
    held = {}
    pressed = {}
    released = {}

    @staticmethod
    def handle_input(event):
        # reset pressed
        for key in Input.pressed:
            Input.pressed[key] = False
        # reset released
        for key in Input.released:
            Input.released[key] = False

        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            Input.held[event.key] = True
            Input.pressed[event.key] = True
        if event.type == pygame.KEYUP:
            Input.held[event.key] = False
            Input.released[event.key] = True

    @staticmethod
    def is_held(key):
        if key in Input.held:
            return Input.held[key]

    @staticmethod
    def is_just_pressed(key):
        if key in Input.pressed and Input.pressed[key]:
            return True
        return False

    @staticmethod
    def is_just_released(key):
        if key in Input.released and Input.released[key]:
            return True
        return False
