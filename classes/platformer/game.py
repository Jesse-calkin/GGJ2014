import pygame
import sys
from random import choice
from constants import *
from player import *
from enemy import *
from powerup import *
from blocks import BlockManager
from parallax import *
from sound import *



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
SPACE_KEY = pygame.K_SPACE
JUMP_KEY = pygame.K_a

class Game(object):
    branch_scores =[0,0]
    total_score = 0
    evolv_threshold = 10

    def should_transition(self):
        if self.branch_scores[0] >= self.evolv_threshold:
            return True,1
        elif self.branch_scores[1] >= self.evolv_threshold:
            return True,2

    def update_scores(self, score_type):
        # pass in a powerup.score_type
        if score_type==1:
            self.branch_scores[0]+=1
        if score_type==2:
            self.branch_scores[1]+=1
        self.total_score += 1

    def main(self, screen):
        global delta_time

        """ game stuff """
        clock = pygame.time.Clock()
        running = True
        paused = False

        """ sprite stuff """
        player = Player()
        player_group = pygame.sprite.Group()
        player_group.add(player)
        bgcolor = WHITE

        enemy = Enemy()
        enemy_group = pygame.sprite.Group()
        enemy_group.add(enemy)

        powerup_mgr = PowerupManager()

        block_mgr = BlockManager()

        """background stuff"""
        bg = ParallaxSurface(pygame.RLEACCEL)
        bg.add('../../resources/backgrounds/testbackground.png', 5)
        bg.add('../../resources/backgrounds/testforeground.png', 2)
        speed = 5
        t_ref = 0
        backgroundy = -600

        "sound stuff"
        Sound.start()
        sounds = [sound_tuple_walk]
        Sound.load_sounds(sounds)

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
                    if event.key == SPACE_KEY:
                        paused = not paused
                    # Do not send these events if we are paused
                    if not paused:
                        if event.key == UP_KEY:
                            player.move_up()
                            self.update_scores(2)
                        if event.key == DOWN_KEY:
                            player.move_down()
                            self.update_scores(1)
                        if event.key == RIGHT_KEY:
                            player.move_right()
                        if event.key == LEFT_KEY:
                            player.move_left()
                        if event.key == JUMP_KEY:
                            player.jump()

            #If we aren't paused, do this stuff
            if not paused:
                # Update operaions
                bg.scroll(speed)
                player.update(delta_time)
                enemy_group.update(delta_time)
                block_mgr.update(-80.0, delta_time)
                powerup_mgr.update(-80.0, delta_time)

            # Drawing operations
            #screen.fill(bgcolor)
            bg.draw(screen, backgroundy)
            player_group.draw(screen)
            block_mgr.on_draw(screen)
            enemy_group.draw(screen)
            powerup_mgr.on_draw(screen)
            pygame.display.flip()
            caption = 'FPS: %s | SCORE: %s | TRANSITION? %s' %(str(clock.get_fps()).split('.')[0], str(self.total_score), str(self.should_transition()))
            pygame.display.set_caption(caption)

if __name__ == '__main__':
    pygame.init()
    print 'Pygame Version:',pygame.ver, '\nDisplay Driver:',pygame.display.get_driver()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    Game().main(screen)
