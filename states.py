from board import *
from pygame import *
from configurable import *
from turn_manager import *

background_image = image.load("res/board.png")  # don't really know where besides here to put this...
background_image = transform.scale(background_image, (Config.width, Config.height))


class StateManager:

    state = None

    @classmethod
    def set_state(cls, state):
        cls.state = state

    @classmethod
    def get_state(cls):
        return cls.state


class State:

    def update(self, window):
        raise NotImplementedError()


# STATE IMPLEMENTATIONS BELOW


class GameState(State):

    def __init__(self, window):
        Board.init(window)

    def update(self, window):
        window.blit(background_image, (0, 0))
        Board.update()
