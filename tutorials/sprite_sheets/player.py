import pygame

from spritesheet_functions import *
from platforms import *

class Player(pygame.sprite.Sprite): 
    """ This class represents the bar at the bottom that the player controls. """
  
    # -- Attributes 
    # Set speed vector of player
    change_x = 0
    change_y = 0
    
    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # Where the player is as far as the side-scroller is concerned
    world_shift = 0    
    
    # List of sprites we can bump against
    level = None
    
    # -- Methods 
    def __init__(self): 
        """ Constructor function """ 
        
        # Call the parent's constructor 
        pygame.sprite.Sprite.__init__(self) 
        
        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.getImage(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.getImage(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.getImage(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.getImage(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.getImage(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.getImage(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.getImage(0, 186, 70, 90)
        self.walking_frames_r.append(image)
        
        # Load all the right facing images, then flip them 
        # to face left.
        image = sprite_sheet.getImage(0, 0, 66, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.getImage(66, 0, 66, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.getImage(132, 0, 67, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.getImage(0, 93, 66, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.getImage(66, 93, 66, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.getImage(132, 93, 72, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.getImage(0, 186, 70, 90)
        image = pygame.transform.flip(image,True,False)
        self.walking_frames_l.append(image)        
        
        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
  
        # Set a referance to the image rect.
        self.rect = self.image.get_rect() 
      
    def update(self): 
        """ Move the player. """
        # Gravity
        self.calc_grav()
        
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
            
        #print([((self.rect.x + self.world_shift) // 30) % len(self.walking_frames)])
        
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right, 
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y
        
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) 
        for block in block_hit_list:

            # We hit something below us. Set the boolean to flag that we can jump
            if self.change_y > 0:
                self.jump_ok = True

            # Keep track of the last time we hit something
            self.frame_since_collision = 0

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top 
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
            
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

        # If we haven't hit anything in a while, allow us jump
        if self.frame_since_collision > 3:
            self.jump_ok = False

        # Increment frame counter, used for jumping
        self.frame_since_collision += 1

    def calc_grav(self):
        """ Calculate effect of gravity. """ 
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.frame_since_collision = 0
            self.jump_ok = True

    def jump(self):
        """ Called when user hits 'jump' button. """ 
        
        # move down a bit and see if there is a platform below us
        self.rect.y += 1
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 1
        
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
            
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        if self.jump_ok:
            self.change_x = -6
            self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        if self.jump_ok:
            self.change_x = 6
            self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        