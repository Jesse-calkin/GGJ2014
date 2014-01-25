import pygame
from spritesheet_functions import *
import pygame.math

"""
Player class
"""


class Player(pygame.sprite.Sprite):
    """ 
    Initialize and set default vectors
    """
    position = pygame.math.Vector2(200,0)
    impulse = pygame.math.Vector2(0,0)

    # holding our animation frames for now
    frames = []

    # Constructor. Can also take color, width, height
    def __init__(self):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)


        sprite_sheet = SpriteSheet("../../resources/sprites/pac.png")
        frame = sprite_sheet.getImage(0, 0, 102, 104)
        self.frames.append(frame)
        frame = sprite_sheet.getImage(0, 102, 102, 104)
        self.frames.append(frame)

        # Fetch the rectangle object that has the dimensions of the image
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect()

        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def applyImpulse(self,vec2):
        impulseToApply = vec2
        if not impulseToApply.is_normalized():
            impulseToApply = impulseToApply.normalize()
            print 'applying impulse', impulseToApply
        self.impulse = impulseToApply

    def move_up(self):
        upVec = pygame.math.Vector2(0,-1)
        self.applyImpulse(upVec)

    def move_down(self):
        downVec = pygame.math.Vector2(0,1)
        self.applyImpulse(downVec)

    def move_right(self):
        rightVec = pygame.math.Vector2(1,0)
        self.applyImpulse(rightVec)

    def move_left(self):
        leftVec = pygame.math.Vector2(-1,0)
        self.applyImpulse(leftVec)

    def animate(self):
        if self.image == self.frames[0]:
            self.image = self.frames[1]
        else:
            self.image = self.frames[0]

    def update(self):
        self.rect.x += self.impulse.x
        self.rect.y += self.impulse.y
        self.animate()
