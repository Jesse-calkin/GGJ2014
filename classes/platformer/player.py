import pygame
from spritesheet_functions import *

"""
Player class
"""


class Player(pygame.sprite.Sprite):

    # Constructor. Can also take color, width, height
    def __init__(self):

        # Call the parent class (Sprite) constructor - like calling super
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        sprite_sheet = SpriteSheet("../../resources/sprites/nyan_cat.png")
        self.image = sprite_sheet.getImage(13, 131, 32, 30)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
