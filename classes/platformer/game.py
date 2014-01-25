import pygame
import sys
from random import choice
from constants import *
from player import *
from enemy import *
from powerup import *
from blocks import BlockManager
from parallax import *



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
        player_group = pygame.sprite.Group()
        player_group.add(player)
        bgcolor = WHITE

        enemy = Enemy()
        enemy_group = pygame.sprite.Group()
        enemy_group.add(enemy)

        powerup = Powerup()
        powerup_group = pygame.sprite.Group()
        powerup_group.add(powerup)


        block_mgr = BlockManager()

        """background stuff"""
        bg = ParallaxSurface(pygame.RLEACCEL)
        bg.add('../../resources/backgrounds/testbackground.png', 5)
        bg.add('../../resources/backgrounds/testforeground.png', 2)
        speed = 10
        t_ref = 0

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
                if event.type == pygame.KEYDOWN:
                    if event.key == ESC_KEY:
                        running = False
                    if event.key == UP_KEY:
                        player.move_up()
                    if event.key == DOWN_KEY:
                        player.move_down()
                    if event.key == RIGHT_KEY:
                        player.move_right()
                    if event.key == LEFT_KEY:
                        player.move_left()
            # Update operaions
            bg.scroll(speed)

            player.update(delta_time)
            enemy_group.update(delta_time)
            powerup_group.update(delta_time)
            block_mgr.update(-80.0, delta_time)

            # Drawing operations
            #screen.fill(bgcolor)
            bg.draw(screen)
            player_group.draw(screen)
            block_mgr.on_draw(screen)
            enemy_group.draw(screen)
            powerup_group.draw(screen)
            pygame.display.flip()

            pygame.display.set_caption(str(clock.get_fps()))

if __name__ == '__main__':
    pygame.init()
    print 'Pygame Version:',pygame.ver, '\nDisplay Driver:',pygame.display.get_driver()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    Game().main(screen)
