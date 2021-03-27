from StaticComp import StaticComp
from Physics import Physics


class WallComp(StaticComp):
    def __init__(self, x, y, width, height, sprite):
        StaticComp.__init__(self, x, y, width, height, sprite)

        Physics.add(self)
