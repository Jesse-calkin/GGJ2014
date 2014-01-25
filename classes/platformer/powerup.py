import pygame
from spritesheet_functions import *
import pygame.math

"""
Powerup class
"""


class Powerup(pygame.sprite.Sprite):
    """ 
    Initialize and set default vectors
    """
    position = pygame.math.Vector2(900,400)
    impulse = pygame.math.Vector2(-7,0)

    class branch_type:
        _none, up, down = range(3)

    timer = 0
    # holding our animation frames for now
    frames = []

    # Constructor. Can also take color, width, height
    def __init__(self):
        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)


        sprite_sheet = SpriteSheet("../../resources/sprites/pac.png")
        frame = sprite_sheet.getImage(88, 218, 82, 83)
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
        self.impulse.x += impulseToApply.x
        self.impulse.y += impulseToApply.y

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

    def set_organism(self,organism):
        self.organism = organism

    def set_branch_type(self,branch_type):
        self.branch_type = branch_type

    def animate(self):
        pass
        # if self.image == self.frames[0]:
        #     self.image = self.frames[1]
        # else:
        #     self.image = self.frames[0]

    def update(self,dt):
        self.rect.x += self.impulse.x
        self.rect.y += self.impulse.y
        self.timer += dt
        
        if self.timer > .5:
            self.animate()
            self.timer = 0
