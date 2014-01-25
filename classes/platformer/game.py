import pygame
import sys
from random import choice
from constants import *
from player import *
from paralaxx import *



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
        #clock = pygame.time.Clock()
        running = True

        """ sprite stuff """
        player = Player()
        player.rect.y = 400
        player.rect.x = 400
        sprite_group = pygame.sprite.Group()
        sprite_group.add(player)

        """background stuff"""
        bg = parallax.ParallaxSurface(pygame.RLEACCEL)
        bg.add('../../resources/backgrounds/testbackground.png', 5)
        bg.add('../../resources/backgrounds/testforeground.png', 2)

        speed = 10
        t_ref = 0

        """ hey look! A Game loop! """
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            bg.scroll(speed)
            t = pygame.time.get_ticks()
            if (t - t_ref) > 60:
                bg.draw(screen)
                pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    Game().main(screen)
