import pygame

import constants
import platforms
import mobs

HEIGHT = 984
scale_y = 984/600
scale_x = 1824 / 800

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
    
    

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -20000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """
        # Draw the background
        screen.fill(constants.WHITE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Tutorial
class Level_00(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_00.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -5400

# Pangea
class Level_01(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
        
        # Array with type of platform, and x, y location of the platform.
        level = [ 
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = scale_y *platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 3000
        block.rect.y = scale_y *200
        block.boundary_left = scale_x *  1600
        block.boundary_right = scale_x *  6750
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  450
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 2600
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 3600
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 4600
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1550
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  1549
        block.boundary_right = scale_x *  1550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *460
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 3750
        block.rect.y = scale_y *530 
        block.boundary_left = scale_x *  1749
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 3750
        block.rect.y = scale_y *460 
        block.boundary_left = scale_x *  1749
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Greece
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_03.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
        
        # Array with type of platform, and x, y location of the platform.
        level = [
                    ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = scale_y *platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  1749
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1750
        block.rect.y = scale_y *460
        block.boundary_left = scale_x *  1749
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1750
        block.rect.y = scale_y *390
        block.boundary_left = scale_x *  1749
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1750
        block.rect.y = scale_y *320
        block.boundary_left = scale_x *  1749
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 2500
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  1
        block.boundary_bottom = scale_y *  550
        block.change_y = -6
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *460
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *390
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *320
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *250
        block.boundary_left = scale_x *  2749
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 4000
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -12
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  4249
        block.boundary_right = scale_x *  4250
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *460
        block.boundary_left = scale_x *  4249
        block.boundary_right = scale_x *  4250
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *390
        block.boundary_left = scale_x *  4249
        block.boundary_right = scale_x *  4250
        block.change_x = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *320
        block.boundary_left = scale_x *  4249
        block.boundary_right = scale_x *  4250
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *250
        block.boundary_left = scale_x *  4249
        block.boundary_right = scale_x *  4250
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *180
        block.boundary_left = scale_x *  4249
        block.boundary_right = scale_x *  4250
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 5000
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  5000
        block.boundary_right = scale_x *  8000
        block.change_x = -15
        block.player = self.player
        block.level = self
        self.platform_list.add(block)        


# China
class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_04.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
        
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM, 570, 500],
                  [platforms.STONE_PLATFORM, 870, 400],
                  [platforms.STONE_PLATFORM, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  [platforms.STONE_PLATFORM, 7000, 500],
                  [platforms.STONE_PLATFORM, 6750, 400],
                  [platforms.STONE_PLATFORM, 3000, 300],
                  ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = scale_y *platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = scale_y *300
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  3000
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 2750
        block.rect.y = scale_y *200
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  3000
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 3250
        block.rect.y = scale_y *300
        block.boundary_left = scale_x *  3050
        block.boundary_right = scale_x *  6750
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 6500
        block.rect.y = scale_y *200
        block.boundary_left = scale_x *  3050
        block.boundary_right = scale_x *  6750
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1550
        block.rect.y = scale_y *140
        block.boundary_left = scale_x *  1550
        block.boundary_right = scale_x *  2000
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 5050
        block.rect.y = scale_y *140
        block.boundary_left = scale_x *  5050
        block.boundary_right = scale_x *  5750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *140
        block.boundary_left = scale_x *  4250
        block.boundary_right = scale_x *  4500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Scandinavia
class Level_04(Level):
    """ Definition for level 4. """

    def __init__(self, player):
        """ Create level 4. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_05.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
        
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  1250
        block.boundary_right = scale_x *  1750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  1750
        block.boundary_right = scale_x *  2250
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  2250
        block.boundary_right = scale_x *  2750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 2750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  2750
        block.boundary_right = scale_x *  3250
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 3250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  3250
        block.boundary_right = scale_x *  3750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
                
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 3750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  3750
        block.boundary_right = scale_x *  4250
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
                
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  4250
        block.boundary_right = scale_x *  4750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
                
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  4750
        block.boundary_right = scale_x *  5250
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
                        
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 5250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  5250
        block.boundary_right = scale_x *  5750
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
                
        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 5750
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  5750
        block.boundary_right = scale_x *  6250
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Poland
class Level_05(Level):
    """ Definition for level 5. """

    def __init__(self, player):
        """ Create level 5. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_06.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
        
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM, 570, 500],
                  [platforms.STONE_PLATFORM, 870, 400],
                  [platforms.STONE_PLATFORM, 1070, 500],
                  [platforms.STONE_PLATFORM, 7000, 500],
                  [platforms.STONE_PLATFORM, 6750, 400],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  [platforms.STONE_PLATFORM, 6000, 280],
                  [platforms.STONE_PLATFORM, 6300, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = scale_y *platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  6000
        block.change_x = -7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 2350
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  6000
        block.change_x = -7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 3350
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  6000
        block.change_x = -7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 4350
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  6000
        block.change_x = -7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 5350
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  6000
        block.change_x = -7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = scale_y *200
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = scale_y *400
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = scale_y *300
        block.boundary_top = scale_y *  100
        block.boundary_bottom = scale_y *  550
        block.change_y = -10
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# England
class Level_06(Level):
    """ Definition for level 6. """

    def __init__(self, player):
        """ Create level 6. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_07.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
        
                # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM, 570, 500],
                  [platforms.STONE_PLATFORM, 870, 400],
                  [platforms.STONE_PLATFORM, 1070, 500],
                  [platforms.STONE_PLATFORM, 7000, 500],
                  [platforms.STONE_PLATFORM, 6750, 400],
                  [platforms.STONE_PLATFORM, 6500, 300],
                  [platforms.STONE_PLATFORM, 6250, 300],
                  [platforms.STONE_PLATFORM, 6000, 300],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  [platforms.STONE_PLATFORM, 2100, 280],
                  [platforms.STONE_PLATFORM, 3050, 280],
                  [platforms.STONE_PLATFORM, 4200, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = scale_y *platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  1350
        block.boundary_right = scale_x *  2000
        block.change_x = 6
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 2200
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  2200
        block.boundary_right = scale_x *  2900
        block.change_x = 7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 3800
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  3200
        block.boundary_right = scale_x *  4100
        block.change_x = 8
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 4700
        block.rect.y = scale_y *280
        block.boundary_left = scale_x *  4300
        block.boundary_right = scale_x *  5000
        block.change_x = 7
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 4800
        block.rect.y = scale_y *310
        block.boundary_left = scale_x *  4800
        block.boundary_right = scale_x *  5700
        block.change_x = 5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  1250
        block.boundary_right = scale_x *  1800
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1600
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  1600
        block.boundary_right = scale_x *  3400
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 4000
        block.rect.y = scale_y *530
        block.boundary_left = scale_x *  4000
        block.boundary_right = scale_x *  6000
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Nethken Hall
class Level_07(Level):
    """ Definition for level 7. """

    def __init__(self, player):
        """ Create level 7. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_08.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
