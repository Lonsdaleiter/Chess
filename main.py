'''
The main module which
builds the pygame window
and contains the gameloop.

- Lonsdaleiter
'''


import config
import pygame
import drawer
import mouse
import assets
import keyboard
import board
import turnmanager
import time
import os


running = False
window = None
clock = None


def init():
    global running
    global window
    global clock

    pygame.init()
    running = True
    window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

    pygame.display.set_caption("Chess")

    clock = pygame.time.Clock()

    drawer.window = window

    board.init(window)


def update():
    global running
    global window
    global clock

    mouseup = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseup = True
            mouse.down = True

        if not mouseup:
            mouse.down = False

        if event.type == pygame.MOUSEMOTION:
            mouse.x = pygame.mouse.get_pos()[0]
            mouse.y = pygame.mouse.get_pos()[1]

    clock.tick(60)

    drawer.draw(assets.background_image, 0, 0)
    keyboard.update()

    board.update()

    pygame.display.flip()

    if turnmanager.won:
        os.system("say 'Closing the window in 5 seconds'")
        time.sleep(5)
        exit(0)


def end():
    pygame.quit()


if __name__ == "__main__":
    init()
    while running:
        update()
    end()
