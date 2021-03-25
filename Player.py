import pygame
from DynamicComp import DynamicComp
from CompContainer import CompContainer
from Vector2 import Vector2
from GameTime import GameTime
from Input import Input


class Player(DynamicComp, CompContainer):
    def __init__(self, x, y, width, height, sprite):
        DynamicComp.__init__(self, x, y, width, height, sprite)
        CompContainer.__init__(self)
        self.input_vector = Vector2()
        self.speed = 300

    def self_handle_event(self):
        self.input_vector = Vector2()
        if Input.is_held(pygame.K_a):
            self.input_vector.x -= 1
        if Input.is_held(pygame.K_d):
            self.input_vector.x += 1
        if Input.is_held(pygame.K_w):
            self.input_vector.y -= 1
        if Input.is_held(pygame.K_s):
            self.input_vector.y += 1
        self.input_vector = self.input_vector.normalized()

    def self_update(self):
        move_vec = self.input_vector * self.speed * GameTime.delta
        self.move(move_vec)
