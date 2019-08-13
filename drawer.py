import pygame


window = None


def draw(image, x, y):
    global window

    window.blit(image, (x, y))
