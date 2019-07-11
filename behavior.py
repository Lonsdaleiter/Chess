from turn_manager import *


class Behavior:

    @classmethod
    def can_move(cls, unit, board, x, y, nx, ny):
        if x == nx and y == ny:
            return False

        if unit.allegiance != Turn.current_player:
            print(unit.allegiance)
            return False

        if unit.unit_type == "queen":
            return cls._queen(unit, board, x, y, nx, ny)
        if unit.unit_type == "bishop":
            return cls._bishop(unit, board, x, y, nx, ny)
        if unit.unit_type == "rook":
            return cls._rook(unit, board, x, y, nx, ny)
        if unit.unit_type == "pawn":
            return cls._pawn(unit, board, x, y, nx, ny)
        if unit.unit_type == "king":
            return cls._king(unit, board, x, y, nx, ny)
        if unit.unit_type == "knight":
            return cls._knight(unit, board, x, y, nx, ny)
        return False

    @classmethod
    def _queen(cls, unit, board, x, y, nx, ny):
        return (cls.is_diagonal(x, y, nx, ny) or cls.is_straight(x, y, nx, ny))\
            and not cls.is_unit_in_path(board, x, y, nx, ny)

    @classmethod
    def _bishop(cls, unit, board, x, y, nx, ny):
        return cls.is_diagonal(x, y, nx, ny) and not cls.is_unit_in_path(board, x, y, nx, ny)

    @classmethod
    def _rook(cls, unit, board, x, y, nx, ny):
        return cls.is_straight(x, y, nx, ny) and not cls.is_unit_in_path(board, x, y, nx, ny)

    @staticmethod
    def _knight(unit, board, x, y, nx, ny):
        return (abs(x - nx) == 2 and abs(y - ny) == 1) or (abs(x - nx) == 1 and abs(y - ny) == 2)

    @classmethod
    def _pawn(cls, unit, board, x, y, nx, ny):
        return (cls.is_straight(x, y, nx, ny)
                and abs(y - ny) < (3 if y == (6 if unit.allegiance == "a" else 1) else 2) and
                not board[nx][ny])\
            or (cls.is_diagonal(x, y, nx, ny) and abs(x - nx) == 1 and (board[nx][ny]))

    @staticmethod
    def _king(unit, board, x, y, nx, ny):
        return abs(x - nx) <= 1 and abs(y - ny) <= 1

    @classmethod
    def is_diagonal(cls, x, y, nx, ny):  # the first call to is_straight is to stop division by 0
        return not cls.is_straight(x, y, nx, ny) and (abs(ny - y)) / (abs(nx - x)) == 1

    @staticmethod
    def is_straight(x, y, nx, ny):
        return y - ny == 0 or x - nx == 0

    @classmethod
    def is_unit_in_path(cls, board, x, y, nx, ny):
        xDirection = 1 if x < nx else (0 if x == nx else -1)
        yDirection = 1 if y < ny else (0 if y == ny else -1)

        print("Direction: " + str(xDirection), str(yDirection))

        tempX = x
        tempY = y

        while tempX != nx or tempY != ny:
            tempX += xDirection if tempX != nx else 0
            tempY += yDirection if tempY != ny else 0

            print("Checking pos: " + str(tempX), str(tempY))

            print("Destination: " + str(nx), str(ny))

            if board[tempX][tempY] and not (tempX == nx and tempY == ny):
                return True

        return False
