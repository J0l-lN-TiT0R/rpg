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

        self.pos = pos
        self.text = text
        self.display_text = ''
        self.current_symbol = 0
        self.text_pos = (10, 14)
        self.font = pg.freetype.Font(font, 16)

        text_surf, text_rect = self.font.render(self.text)
        self.image = pg.Surface((text_rect.w + 40, text_rect.h + 25),
                                pg.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.border = pg.Rect((0, 0), (text_rect.w + 20, self.rect.h))

    def print(self, speed=10):
        """Print current text on the image surface."""
        # Multiplying by dt to make animation consistent with the framerate
        self.current_symbol += self.game.dt * speed
        self.display_text = self.text[:int(self.current_symbol)]
        self.add(self.game.all_sprites)
        text_surf, text_rect = self.font.render(self.display_text)
        self.image.fill((0, 0, 0, 0))
        self.image.blit(text_surf, self.text_pos)
        pg.draw.rect(self.image, (0, 0, 0), self.border,
                     width=5, border_radius=10)

        # Measuring time needed to display the text
#         if len(self.display_text) == 1:
#             self.start_time = pg.time.get_ticks()
#         if len(self.display_text) == len(self.text):
#             print(pg.time.get_ticks() - self.start_time)
#             exit()

    def set_text(self, text):
        """Change displayed text and the box around it."""
        self.reset()
        self.text = text
        text_surf, text_rect = self.font.render(self.text)
        self.image = pg.Surface((text_rect.w + 40, text_rect.h + 25),
                                pg.SRCALPHA)
        self.rect = self.image.get_rect(center=self.pos)
        self.border = pg.Rect((0, 0), (text_rect.w + 20, self.rect.h))

    def reset(self):
        """Delete current message box and prepare for the next one."""
        self.display_text = ''
        self.current_symbol = 0
        self.kill()
