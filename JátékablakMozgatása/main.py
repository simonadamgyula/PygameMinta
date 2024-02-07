import pygame
from settings import screen_width, screen_height, level_map
from level import Level

pygame.init()
screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))
clock: pygame.time.Clock = pygame.time.Clock()

level: Level = Level(level_map, screen)
bg_surf: pygame.Surface = pygame.image.load('./img/BG.png').convert_alpha()
bg_rect: pygame.Rect = bg_surf.get_rect(bottomleft=(0, screen_height))

running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_surf, bg_rect)
    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()