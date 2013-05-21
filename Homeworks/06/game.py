from solution import *
from random import randint
import pygame
from pygame.locals import *


class PythonGame:
    CAPTION_TEXT = 'Pythons bite!'
    BOARD_WIDTH = 704  # 11 * 64
    SIZE = BOARD_WIDTH, BOARD_WIDTH
    WORLD_WIDTH = 64
    BACKGROUND_COLOR = 0, 0, 0
    running = True

    def __init__(self):
        # Initialize the world and the python
        self.world = World(self.WORLD_WIDTH)
        start_coords = Vec2D(4, 4)
        self.python = Python(self.world, start_coords, 4, Python.DOWN)
        self.trail_x = []
        self.trail_y = []

        # Initialize the game
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(self.CAPTION_TEXT)
        self.clock = pygame.time.Clock()

    def play(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(self.BACKGROUND_COLOR)
        self.draw_apple()
        self.draw_python()
        pygame.display.flip()

        while PythonGame.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    PythonGame.running = False

            key = pygame.key.get_pressed()
            try:
                if key[pygame.K_LEFT]:
                    self.unknow_function(Python.LEFT)
                if key[pygame.K_RIGHT]:
                    self.unknow_function(Python.RIGHT)
                if key[pygame.K_UP]:
                    self.unknow_function(Python.UP)
                if key[pygame.K_DOWN]:
                    self.unknow_function(Python.DOWN)

            except (Death, ValueError):

                font = pygame.font.Font(None, 50)
                game_over = font.render("Game Over", 1, (238, 99, 99))
                self.screen.blit(game_over, (300, 300))
                pygame.display.flip()
                self.clock.tick(20)
                return  # or reset game

    def draw_python(self):
        for part_num in range(self.python.size + 1):
            x, y = self.python.coords - self.python.direction * part_num
            if self.python.direction in (Python.RIGHT, Python.LEFT):
                x += 11 * part_num
            else:
                y+= 11 * part_num
            print(x, y)
            self.trail_x.insert(0, x)
            self.trail_y.insert(0, y)
            r, g, b = randint(100, 200), randint(100, 200), randint(100, 200)
            for ix in range(-5, 5):
                for iy in range(-5, 5):
                    self.screen.set_at((x + ix, y + iy), (r, g, b))

    def draw_apple(self):
        #r, g, b = randint(150, 230), randint(150, 230), randint(150, 230)
        r, g, b = 255, 0, 0
        x, y = randint(0, self.WORLD_WIDTH), randint(0, self.WORLD_WIDTH)
        print("apple at", x , y)
        for ix in range(-5, 5):
            for iy in range(-5, 5):
                self.screen.set_at((x + ix, y + iy), (r, g, b))

    def draw_trail(self):
        r, g, b = 0, 0, 0
        x, y = self.trail_x.pop(), self.trail_y.pop()
        print("trail at", x, y)
        for ix in range(-5, 5):
            for iy in range(-5, 5):
                self.screen.set_at((x + ix, y + iy), (r, g, b))

    def unknow_function(self, direction):
        self.python.move(direction)
        self.draw_trail()
        pygame.display.flip()
        self.draw_python()

PythonGame().play()
