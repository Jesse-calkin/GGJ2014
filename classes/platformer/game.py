import pygame
from random import choice
from constants import *
from player import *

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
        """ game stuff """
        clock = pygame.time.Clock()
        running = True

        """ sprite stuff """
        player = Player()
        player.rect.y = 400
        player.rect.x = 400
        sprite_group = pygame.sprite.Group()
        sprite_group.add(player)

        """ hey look! A Game loop! """
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == ESC_KEY:
                    running = False
            bgcolor = choice(TASTE_THE_RAINBOW)
            screen.fill(bgcolor)
            sprite_group.draw(screen)
            pygame.display.flip()
            clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Game().main(screen)
