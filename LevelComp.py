import pygame
from GameData import GameData
from CompContainer import CompContainer
from WallComp import WallComp
from Physics import Physics
from Player import Player
from Enemy import Enemy
from Sprite import Sprite
from Pathfinder import Pathfinder
from Events import Events
from CoinComp import CoinComp
from HeartsComp import HeartsComp

comp_map = {
    '#': WallComp,
    ' ': WallComp,
    'p': Player,
    'e': Enemy,
    '.': Sprite,
    '$': CoinComp
}


class LevelComp(CompContainer):
    def __init__(self, level):
        CompContainer.__init__(self)
        self.name = level
        self.rows = None
        self.cols = None
        self.paused = False

        Physics.clear()

        self.init()

        GameData.current_level = self
        Pathfinder.update_table()

    def self_handle_event(self, event):
        if not self.paused:
            self.handle_event(event)

        if event is None:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Events.emit("toggle_pause_menu")
                self.paused = not self.paused

    def self_update(self):
        if not self.paused:
            self.update()

    def self_draw(self, win):
        self.draw(win)

    def init(self):
        self.build_level()

        self.load_ui()
        # create pause menu

    def build_level(self):
        file_path = f'levels/{self.name}.txt'
        with open(file_path, 'r') as f:
            row = 0
            line = f.readline()
            while line:
                col = 0
                line = line[0:-1]

                for c in line:
                    if c in comp_map:
                        self.create_component(c, col, row)
                    col += 1

                row += 1
                line = f.readline()
                if self.cols is None:
                    self.cols = col
            self.rows = row

        super().fix_draw_order()

    def load_ui(self):
        # hearts component
        temp_sprite = Sprite("heart", 50, 50, 0, 0)
        new_heart_comp = HeartsComp(0, 0, 0, 0, temp_sprite)
        self.add_component(new_heart_comp)

    def create_component(self, comp_type, row, col):
        # create background
        if comp_type != '#':
            new_background = Sprite('background', GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                    col * GameData.tile_size)
            self.add_component(new_background, 0)

        # money
        if comp_type == '$':
            temp_sprite = Sprite('coin', GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_coin = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size, GameData.tile_size,
                                           GameData.tile_size,
                                           temp_sprite)
            self.add_component(new_coin, 5)

        # create walls
        if comp_type == '#' or comp_type == ' ':
            temp_sprite = Sprite('wall', GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_wall = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size, GameData.tile_size,
                                           GameData.tile_size,
                                           temp_sprite)
            self.add_component(new_wall, 10)

        # create player
        if comp_type == 'p':
            temp_sprite = Sprite("player", GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_player = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size,
                                             GameData.tile_size,
                                             GameData.tile_size, temp_sprite)
            self.add_component(new_player, 30)

        # create enemy
        if comp_type == 'e':
            temp_sprite = Sprite("enemy", GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_enemy = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size, GameData.tile_size,
                                            GameData.tile_size, temp_sprite)
            self.add_component(new_enemy, 20)
