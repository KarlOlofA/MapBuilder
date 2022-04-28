import pygame
from settings import Settings
from file_handler import FileHandler


class Sidebar:

    def __init__(self, mb):
        self.screen = mb
        self.settings = Settings(self.screen)

        # Get sidebar sizes
        self.width = self.settings.sidebar_size[0]
        self.height = self.settings.sidebar_size[1]

        # Background
        self.color = self.settings.BLACK
        self.bg_rect = pygame.Rect((self.settings.grid_size[0], 0, self.width, self.height))

        # Buttons
        self.export_color = self.settings.GREY
        self.export_rect = pygame.Rect((self.settings.grid_size[0] + 5, 5, self.width - 10, 40))

        self.export_font = pygame.font.SysFont(None, 24)
        self.export_img = self.export_font.render("Export Data", True, self.settings.TURQUOISE)

        # Reset Button
        self.reset_color = self.settings.GREY
        self.reset_rect = pygame.Rect((self.settings.grid_size[0]+5, 55, self.width - 10, 40))

        self.reset_font = pygame.font.SysFont(None, 24)
        self.reset_img = self.reset_font.render("Reset Table", True, self.settings.TURQUOISE)

        # Saving things
        self.file_handler = FileHandler()

        self.has_saved = False
        self.export_is_pressed = False
        self.exported = False

        self.reset_is_pressed = False

    def draw(self):

        pygame.draw.rect(self.screen, self.color, self.bg_rect)
        # Draw button + Text
        pygame.draw.rect(self.screen, self.export_color, self.export_rect)
        self.screen.blit(self.export_img, (self.settings.grid_size[0]+50, 17))

        # Reset Button + Text
        pygame.draw.rect(self.screen, self.reset_color, self.reset_rect)
        self.screen.blit(self.reset_img, (self.settings.grid_size[0]+50, 68))

    def export_clicked(self, nodes):

        self.export_color = self.settings.WHITE
        self.file_handler.export_grid(nodes)

    def export_not_clicked(self):

        self.export_color = self.settings.GREY

    def handle_interaction(self, pos, nodes, start_end):

        self.export_is_pressed = self.export_rect.collidepoint(pos)
        self.reset_is_pressed = self.reset_rect.collidepoint(pos)

        # Export Data
        if self.export_is_pressed and not self.exported:
            self.export_clicked(nodes)
            self.exported = True
        elif self.export_is_pressed and self.exported:
            self.export_clicked(nodes)
        else:
            self.export_not_clicked()
            self.exported = False

        # Reset All Nodes
        if self.reset_is_pressed:
            start_end["start"] = None
            start_end["end"] = None
            for row in nodes:
                for node in row:
                    node.reset()


