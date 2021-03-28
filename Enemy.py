from Timer import Timer
from DynamicComp import DynamicComp
from CompContainer import CompContainer
from Vector2 import Vector2
from GameTime import GameTime
from Pathfinder import Pathfinder
from Physics import Physics
from CollisionTypes import CollisionTypes
from GameData import GameData
from PowerupTypes import PowerupTypes
from Events import Events
import random


class Enemy(DynamicComp, CompContainer):
    def __init__(self, x, y, width, height, sprite):
        DynamicComp.__init__(self, x, y, width, height, sprite)
        CompContainer.__init__(self)
        self.input_vector = Vector2()
        self.speed = 200
        self.follow_distance = 5
        self.damage = 1
        self.xp = 10

        self.collision_type = CollisionTypes.enemy
        Physics.add(self, CollisionTypes.enemy)

        self.add_component(self.sprite)

        Events.connect("enemy_killed", self, self.free)

        # self.timer = Timer(self.timer_timeout)
        # self.add_component(self.timer)
        # self.timer.start(1)

    def self_handle_event(self, event):
        pass

    def self_update(self):
        self.update()

        # follow player if ready to move
        if self.destination is None:
            dir = Pathfinder.get_smaller_cell_dir(self.position)
            if GameData.player is not None:
                if GameData.player.current_powerup == PowerupTypes.invincibility:
                    dir = Pathfinder.get_bigger_cell_dir(self.position)
            cell_value = Pathfinder.get_cell_value(self.position)
            if dir is not None and cell_value <= self.follow_distance:
                self.move_to_cell(dir)
            else:
                self.move_to_random_free_cell()

        # if it has a destination
        if self.destination is not None:
            # print(self.position,self.destination)
            movement_vec = self.position.move_towards(self.destination, self.speed * GameTime.delta) - self.position
            if self.position + movement_vec == self.destination:
                self.destination = None
                self.move(movement_vec)
            else:
                self.move(movement_vec)

    def free(self, comp):
        if comp is not self:
            return
        self.parent.remove_component(self)
        Physics.remove(self, self.collision_type)
        Events.emit("give_xp", self.xp)

    def timer_timeout(self):
        if self.destination is None:
            free_cells = self.get_free_cells()
            if len(free_cells) == 0:
                return
            random_free_cell = free_cells[random.randint(0, len(free_cells) - 1)]
            self.move_to_cell(random_free_cell)

        self.timer.start(1)
