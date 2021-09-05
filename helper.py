import sys
from pathlib import Path

import pygame as pg

from settings import *


class SpriteSheet:
    """Class for storing and managing sprite sheets."""
    def __init__(self, file_path, scale=1):
        """Load the sprite sheet from the given path.

        Scale the sheet by the scale parameter.
        """
        sheet = pg.image.load(file_path).convert_alpha()
        w, h = sheet.get_size()
        target_size = (int(w * scale), int(h * scale))
        self.sheet = pg.transform.scale(sheet, target_size)
        self.w, self.h = self.sheet.get_size()

    def get_image(self, x, y, width, height):
        """Cut and return a piece of sprite sheet."""
        return self.sheet.subsurface(x, y, width, height)


# Use this to not overcomplicate
# res = Path("res")

# Use this to be able to run the game by simply
# double-clicking the main file
res = Path(sys.argv[0]).parent/"res"
