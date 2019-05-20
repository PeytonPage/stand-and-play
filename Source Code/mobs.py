"""
Module for managing platforms.
"""
import pygame
import player
import subprocess

from spritesheet_functions import SpriteSheet

import FinalProject

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

MOB1 = (0, 0, 140, 70)

class Mob(pygame.sprite.Sprite):
    """ Basic mob the user avoids """

    def __init__(self, sprite_sheet_data):
        """ Mob constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("mobs_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.image = pygame.transform.scale(self.image, (int(sprite_sheet.width * 1.5), int(sprite_sheet.height * 1.5)))

        self.rect = self.image.get_rect()

class MovingMob(Mob):
    """ This is a mob that can move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None
            

    def update(self):
        """ Move the mob. If the player is in the way, it will damage the player. """

        # Move left/right
        self.rect.x += (self.change_x * 10)

        # Move up/down
        self.rect.y += (self.change_y * 10)

        # Invincibility (for testing purposes)
        invincible = False

        # Check and see if we the player and restart if hit
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit and (invincible == False):
            FinalProject.Platformer = False
            FinalProject.gameOver = True
            FinalProject.main()

        # Check the boundaries and see if we need to reverse direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
