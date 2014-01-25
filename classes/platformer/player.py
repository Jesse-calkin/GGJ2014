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
    position = pygame.math.Vector2(0,0)
    impulse = pygame.math.Vector2(0,0)
    # Constructor. Can also take color, width, height
    def __init__(self):

        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("../../resources/sprites/pac.png")
        self.image = sprite_sheet.getImage(13, 131, 32, 30)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
    def applyImpulse(vec2):
        impulseToApply = vec2
        pass