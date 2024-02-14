import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size: int, x: int, y: int):
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((size, size))
        self.rect: pygame.Rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


class TerrainTile(Tile):
    def __init__(self, size: int, x: int, y: int, terrain_type: str):
        super().__init__(size, x, y)
        self.image: pygame.Surface = pygame.image.load(
            f"../img/terrain/{terrain_type}.png"
        ).convert_alpha()
