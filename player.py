"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
    
    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("p1_walk.png")
        
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(43, 0, 59, 78)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(154, 0, 70, 79)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(265, 0, 74, 77)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(371, 0, 83, 79)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(21, 83, 100, 80)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(144, 84, 84, 80)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(263, 83, 73, 78)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(381, 83, 66, 77)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(42, 167, 63, 81)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(158, 165, 51, 79)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(270, 166, 60, 79)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(381, 166, 60, 81)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(39, 250, 66, 80)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(144, 248, 81, 83)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(255, 248, 88, 81)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(370, 250, 81, 81)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(36, 332, 70, 82)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(158, 332, 61, 82)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(273, 331, 53, 83)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them to face left.
        image = sprite_sheet.get_image(43, 0, 59, 78)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(154, 0, 70, 79)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(265, 0, 74, 77)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(371, 0, 83, 79)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(21, 83, 100, 80)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(144, 84, 84, 80)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(263, 83, 73, 78)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(381, 83, 66, 77)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(42, 167, 63, 81)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(158, 165, 51, 79)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(270, 166, 60, 79)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(381, 166, 60, 81)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(39, 250, 66, 80)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(144, 248, 81, 83)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(255, 248, 88, 81)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(370, 250, 81, 81)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(36, 332, 70, 82)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(158, 332, 61, 82)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(273, 331, 53, 83)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (sprite_sheet.width * 2, sprite_sheet.height * 2))
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

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
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

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .7

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -20

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -75
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 75
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


    
        

