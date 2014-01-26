import pygame
from pygame.sprite import Group
from pygame.transform import scale
from spritesheet_functions import *
from vector import V2

import constants

class Hazard(pygame.sprite.Sprite):

    timer = 0
    # holding our animation frames for now
    frames = []

    group = Group()

    velocity = V2(-1, 0)

    # Constructor. Can also take color, width, height
    def __init__(self, start_location):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

        self.group.empty()
        self.group.add(self)

        sprite_sheet = SpriteSheet("../../resources/sprites/pac.png")
        frame = sprite_sheet.getImage(35, 25, 35, 18)
        self.frames.append(frame)

        # Fetch the rectangle object that has the dimensions of the image
        # self.image = self.frames[0]
        height = 50
        start_y = 0 if start_location == "top" else constants.SCREEN_HEIGHT - height
        self.rect = pygame.Rect(constants.SCREEN_WIDTH, start_y, 400, height)
        self.image = scale(self.frames[0], [self.rect.w, self.rect.h])

    def update(self, scroll_speed, delta_time):
        self.rect.x += scroll_speed * self.velocity.x * delta_time

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
