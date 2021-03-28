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
from HeartsComp import HeartsComp
from Sprite import Sprite
from PowerupTypes import PowerupTypes
from Camera import Camera

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
        self.invincible_alpha = 120
        self.current_powerup = None

        GameData.player = self
        self.invincibility_timer = Timer(self.invincibility_timeout)
        self.add_component(self.invincibility_timer)

        self.powerup_timer = Timer(self.powerup_timeout)
        self.add_component(self.powerup_timer)

        self.init()

        Events.connect("powerup_picked", self, self.powerup_picked)

    def powerup_picked(self, powerup_comp):
        powerup_type = powerup_comp.powerup_type
        self.current_powerup = powerup_type

        if powerup_type == PowerupTypes.invincibility:
            self.invincibility_timer.stop()
            self.set_invincible(True)
            self.powerup_timer.start(4)

    def powerup_timeout(self):
        if self.current_powerup == PowerupTypes.invincibility:
            self.set_invincible(False)

        self.current_powerup = None

    def set_invincible(self, value):
        self.invincible = value

        if self.invincible:
            self.sprite.set_alpha(self.invincible_alpha)
        else:
            self.sprite.set_alpha(255)

    def self_handle_event(self, event):
        if self.destination is None:
            free_cells = self.get_free_cells()
            for key in directions:
                if Input.is_held(key) and directions[key] in free_cells:
                    self.move_to_cell(directions[key])

    def cell_changed(self):
        Pathfinder.update_table()

        self.check_collisions_end()

    def check_collisions(self):
        # coins collision
        coins_collisions = Physics.get_collisions(self, CollisionTypes.pickable)
        for coin in coins_collisions:
            Events.emit("coin_picked", coin)

        # enemy collision
        enemy_collisions = Physics.get_collisions(self, CollisionTypes.enemy)
        if len(enemy_collisions):
            if self.invincible is False:
                self.player_hurt(enemy_collisions[0].damage)
            elif self.current_powerup == PowerupTypes.invincibility:
                Events.emit("enemy_killed", enemy_collisions[0])

        # powerup collision
        if self.current_powerup is None:
            powerup_colls = Physics.get_collisions(self, CollisionTypes.powerup)
            if len(powerup_colls):
                Events.emit("powerup_picked", powerup_colls[0])

    def check_collisions_end(self):
        # door collision
        door_coll = Physics.get_collisions(self, CollisionTypes.door)
        if len(door_coll):
            Events.emit("level_completed", GameData.current_level.name)

    def player_hurt(self, damage):
        self.set_invincible(True)
        self.hp -= damage
        Events.emit("set_hp", self.hp)
        self.invincibility_timer.start(self.invincibility_time)
        # reset level ih hp == 0
        if self.hp == 0:
            GameData.game.clear_level()
            GameData.game.load_level(self.parent.name)

    def invincibility_timeout(self):
        self.set_invincible(False)

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

    def init(self):
        # hearts component
        temp_sprite = Sprite("heart", 50, 50, 0, 0, ui_sprite=True)
        new_heart_comp = HeartsComp(0, 0, 0, 0, temp_sprite)
        self.add_component(new_heart_comp)

        Camera.set_follows(self)
