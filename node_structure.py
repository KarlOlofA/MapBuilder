import pygame
from settings import Settings

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:

    def __init__(self, mb, row, col, width):

        self.color = WHITE
        self.screen = mb
        self.settings = Settings(self.screen)

        # Sizes
        self.x = row * width
        self.y = col * width

        self.row = row
        self.col = col

        self.width = self.settings.grid_size[0]
        self.height = self.settings.grid_size[1]

        # Nodes & Neighbours
        self.neighbours = []

    def get_pos(self):
        return self.row, self.col

    # Check Functions
    def is_closed(self):
        return self.color is RED

    def is_open(self):
        return self.color is GREEN

    def is_room(self):
        return self.color is BLACK

    def is_start(self):
        return self.color is GREEN

    def is_end(self):
        return self.color is RED

    def reset(self):
        self.color = WHITE

    # Make Functions
    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_room(self):
        self.color = BLACK

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED

    # Other
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update_neighbours(self, grid):
        pass

    def __lt__(self, other):
        return False
