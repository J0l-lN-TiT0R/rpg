import pygame as pg
import pygame.freetype

from settings import *


class Message(pg.sprite.Sprite):
    """Class for creating in-game messages."""

    def __init__(self, game, pos, text, font=None):
        """Initialize required variables."""
        self._layer = MESSAGE_LAYER
        super().__init__(game.all_sprites)
        self.image = pg.Surface((200, 40), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.border = pg.Rect((0, 0), self.rect.size)
        self.text = text
        self.text_pos = (10, 10)
        self.font = pg.freetype.Font(font, 16)

    def print(self):
        """Print current text on the image surface."""
        pg.draw.rect(self.image, (0, 0, 0), self.border,
                     width=5, border_radius=10)
        self.font.render_to(self.image, self.text_pos, self.text)
