import pygame
from Events import Events


class GameTime:
    game_time = 0
    delta = 0
    start_time = None
    duration = None

    @staticmethod
    def update():
        time_now = pygame.time.get_ticks()
        GameTime.delta = (time_now - GameTime.game_time) / 1000
        GameTime.game_time = time_now

        if GameTime.start_time is not None and GameTime.duration is not None:
            if GameTime.start_time <= GameTime.game_time - GameTime.duration:
                GameTime.start_time = None
                GameTime.duration = None
                Events.emit('timeout')

    @staticmethod
    def start_timer(ms):
        GameTime.start_time = GameTime.game_time
        GameTime.duration = ms
