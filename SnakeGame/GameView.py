import pygame

class GameView(object):
    
    DEFAULT_SIZE = width, length = 540, 540
    BG_COLOR = green = 0, 135, 0

    def __init__(self):
        self.size = self.DEFAULT_SIZE

    def init(self):
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.BG_COLOR)
        pygame.display.flip()
