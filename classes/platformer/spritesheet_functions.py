"""Spritesheet Functions

Taken from the spritesheet tutorial at http://programarcadegames.com/python_examples/sprite_sheets/
"""
import pygame
import json
from constants import *


class SpriteSheet():
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None
    texture_map = None

    resource_path = '../../resources/sprites/'

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def getImage(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)

        return image

    def get_frames_from_texmap(self,file_name):
        frames = []
        with open(file_name) as infile:
            texture_map = json.load(infile)

        for i in texture_map['frames']:
            image = self.getImage(i['frame']['x'], i['frame']['y'], i['frame']['w'], i['frame']['h'])
            # scale image down by 1/2
            image = pygame.transform.scale(image,(image.get_width()/3,image.get_height()/3))
            frames.append(image)

        return frames