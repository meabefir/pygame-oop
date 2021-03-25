from GameData import GameData
from CompContainer import CompContainer
from StaticComp import StaticComp
from DynamicComp import DynamicComp
from Player import Player
from Enemy import Enemy
from Sprite import Sprite

comp_map = {
    '#': StaticComp,
    'p': Player,
    'e': Enemy,
    '.': Sprite
}


class LevelComp(CompContainer):
    def __init__(self, level):
        CompContainer.__init__(self)
        self.name = level

        self.build_level()

    def self_handle_event(self):
        self.handle_event()
        pass

    def self_update(self):
        self.update()
        pass

    def self_draw(self, win):
        self.draw(win)

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

        super().fix_draw_order()

    def create_component(self, comp_type, row, col):
        # create background
        if comp_type != '#':
            new_background = Sprite('background', GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                    col * GameData.tile_size)
            self.add_component(new_background, 0)

        # create walls
        if comp_type == '#':
            temp_sprite = Sprite('wall', GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_wall = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size, GameData.tile_size,
                                           GameData.tile_size,
                                           temp_sprite)
            self.add_component(new_wall, 10)

        # create player
        if comp_type == 'p':
            temp_sprite = Sprite("player", GameData.tile_size - 20, GameData.tile_size - 20, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_player = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size,
                                             GameData.tile_size - 20,
                                             GameData.tile_size - 20, temp_sprite)
            self.add_component(new_player, 30)

        # create enemy
        if comp_type == 'e':
            temp_sprite = Sprite("enemy", GameData.tile_size, GameData.tile_size, row * GameData.tile_size,
                                 col * GameData.tile_size)
            new_enemy = comp_map[comp_type](row * GameData.tile_size, col * GameData.tile_size, GameData.tile_size,
                                            GameData.tile_size, temp_sprite)
            self.add_component(new_enemy, 20)
