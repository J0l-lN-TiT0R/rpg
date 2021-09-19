import pygame as pg

from messages import Message
from settings import *


class NPC(pg.sprite.Sprite):
    """Class for creating Non-Player Charactes."""

    def __init__(self, game, pos, image):
        """Initialize required variables."""
        self._layer = GROUND_LAYER
        groups = game.all_sprites, game.walls
        super().__init__(groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect(center=pos)

        self.message = Message(game, (pos[0], pos[1]-40),
                               'El. Psy. Kongroo.')

    def update(self):
        """Update current message."""
        # Show current message when colliding with the player
        if self.rect.colliderect(self.game.player):
            self.message.print()
        elif self.message.groups():
            self.message.reset()
