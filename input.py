from pygame import *


class MouseTracker:

    x = 0
    y = 0

    down = False

    @classmethod
    def set_pos(cls, x, y):
        cls.x = x
        cls.y = y

    @classmethod
    def set_down(cls, down):
        cls.down = down


class Keyboard:

    @classmethod
    def update(cls):
        cls.keys = key.get_pressed()

    @classmethod
    def is_key_down(cls, key):
        return cls.keys[key]
