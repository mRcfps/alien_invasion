import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to key-down"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """respond to key-up"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """respond to the keyboard events and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """update the image on the screen, and switch to the new screen"""
    # re-paint the screen each loop
    screen.fill(ai_settings.bg_color)

    # repaint all the bullets after the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # make recent paint visible
    pygame.display.flip()


def update_bullets(bullets):
    """update the position of the bullet, and delete the disappeared bulelts"""
    # update the position
    bullets.update()

    # remove bullets that has disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """if bullet num has not reached its limit, then fire one"""
    # create a bullet and add it into the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
