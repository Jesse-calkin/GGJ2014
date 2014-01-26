import pygame
import pygame._view
import sys
import os
from random import choice
from constants import *
from player import *
from powerup import *
from blocks import BlockManager
from parallax import *
from sound import *
from level import *
from hazard import Hazard
from music import *

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
    level_score = 0
    total_score = 0
    player = None
    evolv_threshold = 10
    is_fullscreen = False
    world_speed = 1.0  # 1x
    max_speed = 10.0
    speed_increase = 0.002
    last_speed_increase = 0  # last time the speed was increased

    level = Level.first_level()

    bg = ParallaxSurface(pygame.RLEACCEL)

    block_mgr = None
    hazard = None

    def update_background_images_for_current_level(self):
        Game.bg.remove()
        Game.bg.add(self.level.background_filepath, 5)
        Game.bg.add(self.level.foreground_filepath, 2)

    def update_player_for_current_level(self, player):
        player.level = self.level
        player.update_sprite(self.level.player_sprite_filepath, self.level.player_textmap_filepath)
        if self.level.has_blocks:
            player.on_ground = True

    def update_blocks_for_current_level(self):
        self.block_mgr = BlockManager() if self.level.has_blocks else None

    def update_hazard_for_current_level(self):
        self.hazard = Hazard(self.level.hazard_start_location) \
            if self.level.hazard_start_location else None

    def should_transition(self):
        if self.level_score >= self.level.target_score:
            return True
        else:
            return False

    def reached_the_end(self):
        self.paused = True

    def transition_to_next_level(self):
        self.level_score = 0

        next_level = self.level.next_level()
        if next_level:
            self.level = next_level
            self.update_for_current_level()
        else:
            self.reached_the_end()

    def update_for_current_level(self):
        self.update_background_images_for_current_level()
        self.update_player_for_current_level(self.player)
        self.update_blocks_for_current_level()
        self.update_hazard_for_current_level()

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
        self.player = Player()
        player_group = pygame.sprite.Group()
        player_group.add(self.player)

        powerup_mgr = PowerupManager()

        speed = 5

        "music stuff"
        Music.play()

        "sound stuff"
        Sound.start()
        sounds = [sound_tuple_walk, sound_tuple_eat]
        Sound.load_sounds(sounds)

        self.update_for_current_level()

        is_moving_up = False
        is_moving_down = False

        """ hey look! A Game loop! """
        while running:
            # lock frames at 60 fps
            # TODO(caleb): separate draw and update logic based off time if needed.

            ms_since_last_tick = clock.tick(FRAME_RATE)
            delta_time = 1.0 / float(ms_since_last_tick)

            if pygame.time.get_ticks() - self.last_speed_increase > 5000 \
                and self.world_speed < self.max_speed:

                self.world_speed += self.speed_increase

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == ESC_KEY:
                        running = False
                    if event.type == pygame.KEYDOWN and  event.key == SPACE_KEY:
                        paused = not paused
                    # Do not send these events if we are paused
                    if not paused:
                        if event.type == pygame.KEYDOWN and event.key == UP_KEY:
                            is_moving_up = True
                        elif event.type == pygame.KEYUP and event.key == UP_KEY:
                            is_moving_up = False

                        if event.type == pygame.KEYDOWN and event.key == DOWN_KEY:
                            is_moving_down = True
                        elif event.type == pygame.KEYUP and event.key == DOWN_KEY:
                            is_moving_down = False

                        if event.type == pygame.KEYDOWN and event.key == FULLSCREEN_KEY:
                            self.toggle_fullscreen()
                        # if event.key == RIGHT_KEY:
                        #     player.move_right()
                        # if event.key == LEFT_KEY:
                        #     player.move_left()
                        if event.key == JUMP_KEY:
                            self.player.jump()
            if is_moving_up:
                self.player.move_up()
            elif is_moving_down:
                self.player.move_down()

            #If we aren't paused, do this stuff
            if not paused:
                # Update operaions
                Game.bg.scroll(speed*self.world_speed)
                self.player.update(delta_time)

                if self.block_mgr:
                    self.block_mgr.update(self.world_speed, delta_time)
                powerup_mgr.update(self.world_speed, delta_time)
                if self.hazard:
                    self.hazard.on_update(self.world_speed, delta_time)


            powerup = pygame.sprite.spritecollideany(self.player, powerup_mgr.group)
            if powerup:
                print "collided with powerup: %s" % powerup.powerup_type
                Sound.play_sound_for_sound_id(sound_id_eat)
                powerup.collided(self.player)
                self.level_score = self.level_score + 1
                self.total_score = self.total_score + 1
                if self.should_transition():
                    self.transition_to_next_level()

            if self.block_mgr:
                block = pygame.sprite.spritecollideany(
                    self.player, self.block_mgr.obstacle_group)

                if block:
                    self.player.rect.bottom = block.rect.top
                    self.player.on_ground = True
                    if self.player.is_jumping:
                        self.player.is_jumping = False
                    print 'on ground'
                    self.player.impulse.y = 0

            if self.hazard and pygame.sprite.collide_rect(self.player, self.hazard):
                print "Player hit hazard!"

            # Drawing operations
            Game.bg.draw(screen)
            player_group.draw(screen)
            if self.block_mgr:
                self.block_mgr.on_draw(screen)
            if self.hazard:
                self.hazard.on_draw(screen)

            powerup_mgr.on_draw(screen)
            pygame.display.flip()
            caption = 'FPS: %s | LEVEL SCORE: %s | TOTAL SCORE: %s | TRANSITION? %s' %(str(clock.get_fps()).split('.')[0], str(self.level_score), self.total_score, str(self.should_transition()))
            pygame.display.set_caption(caption)

if __name__ == '__main__':
    pygame.init()
    print 'Pygame Version:',pygame.ver, '\nDisplay Driver:',pygame.display.get_driver()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    Game().main(screen)
