import csv

import pygame as pg

from helper import res
from settings import *


class TileMap:
    """Class for storing attributes related to the game map."""

    WALL_IDS = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                52, 53, 54, 58, 59, 60, 61, 52, 53, 54, 65, 66, 67,
                69, 70, 75, 76, 77, 78, 79, 81, 82, 83, 84,
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                107, 108, 109, 110, 11, 112, 113, 114, 115, 116, 227, 118,
                119, 120, 121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135]

    NPC_IDS = list(range(119, 126))

    def __init__(self, game, csv_path, image_path, img_tile_size, spacing=0):
        """Run the private functions to create a map.

        Arguments:
        game - object of the main game class
        csv_path - path to a csv file containing map data
        image_path - path to the tileset image
        img_tile_size = size of a single tile in the given tileset
        spacing = amount of space between tiles in the tileset image
        """
        data_list = self._csv_to_list(csv_path)
        self.image_list = self._parse_image(image_path, img_tile_size, spacing)
        self._load_tiles(game, data_list, self.image_list)
        self.width = len(data_list[0]) * TILE_SIZE
        self.height = len(data_list) * TILE_SIZE

    def _csv_to_list(self, csv_path):
        """Return a 2D list with data from the given csv file."""
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    def _parse_image(self, image_path, img_tile_size, spacing):
        """Return a list of tile images from the given tileset."""
        lst = []
        image = pg.image.load(image_path).convert()

        if img_tile_size != TILE_SIZE:
            scale = TILE_SIZE // img_tile_size
            spacing *= scale
            current_size = image.get_size()
            target_size = tuple(i * scale for i in current_size)
            image = pg.transform.scale(image, target_size)

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
                collidable = int(index) in TileMap.WALL_IDS
                Tile(game, j, i, image_list[int(index)], collidable)


class Tile(pg.sprite.Sprite):
    """Class for storing attributes related to a single tile."""

    def __init__(self, game, x, y, image, is_wall=False):
        """Create a tile sprite in the given position.

        Arguments:
        game - game object
        x, y - row and column where the tile should be placed
        image - image object
        """
        if is_wall:
            groups = game.all_sprites, game.walls
        else:
            groups = game.all_sprites
        self._layer = GROUND_LAYER
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Camera:
    """Class storing methods needed to enable scrolling map feature."""

    def __init__(self, map_width, map_height):
        """Initialize the offset variable.

        offset - tuple, containing amount of pixels by which the map
                 should be shifted along the x and y axis
        """
        self.offset = (0, 0)
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, entity_rect):
        """Move passed rect by the offset variable."""
        return entity_rect.move(self.offset)

    def update(self, target):
        """Make the camera follow the target.

        target - sprite for the camera to follow

        Set the offset variable so that when applied to the map
        the target would be centered on the screen.
        Stop the camera if the target reaches the end of the map.
        """
        x = -target.rect.x + SCREEN_WIDTH // 2
        y = -target.rect.y + SCREEN_HEIGHT // 2
        # Camera constraints
        x = min(x, 0)   # Left
        y = min(y, 0)   # Top
        x = max(x, -self.map_width + SCREEN_WIDTH)      # Right
        y = max(y, -self.map_height + SCREEN_HEIGHT)    # Bottom
        self.offset = (x, y)
