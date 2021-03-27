import pygame
from UIComp import UIComp
from CompContainer import CompContainer


class ButtonComp(UIComp, CompContainer):
    def __init__(self, x, y, width, height, text='', font_size=32, background_color=(255, 255, 255), color=(0, 0, 0),
                 outline_color=None, callback=None, *args):
        CompContainer.__init__(self)
        UIComp.__init__(self, x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.background_color = background_color
        self.color = color
        self.outline_color = outline_color
        self.callback = callback
        self.args = args

        self.mouse_down_over = False

    def self_draw(self, win):
        # Call this method to draw the button on the screen
        if self.outline_color is not None:
            pygame.draw.rect(win, self.outline_color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.background_color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.font_size)
            text = font.render(self.text, 1, self.color)
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2)))
        self.draw(win)

    def self_handle_event(self, event):
        if event is None:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.isOver(pygame.mouse.get_pos()):
                self.mouse_down_over = True
            else:
                self.mouse_down_over = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.isOver(pygame.mouse.get_pos()) and self.mouse_down_over:
                    if self.callback is not None:
                        self.callback(*self.args)

    def self_update(self):
        self.update()
