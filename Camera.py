from Vector2 import Vector2
from GameData import GameData


class Camera:
    follows = None
    size = Vector2(GameData.window_size[0], GameData.window_size[1])
    position = Vector2(0, 0)

    @staticmethod
    def update():
        if Camera.follows is not None:
            Camera.position = (Camera.follows.position - Camera.size / 2).to_int()

    @staticmethod
    def set_follows(comp):
        Camera.follows = comp
