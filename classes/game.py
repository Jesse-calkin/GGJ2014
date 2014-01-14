import pygame

"""Base Game

This is a basic game stub from which to expand upon.
"""

#Global Game Constants
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 600
FRAME_RATE = 30
DELTA_TIME = pygame.time.Clock().tick(60)

#Input
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN
QUIT = pygame.QUIT
ESC_KEY = pygame.K_ESCAPE


class Game(object):
    def main(self, screen):
    	clock = pygame.time.Clock()

    	running = True
    	
    	""" hey look! A Game loop! """
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == ESC_KEY:
                    running = False
            screen.fill((105,180,200))
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Game().main(screen)