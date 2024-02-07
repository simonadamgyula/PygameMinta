import pygame
from settings import tile_size, screen_width
from tiles import TerrainTile
from player import Player


class Level:
    def __init__(self, level_data: list[str], surface: pygame.Surface):
        self.display_surface: pygame.Surface = surface
        self.player = pygame.sprite.GroupSingle()
        self.terrain_tiles: pygame.sprite.Group = pygame.sprite.Group()
        self.world_shift = 0
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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.terrain_tiles.update(self.world_shift)
        self.player.draw(self.display_surface)
        self.scroll_x()
        self.terrain_tiles.draw(self.display_surface)
