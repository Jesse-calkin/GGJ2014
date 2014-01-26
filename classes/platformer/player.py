import pygame
import json
from vector import V2
from spritesheet_functions import *
from sound import *
from constants import *

"""
Player class
"""


class Player(pygame.sprite.Sprite):
    """
    Initialize and set default vectors
    """
    impulse = V2(0, 0)
    position = V2(100, 300)
    on_ground = False
    level = None
    is_jumping = False
    jumpulse = V2(0, -150)
    jumptimer = 0

    timer = 0
    # holding our animation frames for now
    frames = []

    # Constructor. Can also take color, width, height
    def __init__(self):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

    def applyImpulse(self, vec2):
        self.impulse.x += vec2.x
        self.impulse.y += vec2.y

    def apply_gravity(self):
        self.applyImpulse(self.level.gravity)

    def jump(self):
        if not self.is_jumping and self.level.gravity.y > 0:
            self.is_jumping = True
            self.applyImpulse(self.jumpulse)
            print 'jump'

    def move_up(self):
        upVec = pygame.math.Vector2(0, -3)
        self.applyImpulse(upVec)
        Sound.play_sound_for_sound_id(sound_id_walk)

    def move_down(self):
        downVec = pygame.math.Vector2(0, 3)
        self.applyImpulse(downVec)
        Sound.play_sound_for_sound_id(sound_id_walk)

    def move_right(self):
        rightVec = pygame.math.Vector2(1, 0)
        self.applyImpulse(rightVec)

    def move_left(self):
        leftVec = pygame.math.Vector2(-1, 0)
        self.applyImpulse(leftVec)

    def set_organism(self, organism):
        self.organism = organism

    def animate(self):
        if self.image == self.frames[0]:
            self.image = self.frames[0]
        else:
            self.image = self.frames[0]

    def update(self, dt):
        self.timer += dt
        self.rect.x += self.impulse.x * dt
        self.rect.y += self.impulse.y * dt

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.impulse.x = 0
        if self.rect.x < 0:
            self.rect.x = 0
            self.impulse.x = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.impulse.y = 0

        if self.rect.y < 0:
            self.rect.y = 0
            self.impulse.y = 0

        if self.is_jumping:
            if self.jumptimer == 0:
                self.jumptimer += dt
            elif self.jumptimer > .4:
                self.apply_gravity()
            else:
                self.jumptimer += dt

        if not self.is_jumping:
            self.apply_gravity()

        if self.timer > .5:
            self.animate()
            self.timer = 0

    def update_sprite(self, filename1, filename2):
        sprite_sheet = SpriteSheet(filename1)
        self.frames = sprite_sheet.get_frames_from_texmap(filename2)
        self.image = self.frames[2]
        self.rect = self.frames[2].get_rect()
        # Fetch the rectangle object that has the dimensions of the image
        self.rect.x = self.position.x
        self.rect.y = self.position.y
