import pygame
from pygame.sprite import Group
from spritesheet_functions import *
from vector import V2

import constants
from player import Player

import random

POWERUP_VELOCITY = V2(-60, 0)


"""
Powerup class
"""
class Powerup(pygame.sprite.Sprite):
    """
    Initialize and set default vectors
    """

    POWERUP_TYPE_UP = 1
    POWERUP_TYPE_DOWN = 2
    POWERUP_TYPES = [POWERUP_TYPE_UP, POWERUP_TYPE_DOWN]

    powerup_type = None

    timer = 0
    # holding our animation frames for now
    frames = []

    # Constructor. Can also take color, width, height
    def __init__(self):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/sprites/pac.png")
        frame = sprite_sheet.getImage(88, 218, 82, 83)
        self.frames.append(frame)

        # Fetch the rectangle object that has the dimensions of the image
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect()

    def update(self, scroll_speed, delta_time):
        self.rect.x += scroll_speed * POWERUP_VELOCITY.x * delta_time

        if self.rect.right < 0:
            self.mgr.recycle(self)
            return

        if self.timer > .5:
            self.animate()
            self.timer = 0

    def animate(self):
        pass
        # if self.image == self.frames[0]:
        #     self.image = self.frames[1]
        # else:
        #     self.image = self.frames[0]

    def collided(self, collided_with):
        if isinstance(collided_with, Player):
            #TODO animate this or play a noise
            self.mgr.recycle(self)

class PowerupManager(object):

    MAX_ITEMS = 5

    MIN_GAP_X = 200
    MAX_GAP_X = 400

    MAX_GAP_Y = constants.SCREEN_HEIGHT

    last_position = [constants.SCREEN_WIDTH + 100, 0]

    group = Group()

    def __init__(self):
        self.list = []

        for _ in range(self.MAX_ITEMS):
            powerup = Powerup()
            powerup.mgr = self
            self.group.add(powerup)
            self.list.append(powerup)
            self.recycle(powerup)

    def recycle(self, powerup):
        x_gap = random.randint(self.MIN_GAP_X, self.MAX_GAP_X)
        y = random.randint(0, self.MAX_GAP_Y)

        if(y + powerup.rect.h > constants.SCREEN_HEIGHT):
            y = constants.SCREEN_HEIGHT - powerup.rect.h

        powerup.rect.x = self.last_position[0] + x_gap
        powerup.rect.y = y

        powerup.powerup_type = random.choice(Powerup.POWERUP_TYPES)

        self.last_position[0] = powerup.rect.x
        self.last_position[1] = powerup.rect.y

    def update(self, speed, delta_time):
        self.last_position[0] += speed * POWERUP_VELOCITY.x * delta_time
        self.group.update(speed, delta_time)

    def on_draw(self, surface):
        self.group.draw(surface)
