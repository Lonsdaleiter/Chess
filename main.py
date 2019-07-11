from states import *
from input import *
from configurable import *
import pygame


class Engine:

    running = False
    window = None
    clock = None

    @classmethod
    def init(cls):
        pygame.init()
        cls.running = True
        cls.window = pygame.display.set_mode((Config.width, Config.height))

        pygame.display.set_caption(Lang.get_item("name"))

        cls.clock = pygame.time.Clock()

    @classmethod
    def update(cls):
        Keyboard.update()

        mouseup = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                MouseTracker.set_down(True)
                mouseup = True

            if not mouseup:
                MouseTracker.set_down(False)

            if event.type == pygame.MOUSEMOTION:
                MouseTracker.set_pos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        StateManager.get_state().update(cls.window)

        cls.clock.tick(60)

        pygame.display.flip()

    @staticmethod
    def end():
        pygame.quit()

    @classmethod
    def is_running(cls):
        return cls.running


class Driver:

    @staticmethod
    def run():
        Engine.init()
        StateManager.set_state(GameState(Engine.window))

        while Engine.is_running():
            Engine.update()

        Engine.end()


if __name__ == "__main__":
    Driver.run()
