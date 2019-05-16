import pygame

import constants
import platforms
import mobs

HEIGHT = 984

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
    """ Definition for level 0. """

    def __init__(self, player):
        """ Create level 0. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_00.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -5400

# Pangea
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500 * 2],
                  [platforms.GRASS, 870, 400 * 2],
                  [platforms.GRASS, 1070, 500 * 2],
                  [platforms.STONE_PLATFORM, 1190, 280 * 2],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = int(280 * 1.64)
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = 530
        block.boundary_left = 1250
        block.boundary_right = 1500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Egypt
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Greece
class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_03.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = 570
        block.boundary_left = 1250
        block.boundary_right = 1500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# China
class Level_04(Level):
    """ Definition for level 4. """

    def __init__(self, player):
        """ Create level 4. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_04.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  ]

        """ Platforms """

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 2750
        block.rect.y = 280
        block.boundary_left = 2750
        block.boundary_right = 3000
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        """ Mobs """

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = 570
        block.boundary_left = 1250
        block.boundary_right = 2000
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Scandinavia
class Level_05(Level):
    """ Definition for level 5. """

    def __init__(self, player):
        """ Create level 5. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_05.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = 570
        block.boundary_left = 1250
        block.boundary_right = 1500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Middle Ages
class Level_06(Level):
    """ Definition for level 6. """

    def __init__(self, player):
        """ Create level 6. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_06.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = 570
        block.boundary_left = 1250
        block.boundary_right = 1500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# England
class Level_07(Level):
    """ Definition for level 7. """

    def __init__(self, player):
        """ Create level 7. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_07.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS, 570, 500],
                  [platforms.GRASS, 870, 400],
                  [platforms.GRASS, 1070, 500],
                  [platforms.STONE_PLATFORM, 1190, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MOVE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving mob
        block = mobs.MovingMob(mobs.MOB1)
        block.rect.x = 1250
        block.rect.y = 570
        block.boundary_left = 1250
        block.boundary_right = 1500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Nethken Hall
class Level_08(Level):
    """ Definition for level 8. """

    def __init__(self, player):
        """ Create level 8. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_08.png").convert()
        self.background = pygame.transform.scale(self.background, (3840, HEIGHT))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -6200
