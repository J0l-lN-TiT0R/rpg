import csv

import pygame as pg

from helper import res
from settings import *


class TileMap:
    def __init__(self, csv_path, image_path, spacing=0):
        """Run the private functions to create a map."""
        data_list = self._csv_to_list(csv_path)
        image_list = self._parse_image(image_path, spacing)

    def _csv_to_list(self, csv_path):
        """Return a 2D list with data from the given csv file."""
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)

            # To demonstrate the result
            # for row in data:
            #     print(row)

        return data

    def _parse_image(self, image_path, spacing):
        """Return a list of tile images from the given tileset."""
        image_list = []
        image = pg.image.load(image_path).convert()

        width, height = image.get_size()
        for y in range(0, height, TILE_SIZE + spacing):
            for x in range(0, width, TILE_SIZE + spacing):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                image_list.append(tile)
        return image_list
