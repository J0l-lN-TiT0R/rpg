import pygame as pg
from pygame.math import Vector2

from helper import SpriteSheet


class Player(pg.sprite.Sprite):
    """Class for storing all the attributes related to the player."""

    speed = 5

    def __init__(self, sprite_sheet_path, pos):
        """Initialize required variables."""
        super().__init__()

        sprite_sheet = SpriteSheet(sprite_sheet_path, 2)
        self._load_images(sprite_sheet)
        self.image = self.walk_right[0]
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

    def _load_images(self, sheet):
        self.walk_right = []
        self.walk_left = []
        self.walk_up = []
        self.walk_down = []

        # Version 1.0
#         x = 0
#         for _ in range(4):
#             self.walk_down.append(sheet.get_image(x, 0, 32, 32))
#             self.walk_left.append(sheet.get_image(x, 32, 32, 32))
#             self.walk_right.append(sheet.get_image(x, 64, 32, 32))
#             self.walk_up.append(sheet.get_image(x, 96, 32, 32))
#             x += 32

        # Version 2.0
#         w, h = 32, 32
#         for x in range(0, 128, 32):
#             self.walk_down.append(sheet.get_image(x, 0, w, h))
#             self.walk_left.append(sheet.get_image(x, 32, w, h))
#             self.walk_right.append(sheet.get_image(x, 64, w, h))
#             self.walk_up.append(sheet.get_image(x, 96, w, h))

        # Version 3.0
        w, h = sheet.w // 4, sheet.h // 4
        for x in range(0, w*4, w):
            self.walk_down.append(sheet.get_image(x, 0, w, h))
            self.walk_left.append(sheet.get_image(x, h, w, h))
            self.walk_right.append(sheet.get_image(x, h*2, w, h))
            self.walk_up.append(sheet.get_image(x, h*3, w, h))
