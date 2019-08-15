'''
A module containing the Piece
class to be used in other files.

- Lonsdaleiter
'''


import pygame
import utils
import gamemanager


class Piece(pygame.sprite.Sprite):

    def __init__(self, image, unit_type, allegiance, window, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = image  # don't use the image's rectangle

        real_coords = utils.board_to_coord(x, y)
        self.rect = pygame.Rect(real_coords[0], real_coords[1], image.get_width(), image.get_height())

        self.unit_type = unit_type
        self.allegiance = allegiance

        self.window = window

        self.x = x
        self.y = y

        gamemanager.group.append(self)

    def kill(self):
        gamemanager.group.remove(self)

    def draw(self):
        self.window.blit(self.image, utils.board_to_coord(self.x, self.y))

    def scale(self, scale):
        self.image = pygame.transform.scale(self.image,
                                            (int(self.image.get_width() * scale),
                                             int(self.image.get_height() * scale)))

    def move(self, nx, ny):
        c = utils.coord_to_board(nx, ny)
        self.x = c[0]
        self.y = c[1]
        self.rect = pygame.Rect(nx, ny, self.image.get_width(), self.image.get_height())
