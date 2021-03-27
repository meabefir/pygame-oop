import pygame


class UIComp:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def draw_rect(self, win, color=(0, 0, 0)):
        pygame.draw.rect(win, color, (self.x, self.y, self.width, self.height), 2)

    def draw_full_rect(self, win, color=(255, 255, 255)):
        if len(color) == 4:
            temp_s = pygame.Surface((self.width, self.height))
            temp_s.set_alpha(color[3])
            temp_s.fill(color[0:3])
            win.blit(temp_s, (self.x, self.y))
        else:
            pygame.draw.rect(win, color, (self.x, self.y, self.width, self.height), 0)
