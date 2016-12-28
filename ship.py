import pygame


class Ship(object):

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its inital position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its bounding rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # move each new ship to the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust the position of ship according to the moving flag"""
        # update the value of the ship's center instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw a ship at the assigned position"""
        self.screen.blit(self.image, self.rect)
