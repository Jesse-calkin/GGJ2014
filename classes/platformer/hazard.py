import pygame
from pygame.sprite import Group
from pygame.transform import scale, rotate
from spritesheet_functions import *
from vector import V2

import constants

class Hazard(pygame.sprite.Sprite):

    timer = 0
    # holding our animation frames for now
    frames = []

    group = Group()

    velocity = V2(-1, 0)

    rotates = False
    current_angle = 0

    # Constructor. Can also take color, width, height
    def __init__(self, start_location):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

        self.group.empty()
        self.group.add(self)

        sprite_sheet = SpriteSheet("resources/sprites/pac.png")
        frame = sprite_sheet.getImage(35, 25, 35, 18)
        self.frames.append(frame)

        # TODO: size these hazards based off sprites.
        height = 50
        width = 100

        start_y = 0
        start_x = 0

        if start_location == "bottom":
            start_y = constants.SCREEN_HEIGHT - height
            start_x = constants.SCREEN_WIDTH

        elif start_location == "bottom_rotate":
            start_y = constants.SCREEN_HEIGHT - height
            start_x = constants.SCREEN_WIDTH - 75
            self.rotates = True

        start_y = 0 if start_location == "top" else constants.SCREEN_HEIGHT - height
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.root_image = scale(self.frames[0], [self.rect.w, self.rect.h])
        self.image = self.root_image

    def update(self, scroll_speed, delta_time):
        self.rect.x += scroll_speed * self.velocity.x * delta_time

        if self.rotates:
            self.current_angle += 1
            self.image = rotate(self.root_image, self.current_angle)

        if self.rect.right < 0:
            self.kill()
            return
        elif self.rect.x <= 0:
            self.rect.x += -1

        if self.timer > .5:
            self.animate()
            self.timer = 0

    def animate(self):
        pass

    def collided(self, collided_with):
        pass

    def on_update(self, scroll_speed, delta_time):
        self.group.update(scroll_speed, delta_time)

    def on_draw(self, surface):
        self.group.draw(surface)
