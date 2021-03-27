import pygame
import queue


class CompContainer:
    def __init__(self):
        self.components = []
        self.com_prio = []
        self.parent = None

    def add_component(self, comp, prio=0):
        self.com_prio.append((prio, comp))
        comp.parent = self
        self.components.append(comp)

    # DANGER! should also be removed from self.com_prio ?
    def remove_component(self, comp):
        if comp in self.components:
            self.components.remove(comp)

    def fix_draw_order(self):
        self.com_prio.sort(key=lambda com: com[0])
        self.components = []
        for com in self.com_prio:
            self.components.append(com[1])

    def handle_event(self, event):
        for component in self.components:
            component.self_handle_event(event)

    def update(self):
        for component in self.components:
            component.self_update()

    def draw(self, win):
        for component in self.components:
            component.self_draw(win)

    # def self_handle_event(self):
    #     pass
    #
    # def self_update(self):
    #     pass
    #
    # def self_draw(self, win):
    #     pass
