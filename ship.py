import pygame

class Ship:
    '''A class to manage the ship'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position'''

        self.screen = ai_game.screen # assign screen to an attribute
        self.settings = ai_game.settings # create a settings attribute for ship, so we can use it in update()
        self.screen_rect = ai_game.screen.get_rect() # acces screens rect attribute using the get_rect(method)

        # Load the ship image and get it's rect
        self.image = pygame.image.load("/Volumes/fuckTheSystem/Part2/Alien Invasion/img/spaceship.bmp") # Load the image 
        width, height = 100, 70 # set desire size
        self.image = pygame.transform.scale(self.image, (width, height)) # Scale the image to the desired size
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False 
        self.moving_left = False

    def update(self):
        '''Update the ship's possition based on the movement flag'''
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right: # This code checks the position of thee ship before changing the value of self.x.
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x


    def blitme(self):
        '''Draw the ship  '''
        self.screen.blit(self.image, self.rect)