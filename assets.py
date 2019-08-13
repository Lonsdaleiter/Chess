import pygame
import config


def load_image(path):
    return pygame.image.load(path)


def scale_image(image, x_factor, y_factor):
    return pygame.transform.scale(image, (x_factor, y_factor))


background_image = load_image("res/board.png")
background_image = scale_image(background_image, config.WIDTH, config.HEIGHT)
