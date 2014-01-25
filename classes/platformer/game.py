import pygame
from random import choice
from constants import *
from player import *
from blocks import BlockManager

"""Base Game

This is a basic game stub from which to expand upon.
"""


#Input
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN
QUIT = pygame.QUIT
ESC_KEY = pygame.K_ESCAPE


class Game(object):
    def main(self, screen):
        global delta_time

        """ game stuff """
        clock = pygame.time.Clock()
        running = True

        """ sprite stuff """
        player = Player()
        sprite_group = pygame.sprite.Group()
        sprite_group.add(player)
        bgcolor = WHITE

        block_mgr = BlockManager()

        """ hey look! A Game loop! """
        while running:
            # lock frames at 60 fps
            # TODO(caleb): separate draw and update logic based off time if needed.
            fps = 60
            ms_since_last_tick = clock.tick(fps)
            delta_time = 1.0 / float(ms_since_last_tick)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == ESC_KEY:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == UP_KEY:
                    player.move_up()
                if event.type == pygame.KEYDOWN and event.key == DOWN_KEY:
                    player.move_down()
                if event.type == pygame.KEYDOWN and event.key == RIGHT_KEY:
                    player.move_right()
                if event.type == pygame.KEYDOWN and event.key == LEFT_KEY:
                    player.move_left()

            player.update(delta_time)
            screen.fill(bgcolor)
            sprite_group.draw(screen)

            block_mgr.on_draw(screen)

            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Game().main(screen)
