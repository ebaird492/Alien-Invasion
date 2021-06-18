import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    
    def run_game(self):
        """Start main game loop"""
        while True:
            # Check for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # filling screen
            self.screen.fill(self.settings.bg_color)

            # Display screen
            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance
    ai = AlienInvasion()
    ai.run_game()