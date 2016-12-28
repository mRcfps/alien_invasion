import sys

import pygame


def check_events():
    """respond to the keyboard events and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """update the image on the screen, and switch to the new screen"""
    # re-paint the screen each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make recent paint visible
    pygame.display.flip()
