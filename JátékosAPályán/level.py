import pygame
from settings import tile_size
from tiles import TerrainTile
from player import Player


class Level:
    def __init__(self, level_data: list[str], surface: pygame.Surface):
        self.display_surface: pygame.Surface = surface
        self.player = pygame.sprite.GroupSingle()
        self.terrain_tiles: pygame.sprite.Group = pygame.sprite.Group()
        self.setup_level(level_data)

    def setup_level(self, layout: list[str]):
        for row_index, row in enumerate(layout):
            for col_index, tile_type in enumerate(row):
                x: int = col_index * tile_size
                y: int = row_index * tile_size
                if tile_type == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif tile_type != " ":
                    tile: TerrainTile = TerrainTile(tile_size, x, y, tile_type)
                    self.terrain_tiles.add(tile)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(Player.rect):
                if Player.direction.x < 0:
                    Player.rect.left = sprite.rect.right
                if Player.direction.x > 0:
                    Player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(Player.rect):
                if Player.direction.y > 0:
                    Player.rect.bottom = sprite.rect.top
                    Player.direction.y = 0
                    Player.on_ground = True
                elif Player.direction.y < 0:
                    Player.rect.top = sprite.rect.bottom
                    Player.direction.y = 0

    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.terrain_tiles.draw(self.display_surface)
