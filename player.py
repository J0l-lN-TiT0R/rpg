import pygame as pg

from helper import SpriteSheet


class Player(pg.sprite.Sprite):
    def __init__(self, sprite_sheet_path, pos):
        super().__init__()

        self.sprite_sheet = SpriteSheet(sprite_sheet_path)
        self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos
