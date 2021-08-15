import pygame as pg

from player import Player
from helper import res
from settings import *


pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(GAME_TITLE)
pg.display.set_icon(pg.image.load(res/'sprites'/'frog.png'))

player = Player(res/'sprites'/'player_sheet.png', (100, 100))
all_sprites = pg.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                    and event.key == pg.K_ESCAPE):
            running = False

    player.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    clock.tick(FPS)
    pg.display.flip()

