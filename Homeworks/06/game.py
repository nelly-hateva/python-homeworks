from solution import *
from random import randint
import pygame
from pygame.locals import *


class PythonGame:
    CAPTION_TEXT = 'Pythons bite!'
    WORLD_WIDTH = 704
    SIZE = WORLD_WIDTH, WORLD_WIDTH
    BACKGROUND_COLOR = 154, 205, 50
    PYTHON_COLOR = 110, 139, 61
    APPLE_COLOR = 255, 0, 0
    running = True

    def __init__(self):
        self.world = World(self.WORLD_WIDTH)
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(self.CAPTION_TEXT)

    def play(self):
        while PythonGame.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            # Fill background
            background = pygame.Surface(self.screen.get_size())
            background = background.convert()
            background.fill(self.BACKGROUND_COLOR)

            self.draw_apple()
            self.draw_python()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                python.move(Python.LEFT)
            if key[pygame.K_RIGHT]:
                python.move(Python.RIGHT)
            if key[pygame.K_UP]:
                python.move(Python.UP)
            if key[pygame.K_DOWN]:
                python.move(Python.DOWN)

            pygame.display.flip()

    def draw_python(self):
        row, col = randint(0, self.WORLD_WIDTH), randint(0, self.WORLD_WIDTH)
        coords = Vec2D(row, col)
        python = Python(self.world, coords, 3, Python.LEFT)
        r, g, b = self.PYTHON_COLOR
        x, y = python.coords
        for ix in range(-5, 5):
            for iy in range(-5, 5):
                self.screen.set_at((x + ix, y + iy), (r, g, b))

    def draw_apple(self):
        r, g, b = self.APPLE_COLOR
        x, y = randint(0, self.WORLD_WIDTH), randint(0, self.WORLD_WIDTH)
        for ix in range(-5, 5):
            for iy in range(-5, 5):
                self.screen.set_at((x + ix, y + iy), (r, g, b))


PythonGame().play()
