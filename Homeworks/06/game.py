from solution import *
from random import randint
import pygame
from pygame.locals import *


class PythonGame:
    CAPTION_TEXT = 'Pythons bite!'
    WORLD_WIDTH = 300
    SIZE = WORLD_WIDTH * 2, WORLD_WIDTH * 2
    BACKGROUND_COLOR = 154, 205, 50
    SNAKE_COLOR = 110, 139, 61
    FOOD_COLOR = 255, 0, 0
    running = True

    def play(self):
        pygame.init()
        world = World(self.WORLD_WIDTH)

        row, col = randint(0, self.WORLD_WIDTH), randint(0, self.WORLD_WIDTH)
        coords = Vec2D(row, col)
        py_size = randint(3, 5)
        python = Python(world, coords, py_size, Python.LEFT)

        food_cells = randint(5, 11)
        food = [Food(randint(1, 10)) for _ in range(food_cells)]

        screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(self.CAPTION_TEXT)

        # Event loop
        while PythonGame.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            # Fill background
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill(self.BACKGROUND_COLOR)

            # Display snake
            font = pygame.font.Font(None, 30)
            snake = '@@' + '##' * python.size
            text = font.render(snake, 1, self.SNAKE_COLOR)
            textpos = text.get_rect()
            textpos.centerx = python.coords.x * 2
            textpos.centery = python.coords.y * 2
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                python.move(Python.LEFT)
            if key[pygame.K_RIGHT]:
                python.move(Python.RIGHT)
            if key[pygame.K_UP]:
                python.move(Python.UP)
            if key[pygame.K_DOWN]:
                python.move(Python.DOWN)


PythonGame().play()
