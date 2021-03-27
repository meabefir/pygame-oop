import pygame
from DynamicComp import DynamicComp
from Vector2 import Vector2
from GameTime import GameTime
from Input import Input
from GameData import GameData
from Pathfinder import Pathfinder
from Physics import Physics
from CollisionTypes import CollisionTypes
from Events import Events
from Timer import Timer

directions = {
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
}


class Player(DynamicComp):
    def __init__(self, x, y, width, height, sprite):
        DynamicComp.__init__(self, x, y, width, height, sprite)
        self.input_vector = Vector2()
        self.speed = 300
        self.hp = GameData.player_data["max_hp"]
        self.invincible = False
        self.invincibility_time = 2

        GameData.player = self
        self.invincibility_timer = Timer(self.invincibility_timeout)
        self.add_component(self.invincibility_timer)

    def self_handle_event(self, event):
        if self.destination is None:
            free_cells = self.get_free_cells()
            for key in directions:
                if Input.is_held(key) and directions[key] in free_cells:
                    self.move_to_cell(directions[key])

    def cell_changed(self):
        Pathfinder.update_table()

    def check_collisions(self):
        # coins collision
        coins_collisions = Physics.get_collisions(self, CollisionTypes.pickable)
        for coin in coins_collisions:
            Events.emit("coin_picked", coin)

        # enemy collision
        if self.invincible is False:
            enemy_collisions = Physics.get_collisions(self, CollisionTypes.enemy)
            if len(enemy_collisions):
                self.invincible = True
                enemy = enemy_collisions[0]
                self.hp -= enemy.damage
                Events.emit("set_hp", self.hp)
                self.invincibility_timer.start(self.invincibility_time)

    def invincibility_timeout(self):
        self.invincible = False

    def self_update(self):
        self.update()

        self.check_collisions()
        # if it has a destination to reach
        if self.destination is not None:
            movement_vec = self.position.move_towards(self.destination, self.speed * GameTime.delta) - self.position

            # if reached destionation
            if self.position + movement_vec == self.destination:
                self.destination = None
                self.move(movement_vec)
                self.cell_changed()
            else:
                self.move(movement_vec)
