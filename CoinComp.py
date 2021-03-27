from StaticComp import StaticComp
from CollisionTypes import CollisionTypes
from Physics import Physics
from Events import Events


class CoinComp(StaticComp):
    def __init__(self, x, y, width, height, sprite):
        StaticComp.__init__(self, x, y, width, height, sprite)
        self.collision_type = CollisionTypes.pickable

        Physics.add(self, self.collision_type)

        Events.connect("coin_picked", self, self.free)

    def free(self, coin):
        if coin is not self:
            return
        self.parent.remove_component(self)
        Physics.remove(self, self.collision_type)

    def self_handle_event(self, event):
        pass

    def self_update(self):
        pass
