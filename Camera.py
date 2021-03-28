from Vector2 import Vector2


class Camera:
    follows = None
    size = Vector2()
    position = Vector2(0, 0)

    @staticmethod
    def update():
        if Camera.follows is not None:
            Camera.position = Camera.follows.position - Camera.size / 2

    @staticmethod
    def set_follows(comp):
        Camera.follows = comp
