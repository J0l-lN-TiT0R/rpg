import pygame as pg

from player import Player
from world import TileMap
from helper import res
from settings import *


class Game:
    """Generic class for holding the game attributes."""
    def __init__(self):
        """Create the game window."""
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        pg.display.set_icon(pg.image.load(res/'sprites'/'frog.png'))
        self.running = True

    def new(self):
        """Initialize all the sprites."""
        player = Player(res/'sprites'/'player_sheet.png', (100, 100))

        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player)
        self.map = TileMap(self, res/'map'/'map.csv', res/'map'/'rpg_tileset.png')

    def _events(self):
        """Check for input events."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                        and event.key == pg.K_ESCAPE):
                self.running = False

    def _update(self):
        """Update everything that's on the screen."""
        self.all_sprites.update()

    def _draw(self):
        """Draw every sprite."""
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def run(self):
        """The game loop."""
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()


if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
