import pygame


class Physics:
    solids = []

    @staticmethod
    def add_solid(solid):
        if solid not in Physics.solids:
            Physics.solids.append(solid)

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
