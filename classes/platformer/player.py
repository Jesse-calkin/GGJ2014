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
    impulse = V2(0,0)
    position = V2(100,300)
    on_ground = False
    level = None
    is_jumping = False
    jumpulse = (0,5)
    jumptimer = 0

    timer = 0
    # holding our animation frames for now
    frames = []

    # Constructor. Can also take color, width, height
    def __init__(self):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("../../resources/sprites/SpriteTest.png")

        self.frames = sprite_sheet.get_frames_from_texmap("../../resources/sprites/SpriteTest.json")
        
        # Fetch the rectangle object that has the dimensions of the image
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect()

        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def applyImpulse(self,vec2):
        self.impulse.x += vec2.x
        self.impulse.y += vec2.y

    def apply_gravity(self):
        self.applyImpulse(self.level.gravity)

    def jump(self,dt):
        if not self.is_jumping:
            self.is_jumping = True
            self.applyImpulse(self.jumpulse)
            self.jumptimer += dt


    def move_up(self):
        upVec = pygame.math.Vector2(0, -3)
        self.applyImpulse(upVec)
        Sound.play_sound_for_sound_id(sound_id_walk)

    def move_down(self):
        downVec = pygame.math.Vector2(0, 3)
        self.applyImpulse(downVec)
        Sound.play_sound_for_sound_id(sound_id_walk)

    def move_right(self):
        rightVec = pygame.math.Vector2(1,0)
        self.applyImpulse(rightVec)

    def move_left(self):
        leftVec = pygame.math.Vector2(-1,0)
        self.applyImpulse(leftVec)

    def set_organism(self,organism):
        self.organism = organism

    def animate(self):
        if self.image == self.frames[0]:
            self.image = self.frames[1]
        else:
            self.image = self.frames[0]

    def update(self,dt):
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

        if self.is_jumping and self.jumptimer > .3:
            self.apply_gravity()
        
        if not self.is_jumping:
            self.apply_gravity()

        if self.timer > .5:
            self.animate()
            self.timer = 0
