import pygame as pg
from pygame.math import Vector2

from helper import SpriteSheet
from settings import *


class Player(pg.sprite.Sprite):
    """Class for storing all the attributes related to the player."""

    speed = 5

    def __init__(self, game, sprite_sheet_path, pos):
        """Initialize required variables."""
        self._layer = PLAYER_LAYER
        super().__init__(game.all_sprites)

        self.game = game
        self.cycle_len = 4
        sprite_sheet = SpriteSheet(sprite_sheet_path, 1.5)
        self._load_images(sprite_sheet)
        self.image = self.walk_right[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.phys_body = pg.Rect(self.rect.x, self.rect.y,
                                 self.rect.w * 0.5, self.rect.h/4)
        self.phys_body.centerx = self.rect.centerx
        self.phys_body.bottom = self.rect.bottom - 5

        self.last_update = 0
        self.frame = 0
        self.velocity = Vector2(0, 0)

    def update(self):
        """Update the player position."""
        self._move()
        self._animate()

    def _move(self):
        """Change the player velocity vector.

        Move the player in the direction corresponding
        to the currently pressed keys."""
        self.velocity.update(0, 0)
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
        if not self._will_collide():
            self.rect.center += self.velocity
            self.phys_body.center += self.velocity

    def _will_collide(self):
        """Determine if the player will collide with the walls."""
        target_rect = self.phys_body.move(self.velocity)
        for tile in self.game.walls:
            if target_rect.colliderect(tile.rect):
                return True
        return False

    def _load_images(self, sheet):
        """Load images from the sheet into separate lists."""
        self.walk_right = []
        self.walk_left = []
        self.walk_up = []
        self.walk_down = []

        # Calculating the width and height of a separate image
        w, h = sheet.w // self.cycle_len, sheet.h // self.cycle_len
        for x in range(0, w*4, w):
            self.walk_down.append(sheet.get_image(x, 0, w, h))
            self.walk_left.append(sheet.get_image(x, h, w, h))
            self.walk_right.append(sheet.get_image(x, h*2, w, h))
            self.walk_up.append(sheet.get_image(x, h*3, w, h))

    def _animate(self, frame_len=100):
        """Animate the player if moving.

        frame_len - amount of time in ms during which one frame
        of animation is displayed while moving.
        """
        now = pg.time.get_ticks()
        if now - self.last_update > frame_len and self.velocity.length() > 0:
            self.last_update = now

            if self.velocity.y > 0:
                self.animation_cycle = self.walk_down
            elif self.velocity.y < 0:
                self.animation_cycle = self.walk_up
            elif self.velocity.x > 0:
                self.animation_cycle = self.walk_right
            elif self.velocity.x < 0:
                self.animation_cycle = self.walk_left

            self.frame = (self.frame + 1) % self.cycle_len
            self.image = self.animation_cycle[self.frame]
