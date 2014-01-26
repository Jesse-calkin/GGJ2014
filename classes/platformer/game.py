import pygame
import sys
import os
from random import choice
from constants import *
from player import *
from enemy import *
from powerup import *
from blocks import BlockManager
from parallax import *
from sound import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

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
FULLSCREEN_KEY = pygame.K_f

class Game(object):
    branch_scores =[0,0]
    total_score = 0
    evolv_threshold = 10
    is_fullscreen = False
    world_speed = 1.0  # 1x
    max_speed = 4.0
    speed_increase = 0.0015
    last_speed_increase = 0  # last time the speed was increased

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
    
    def toggle_fullscreen(self):
        self.paused = True
        if not self.is_fullscreen:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF|pygame.FULLSCREEN)
            self.is_fullscreen = True
        elif self.is_fullscreen:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
            self.is_fullscreen = False
        self.paused = False

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
        bg.add('../../resources/backgrounds/primordial.jpg', 5)
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

            if self.world_speed < self.max_speed:
                self.world_speed += self.speed_increase

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
                        if event.key == FULLSCREEN_KEY:
                            self.toggle_fullscreen()
                        # if event.key == RIGHT_KEY:
                        #     player.move_right()
                        # if event.key == LEFT_KEY:
                        #     player.move_left()
                        # if event.key == JUMP_KEY and player.on_ground:
                        #     player.jump()

            #If we aren't paused, do this stuff
            if not paused:
                # Update operaions
                bg.scroll(speed)
                player.update(delta_time)
                enemy_group.update(delta_time)
                block_mgr.update(self.world_speed, delta_time)
                powerup_mgr.update(self.world_speed, delta_time)

            powerup = pygame.sprite.spritecollideany(player, powerup_mgr.group)
            if powerup:
                print "collided with powerup: %s" % powerup.powerup_type
                powerup.collided(player)
                self.update_scores(powerup.powerup_type)

            block = pygame.sprite.spritecollideany(player, block_mgr.obstacle_group)
            if block:
                player.rect.bottom = block.rect.top
                player.on_ground = True
                print 'on ground'
                player.impulse.y = 0


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
