'''
A module for the creation of the
board and the updating
of the gamemanager.

- Lonsdaleiter
'''

import pygame
import piece as piecemod
import gamemanager


def init(window):
    data = open("board.dat").read()

    # setting up the group map
    gamemanager.group_map = [[False for _a in range(8)] for _b in range(8)]

    # for parsing the board.dat file
    for i, row in enumerate(data.split("/")):
        for j, piece in enumerate(row.split(";")):
            if len(piece) > 1:
                img = pygame.image.load("res/" + piece.split("-")[0].strip() + piece.split("-")[1] + ".png")
                img = pygame.transform.scale(img, (56, 56))
                piecemod.Piece(img, piece.split("-")[1], piece.split("-")[0].replace("\n", ""), window, j, i)

    for i, piece in enumerate(gamemanager.group):  # filling the group map
        gamemanager.group_map[piece.x][piece.y] = True


# unnecessary middleman function
def update():
    gamemanager.update()
