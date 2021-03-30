import pygame
from UIComp import UIComp

pygame.init()


class InputComp(UIComp):
    def __init__(self, x, y, w, h, placeholder='', font_size=32, outline=2, text="",
                 color_inactive=pygame.Color("gray"),
                 color_active=pygame.Color("black")):
        UIComp.__init__(self, x, y, w, h)
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color = self.color_inactive
        self.placeholder = placeholder
        self.text = text
        self.font_size = font_size
        self.outline = outline

        self.font = pygame.font.SysFont('comicsans', font_size)
        self.placeholder_surface = self.font.render(self.placeholder, True, self.color)
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = False

    def self_handle_event(self, event):
        if event is None:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if self.placeholder is not None:
                    self.placeholder = None
                if event.key == pygame.K_RETURN:
                    # print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def self_update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def self_draw(self, screen):
        # blit the placeholder
        if self.placeholder is not None:
            screen.blit(self.placeholder_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, self.outline)
