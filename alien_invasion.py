import sys

import pygame


def run_game():
    # initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # set the background color
    bg_color = (230, 230, 230)

    # start the main game loop
    while True:
        # listen to the events of the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen each loop
        screen.fill(bg_color)

        # make the latest display visible
        pygame.display.flip()

run_game()
