'''
A miscellaneous utility module.

- Lonsdaleiter
'''


import math


def coord_to_board(x, y):
    return math.floor((x - 15) / 80), math.floor((y - 15) / 80)


def board_to_coord(x, y):
    return x * 80 + 15, y * 80 + 15
