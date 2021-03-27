import pygame, sys
from GameTime import GameTime
from GameData import GameData
from CompContainer import CompContainer
from LevelComp import LevelComp
from Input import Input
from Events import Events
from CanvasComp import CanvasComp

from TextureLoader import textures

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode(GameData.window_size, 0, 32)
pygame.display.set_caption('Ahmed game')


class Game(CompContainer):
    def __init__(self):
        CompContainer.__init__(self)

        self.load_level("level2")
        self.load_UI()

    def run(self):
        # update inputs
        # self.handle_event()

        # update logic
        self.update()

        # draw
        window.fill(GameData.background_color)
        self.draw(window)
        pygame.display.update()

    def load_level(self, name):
        new_level = LevelComp(name)
        self.add_component(new_level, 0)

    def load_UI(self):
        new_ui = CanvasComp(0, 0, GameData.window_size[0], GameData.window_size[1])
        self.add_component(new_ui, 10)


game = Game()
GameData.game = game

running = True
while running:
    for event in pygame.event.get():
        Input.handle_input(event)
        game.handle_event(event)

    game.handle_event(None)

    game.run()

    GameTime.update()
    clock.tick(120)
