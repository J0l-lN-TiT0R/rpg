import pygame as pg
import pygame.freetype

from settings import *


class Message(pg.sprite.Sprite):
    """Class for creating in-game messages."""

    def __init__(self, game, pos, text, font=None):
        """Initialize required variables."""
        self._layer = MESSAGE_LAYER
        super().__init__(game.all_sprites)
        self.game = game

        self.text = text
        self.display_text = ''
        self.current_symbol = 0
        self.text_pos = (10, 14)
        self.font = pg.freetype.Font(font, 16)

        text_surf, text_rect = self.font.render(self.text)
        self.image = pg.Surface((text_rect.w + 40, text_rect.h + 25),
                                pg.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.border = pg.Rect((0, 0), self.rect.size)
        self.border.w = text_rect.w + 20

    def print(self):
        """Print current text on the image surface."""
        self.current_symbol += 0.2
        self.display_text = self.text[:int(self.current_symbol)]
        self.add(self.game.all_sprites)
        text_surf, text_rect = self.font.render(self.display_text)
        self.image.fill((0, 0, 0, 0))
        self.image.blit(text_surf, self.text_pos)
        pg.draw.rect(self.image, (0, 0, 0), self.border,
                     width=5, border_radius=10)

    def reset(self):
        """Delete current message box and prepare for the next one."""
        self.display_text = ''
        self.current_symbol = 0
        self.kill()
