import pygame as pg
from pygame.math import Vector2

from helper import SpriteSheet


class Player(pg.sprite.Sprite):
    """Class for storing all the attributes related to the player."""

    speed = 5

    def __init__(self, sprite_sheet_path, pos):
        """Initialize required variables."""
        super().__init__()

        self.sprite_sheet = SpriteSheet(sprite_sheet_path)
        self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        """Update the player position."""
        self._move()

    def _move(self):
        """Change the player velocity vector.

        Move the player in the direction corresponding
        to the currently pressed keys."""
        self.velocity = Vector2(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.velocity.y = -1
        if keys[pg.K_s]:
            self.velocity.y = 1
        if keys[pg.K_a]:
            self.velocity.x = -1
        if keys[pg.K_d]:
            self.velocity.x = 1

        # Reset the x velocity when trying to move diagonally
        if self.velocity.length() > 1:
            self.velocity.x = 0

        self.velocity *= Player.speed
        self.rect.center += self.velocity
