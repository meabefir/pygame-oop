import pygame
from CollisionTypes import CollisionTypes


class Physics:
    collidables = {}

    @staticmethod
    def is_in_collision_group(comp, coll_type=CollisionTypes.solid):
        if comp in Physics.collidables[coll_type]:
            return True
        return False

    @staticmethod
    def remove(comp, coll_type=CollisionTypes.solid):
        if comp in Physics.collidables[coll_type]:
            Physics.collidables[coll_type].remove(comp)

    @staticmethod
    def add(comp, coll_type=CollisionTypes.solid):
        if comp not in Physics.collidables[coll_type]:
            Physics.collidables[coll_type].append(comp)

    @staticmethod
    def clear():
        for attr in [a for a in dir(CollisionTypes) if not a.startswith('__')]:
            Physics.collidables[getattr(CollisionTypes, attr)] = []

    @staticmethod
    def get_collisions(comp, coll_type=CollisionTypes.solid):
        collided_with = []
        for solid in Physics.collidables[coll_type]:
            if solid != comp and solid.rect.colliderect(comp.rect):
                collided_with.append(solid)
        return collided_with

    @staticmethod
    def get_rect_collisions(rect, coll_type=CollisionTypes.solid):
        collided_with = []
        for solid in Physics.collidables[coll_type]:
            if solid.rect.colliderect(rect):
                collided_with.append(solid)
        return collided_with
