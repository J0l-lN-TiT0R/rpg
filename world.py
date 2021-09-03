import csv

import pygame as pg

from helper import res
from settings import *


class TileMap:
    """Class for storing attributes related to the game map."""
    def __init__(self, game, csv_path, image_path, spacing=0):
        """Run the private functions to create a map."""
        data_list = self._csv_to_list(csv_path)
        image_list = self._parse_image(image_path, spacing)
        self._load_tiles(game, data_list, image_list)

    def _csv_to_list(self, csv_path):
        """Return a 2D list with data from the given csv file."""
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    def _parse_image(self, image_path, spacing):
        """Return a list of tile images from the given tileset."""
        lst = []
        image = pg.image.load(image_path).convert()

        width, height = image.get_size()
        for y in range(0, height, TILE_SIZE + spacing):
            for x in range(0, width, TILE_SIZE + spacing):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                lst.append(tile)
        return lst

    def _load_tiles(self, game, data_list, image_list):
        """Create tile objects."""
        for i, row in enumerate(data_list):
            for j, index in enumerate(row):
                Tile(game, j, i, image_list[int(index)])


class Tile(pg.sprite.Sprite):
    """Class for storing attributes related to a single tile."""
    def __init__(self, game, x, y, image):
        """Create a tile sprite in the given position.

        Arguments:
        game - game object
        x, y - row and column where the tile should be placed
        image - image object
        """
        super().__init__(game.all_sprites)
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

