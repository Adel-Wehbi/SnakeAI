import pygame
from model import GameModel
from view import GameView
from model import Direction

class GameController(object):

    EVENTS = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]

    def __init__(self):
        self.view = GameView()
        self.model = GameModel()
        self.model.init()
        self.view.render(self.model.generateGrid())
        while 1: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key in self.EVENTS:
                        if event.key == pygame.K_w:
                            self.model.snake.direction = Direction.Up
                        elif event.key == pygame.K_s:
                            self.model.snake.direction = Direction.Down
                        elif event.key == pygame.K_a:
                            self.model.snake.direction = Direction.Left
                        elif event.key == pygame.K_d:
                            self.model.snake.direction = Direction.Right
                        

                        self.model.moveSnake()
                        self.view.render(self.model.generateGrid())
            

if __name__ == '__main__':
    x = GameController()
