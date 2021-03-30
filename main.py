import pygame, sys
from Camera import Camera
from GameTime import GameTime
from GameData import GameData
from CompContainer import CompContainer
from LevelComp import LevelComp
from Input import Input
from FPSCounter import FPSCounter
from CanvasComp import CanvasComp
from Database import Database


pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode(GameData.window_size, 0, 32)
pygame.display.set_caption('Ahmed Game')


class Game(CompContainer):
    def __init__(self):
        CompContainer.__init__(self)

        self.load_UI()
        # self.load_fps()

    def run(self):
        # update inputs
        self.handle_event(None)

        # update logic
        self.update()
        Camera.update()

        # draw
        window.fill(GameData.background_color)
        self.draw(window)
        pygame.display.update()

    def clear_level(self):
        level_playing = self.has_component_of_class(LevelComp)
        if level_playing is not None:
            Camera.set_follows(None)
            self.remove_component(level_playing)
            GameData.current_level = None

            if GameData.user is not None:
                GameData.user.update_data(Database.get_user(GameData.user.data['username']))

    def load_level(self, name):
        self.clear_level()
        # create new level
        new_level = LevelComp(name)
        self.add_component(new_level, 0)

        self.fix_draw_order()

    def load_UI(self):
        new_ui = CanvasComp(0, 0, GameData.window_size[0], GameData.window_size[1])
        self.add_component(new_ui, 10)

    def load_fps(self):
        size = (100, 50)
        fps_counter = FPSCounter(0, GameData.window_size[1] - size[1], size[0], size[1])
        self.add_component(fps_counter)


game = Game()
GameData.game = game

running = True
while running:
    for event in pygame.event.get():
        Input.handle_input(event)
        game.handle_event(event)

    #game.handle_event(None)

    game.run()

    GameTime.update()
    clock.tick(120)
