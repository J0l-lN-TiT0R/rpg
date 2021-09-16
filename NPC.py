import pygame as pg

from settings import *


class NPC(pg.sprite.Sprite):
    """ ."""

    def __init__(self, game, pos, image):
        """ ."""
        self._layer = GROUND_LAYER
        groups = game.all_sprites, game.walls
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        """ ."""
        pass
