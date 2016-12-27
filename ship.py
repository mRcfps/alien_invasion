import pygame


class Ship(object):

    def __init__(self, screen):
        """initialize the ship and set its inital position"""
        self.screen = screen

        # load the ship image and get its bounding rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # move each new ship to the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw a ship at the assigned position"""
        self.screen.blit(self.image, self.rect)
