import pygame
import sys

from settings import Settings
from node_structure import Node
from sidebar import Sidebar


class MapBuilder:

    def __init__(self):

        pygame.init()
        self.settings = Settings(self)
        # Quick Settings
        self.width = self.settings.grid_size[0]
        self.height = self.settings.grid_size[1]
        self.sidebar_width = self.settings.sidebar_size[0]

        self.screen = pygame.display.set_mode((self.width + self.sidebar_width, self.height))
        pygame.display.set_caption("Map Builder")

        self.sidebar = Sidebar(self.screen)

        # Grid
        self.total_rows = self.settings.total_rows
        self.nodes = self.make_grid()

        # Define base start and end nodes

        self.start_end = {
            "start": None,
            "end": None
        }

        self.run = True
        self.started = False

    def run_builder(self):
        while self.run:

            # Call Draw Functions
            self.draw()
            self.sidebar.draw()

            for event in pygame.event.get():  # Loop through events.

                if event.type is pygame.QUIT:
                    self.run = False

                if self.started:
                    continue

                self._check_events()  # Check for mouse input.

            pygame.display.flip()

        sys.exit()

    def _check_events(self):

        if pygame.mouse.get_pressed()[0]:  # Left, first click is assign start.

            pos = pygame.mouse.get_pos()

            if pos[0] >= self.width:

                # Sidebar interaction
                self.sidebar.handle_interaction(pos, self.nodes, self.start_end)

            elif pos[0] < self.width - 20 and pos[1] < self.height - 20:  # <--- This needs fixing but works for now.

                # Grid interaction
                row, col = self.get_clicked_pos(pos)

                node = self.nodes[row][col]

                if not self.start_end["start"] and not node.is_end():
                    self.start_end["start"] = node
                    self.start_end["start"].make_start()
                elif not self.start_end["end"] and not node.is_start():
                    self.start_end["end"] = node
                    self.start_end["end"].make_end()
                elif node is not self.start_end["end"] and node is not self.start_end["start"]:
                    node.make_room()

        elif pygame.mouse.get_pressed()[2]:  # Right, get node and reset it to white.

            pos = pygame.mouse.get_pos()
            if pos[0] < 800:

                row, col = self.get_clicked_pos(pos)
                node = self.nodes[row][col]

                if node is self.start:
                    self.start = None
                    node.reset()
                elif node is self.end:
                    self.end = None
                    node.reset()
                elif node.is_room():
                    node.reset()

    def make_grid(self):
        grid = []
        gap = self.width // self.total_rows
        for i in range(self.total_rows):
            grid.append([])
            for j in range(self.total_rows):
                node = Node(self.screen, i, j, gap)
                grid[i].append(node)
        return grid

    def draw_grid(self):
        gap = self.width // self.total_rows
        for i in range(self.total_rows):
            pygame.draw.line(self.screen, self.settings.GREY, (0, i * gap), (self.width, i * gap))
        for j in range(self.settings.total_rows):
            pygame.draw.line(self.screen, self.settings.GREY, (j * gap, 0), (j * gap, self.height))

    def draw(self):
        self.screen.fill(self.settings.WHITE)

        for row in self.nodes:
            for node in row:
                node.draw(self.screen)

        self.draw_grid()

    def get_clicked_pos(self, pos):
        gap = self.width // self.total_rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col


if __name__ == "__main__":
    mb = MapBuilder()
    mb.run_builder()
