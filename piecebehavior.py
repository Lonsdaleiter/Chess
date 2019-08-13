import turnmanager


def can_move(unit, board, x, y, nx, ny):
    if x == nx and y == ny:
        return False

    if unit.allegiance != turnmanager.current_player:
        return False

    if unit.unit_type == "queen":
        return _queen(unit, board, x, y, nx, ny)
    if unit.unit_type == "bishop":
        return _bishop(unit, board, x, y, nx, ny)
    if unit.unit_type == "rook":
        return _rook(unit, board, x, y, nx, ny)
    if unit.unit_type == "pawn":
        return _pawn(unit, board, x, y, nx, ny)
    if unit.unit_type == "king":
        return _king(unit, board, x, y, nx, ny)
    if unit.unit_type == "knight":
        return _knight(unit, board, x, y, nx, ny)
    return False


def _queen(unit, board, x, y, nx, ny):
    return (is_diagonal(x, y, nx, ny) or is_straight(x, y, nx, ny))\
        and not is_unit_in_path(board, x, y, nx, ny)


def _bishop(unit, board, x, y, nx, ny):
    return is_diagonal(x, y, nx, ny) and not is_unit_in_path(board, x, y, nx, ny)


def _rook(unit, board, x, y, nx, ny):
    return is_straight(x, y, nx, ny) and not is_unit_in_path(board, x, y, nx, ny)


def _knight(unit, board, x, y, nx, ny):
    return (abs(x - nx) == 2 and abs(y - ny) == 1) or (abs(x - nx) == 1 and abs(y - ny) == 2)


def _pawn(unit, board, x, y, nx, ny):
    return (is_straight(x, y, nx, ny)
            and abs(y - ny) < (3 if y == (6 if unit.allegiance == "a" else 1) else 2) and
            not board[nx][ny])\
        or (is_diagonal(x, y, nx, ny) and abs(x - nx) == 1 and (board[nx][ny]))


def _king(unit, board, x, y, nx, ny):
    return abs(x - nx) <= 1 and abs(y - ny) <= 1


def is_diagonal(x, y, nx, ny):  # the first call to is_straight is to stop division by 0
    return not is_straight(x, y, nx, ny) and (abs(ny - y)) / (abs(nx - x)) == 1


def is_straight(x, y, nx, ny):
    return y - ny == 0 or x - nx == 0


def is_unit_in_path(board, x, y, nx, ny):
    x_direction = 1 if x < nx else (0 if x == nx else -1)
    y_direction = 1 if y < ny else (0 if y == ny else -1)

    temp_x = x
    temp_y = y

    while temp_x != nx or temp_y != ny:
        temp_x += x_direction if temp_x != nx else 0
        temp_y += y_direction if temp_y != ny else 0

        if board[temp_x][temp_y] and not (temp_x == nx and temp_y == ny):
            return True

    return False
