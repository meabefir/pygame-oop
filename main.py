import pygame, sys
from GameTime import GameTime
from CompContainer import CompContainer
from LevelComp import LevelComp
from Input import Input

from TextureLoader import textures

pygame.init()
clock = pygame.time.Clock()

window_size = (1280, 720)
window = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption('Ahmed game')

background_color = (255, 255, 255)


class Game(CompContainer):
    def __init__(self):
        CompContainer.__init__(self)

    def run(self):
        # update inputs
        self.handle_event()

        # update logic
        self.update()

        # draw
        window.fill(background_color)
        self.draw(window)
        pygame.display.update()

    def load_level(self, name):
        new_level = LevelComp(name)
        self.add_component(new_level)


game = Game()

game.load_level("level2")

running = True
while running:
    for event in pygame.event.get():
        Input.handle_input(event)

    game.run()

    GameTime.update()
    clock.tick(120)
