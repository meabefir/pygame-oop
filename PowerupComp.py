from StaticComp import StaticComp
from Physics import Physics
from CollisionTypes import CollisionTypes
from Events import Events
from PowerupTypes import PowerupTypes
from GameData import GameData


class PowerupComp(StaticComp):
    def __init__(self, x, y, width, height, sprite, powerup_type):
        StaticComp.__init__(self, x, y, width, height, sprite)
        self.collision_type = CollisionTypes.powerup
        self.powerup_type = powerup_type

        Physics.add(self, CollisionTypes.powerup)

        Events.connect("powerup_picked", self, self.powerup_picked)

    def powerup_picked(self, comp):
        if comp is self:
            self.free()

    def free(self):
        Physics.remove(self, self.collision_type)
        self.parent.remove_component(self)
