import pygame as pg


class SpriteSheet:
    def __init__(self, file_path):
        self.sheet = pg.image.load(file_path).convert_alpha()

    def get_image(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)
