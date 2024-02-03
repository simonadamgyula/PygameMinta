import pygame
from settings import tile_size
from tiles import TerrainTile


class Level:
    def __init__(self, level_data: list[str], surface: pygame.Surface):
        self.display_surface: pygame.Surface = surface
        self.terrain_tiles: pygame.sprite.Group = pygame.sprite.Group()
        self.setup_level(level_data)

    def setup_level(self, layout: list[str]):
        for row_index, row in enumerate(layout):
            for col_index, tile_type in enumerate(row):
                x: int = col_index * tile_size
                y: int = row_index * tile_size
                if tile_type != ' ':
                    tile: TerrainTile = TerrainTile(tile_size, x, y, tile_type)
                    self.terrain_tiles.add(tile)

    def run(self):
        self.terrain_tiles.draw(self.display_surface)

