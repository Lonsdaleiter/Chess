'''
A module managing the board's
piece data.

- Lonsdaleiter
'''


import keyboard
import pygame
import mouse
import utils
import piecebehavior
import turnmanager
import os


group = []
group_map = []

selected_piece = None


def update():
    global selected_piece
    global group
    global group_map
    
    for piece in group:
        piece.draw()

        if mouse.down and \
                piece.rect.collidepoint((mouse.x, mouse.y)) \
                and selected_piece is None and piece.allegiance == turnmanager.current_player:
            selected_piece = piece
            selected_piece.scale(2)

        if keyboard.is_key_down(pygame.K_ESCAPE) and selected_piece is not None:
            selected_piece.scale(0.5)
            selected_piece = None

        if mouse.down and selected_piece is not None:
            coords = utils.coord_to_board(mouse.x, mouse.y)
            ocoords = selected_piece.x, selected_piece.y

            if piecebehavior.can_move(selected_piece, group_map,
                                      ocoords[0], ocoords[1],
                                      coords[0], coords[1]):

                if group_map[coords[0]][coords[1]]:  # combat
                    p = get_piece_at(coords[0], coords[1])

                    if p.allegiance == selected_piece.allegiance:
                        return

                    if p.unit_type == "king":
                        os.system("say '" + ("blue" if p.allegiance == "a" else "red") + " player has won. Good game.'")
                        turnmanager.won = True
                        # f = pygame.font.Font("freesansbold.ttf", 72)
                        # text = f.render("Player " +
                        #                 selected_piece.allegiance.upper() + " has won!",
                        #                 True, (0, 0, 0), (256, 256, 256))
                        # textrect = text.get_rect()
                        # textrect.center = config.width // 2, config.height // 2

                    p.kill()

                group_map[ocoords[0]][ocoords[1]] = False
                group_map[coords[0]][coords[1]] = True

                selected_piece.scale(0.5)
                c = utils.board_to_coord(coords[0], coords[1])
                selected_piece.move(c[0], c[1])
                selected_piece = None

                turnmanager.switch()


def get_piece_at(x, y):
    global group

    for piece in group:
        if piece.x == x and piece.y == y:
            return piece

    return None
