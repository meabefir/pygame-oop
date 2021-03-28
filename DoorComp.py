from StaticComp import StaticComp
from CollisionTypes import CollisionTypes
from Physics import Physics


class DoorComp(StaticComp):
    def __init__(self, x, y, width, height, sprite):
        StaticComp.__init__(self, x, y, width, height, sprite)

        Physics.add(self, CollisionTypes.door)
