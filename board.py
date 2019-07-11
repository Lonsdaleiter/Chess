from input import *
from behavior import *
from pygame import *
from configurable import *
from turn_manager import *
import math


class Board:

    @classmethod
    def init(cls, window):
        data = open("default_board.dat").read()

        for i, row in enumerate(data.split("/")):
            for j, piece in enumerate(row.split(";")):
                if len(piece) > 1:
                    img = image.load("res/" + piece.split("-")[0].strip() + piece.split("-")[1] + ".png")
                    img = transform.scale(img, (56, 56))
                    Piece(img, piece.split("-")[1], piece.split("-")[0].replace("\n", ""), window, j, i)

        PieceManager.group_map = [[False for _a in range(8)] for _b in range(8)]

        for i, piece in enumerate(PieceManager.group):
            PieceManager.group_map[piece.x][piece.y] = True

        # for i, row in enumerate(data.split("/")):
        #     r = []
        #     for j, piece in enumerate(row.split(";")):  # x
        #         if len(piece) > 1:
        #             img = image.load("res/" + piece.split("-")[0].strip() + piece.split("-")[1] + ".png")
        #             img = transform.scale(img, (56, 56))
        #
        #             r.append(Piece(img, piece.split("-")[1], piece.split("-")[0], window, j * 80 + 15, i * 80 + 15))
        #         else:
        #             r.append(None)
        #     cls.board.append(r)

    @classmethod
    def update(cls):
        PieceManager.update()

    @classmethod
    def coord_to_board(cls, x, y):
        return math.floor((x - 15) / 80), math.floor((y - 15) / 80)

    @classmethod
    def board_to_coord(cls, x, y):
        # print(math.floor(x * (Config.width / (len(Board.board) - 1))),
        # math.floor(y * (Config.height / (len(Board.board[0]) - 1))))
        return x * 80 + 15, y * 80 + 15


class Piece(sprite.Sprite):

    def __init__(self, image, unit_type, allegiance, window, x, y):
        sprite.Sprite.__init__(self)

        self.image = image  # don't use the image's rectangle

        real_coords = Board.board_to_coord(x, y)
        self.rect = Rect(real_coords[0], real_coords[1], image.get_width(), image.get_height())

        self.unit_type = unit_type
        self.allegiance = allegiance

        self.window = window

        self.x = x
        self.y = y

        PieceManager.group.append(self)

    def kill(self):
        PieceManager.group.remove(self)

    def draw(self):
        self.window.blit(self.image, Board.board_to_coord(self.x, self.y))

    def scale(self, scale):
        self.image = transform.scale(self.image,
                                     (int(self.image.get_width() * scale),
                                      int(self.image.get_height() * scale)))
        #self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self, nx, ny):
        c = Board.coord_to_board(nx, ny)
        self.x = c[0]
        self.y = c[1]
        self.rect = Rect(nx, ny, self.image.get_width(), self.image.get_height())


class PieceManager:

    group = []
    group_map = []

    selected_piece = None

    @classmethod
    def update(cls):
        if Turn.won:
            cls._winning(cls.group[0].window)
            return

        for piece in cls.group:
            piece.draw()

            if MouseTracker.down and \
                    piece.rect.collidepoint((MouseTracker.x, MouseTracker.y)) \
                    and cls.selected_piece is None and piece.allegiance == Turn.current_player:
                cls.selected_piece = piece
                cls.selected_piece.scale(2)

            if Keyboard.is_key_down(K_ESCAPE) and cls.selected_piece is not None:
                cls.selected_piece.scale(0.5)
                cls.selected_piece = None

            if MouseTracker.down and cls.selected_piece is not None:
                coords = Board.coord_to_board(MouseTracker.x, MouseTracker.y)
                ocoords = cls.selected_piece.x, cls.selected_piece.y
                # print(coords[0])
                if Behavior.can_move(cls.selected_piece, cls.group_map,
                                     ocoords[0], ocoords[1],
                                     coords[0], coords[1]):

                    if cls.group_map[coords[0]][coords[1]]:  # combat
                        p = cls.get_piece_at(coords[0], coords[1])

                        if p.allegiance == cls.selected_piece.allegiance:
                            return

                        if p.unit_type == "king":
                            f = font.Font("freesansbold.ttf", 72)
                            cls.text = f.render("Player " +
                                                cls.selected_piece.allegiance.upper() + " has won!",
                                                True, (0, 0, 0), (256, 256, 256))
                            cls.textrect = cls.text.get_rect()
                            cls.textrect.center = Config.width // 2, Config.height // 2
                            Turn.set_won(cls.selected_piece.allegiance)

                        p.kill()

                    cls.group_map[ocoords[0]][ocoords[1]] = False
                    cls.group_map[coords[0]][coords[1]] = True

                    cls.selected_piece.scale(0.5)
                    c = Board.board_to_coord(coords[0], coords[1])
                    cls.selected_piece.move(c[0], c[1])
                    cls.selected_piece = None

                    Turn.switch()

    @classmethod
    def _winning(cls, window):
        window.blit(cls.text, cls.textrect)

    @classmethod
    def get_piece_at(cls, x, y):
        for piece in cls.group:
            if piece.x == x and piece.y == y:
                return piece

        return None
