import pygame


class Physics:
    solids = []

    @staticmethod
    def is_solid(comp):
        if comp in Physics.solids:
            return True
        return False

    @staticmethod
    def remove_solid(solid):
        Physics.solids.remove(solid)

    @staticmethod
    def add_solid(solid):
        if solid not in Physics.solids:
            Physics.solids.append(solid)

    @staticmethod
    def clear():
        Physics.solids = []

    @staticmethod
    def get_collisions(comp):
        collided_with = []
        for solid in Physics.solids:
            if solid != comp and solid.rect.colliderect(comp.rect):
                collided_with.append(solid)
        return collided_with

    @staticmethod
    def get_rect_collisions(rect):
        collided_with = []
        for solid in Physics.solids:
            if solid.rect.colliderect(rect):
                collided_with.append(solid)
        return collided_with
