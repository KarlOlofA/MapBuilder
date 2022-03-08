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
        self.save_color = self.settings.GREY
        self.save_rect = pygame.Rect((self.settings.grid_size[0]+5, 5, self.width - 10, 40))

        self.font = pygame.font.SysFont(None, 24)
        self.img = self.font.render("Export Data", True, self.settings.TURQUOISE)

        # Saving things
        self.file_handler = FileHandler()

        self.has_saved = False
        self.is_pressed = False
        self.exported = False

    def draw(self):

        pygame.draw.rect(self.screen, self.color, self.bg_rect)
        # Draw button + text
        pygame.draw.rect(self.screen, self.save_color, self.save_rect)
        self.screen.blit(self.img, (self.settings.grid_size[0]+50, 17))

    def button_clicked(self, nodes):

        self.save_color = self.settings.WHITE
        self.file_handler.export_grid(nodes)

    def button_not_clicked(self):

        self.save_color = self.settings.GREY

    def handle_interaction(self, pos, nodes):

        self.is_pressed = self.save_rect.collidepoint(pos)

        if self.is_pressed and not self.exported:
            self.button_clicked(nodes)
            self.exported = True
        elif self.is_pressed and self.exported:
            self.button_clicked(nodes)
        else:
            self.button_not_clicked()
            self.exported = False
