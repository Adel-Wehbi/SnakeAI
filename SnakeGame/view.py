import pygame
from model import CellContent
import enum

class GameView(object):

    grid = [
            [CellContent.SnakeBody, CellContent.SnakeBody, CellContent.SnakeBody, CellContent.SnakeBody],
            [CellContent.Empty, CellContent.SnakeBody, CellContent.Empty, CellContent.Empty],
            [CellContent.Empty, CellContent.Empty, CellContent.SnakeBody, CellContent.Empty],
            [CellContent.SnakeBody, CellContent.Empty, CellContent.Empty, CellContent.SnakeHead]
        ]
    
    BG_COLOR = green = 0, 135, 0
    SNAKE_COLOUR = 135, 0, 0

    def __init__(self, gridDimensions=(10, 10), gridSize=(540, 540)):
        self.width = gridDimensions[0]
        self.length = gridDimensions[1]
        self.gridSize=gridSize
        self.cellWidth = gridSize[0]/self.width
        self.cellLength = gridSize[1]/self.length

    def render(self, grid):
        self.screen = pygame.display.set_mode(self.gridSize)
        self.screen.fill(self.BG_COLOR)
        
        for i in range(self.length):
            for j in range(self.width):
                print(grid[i][j])
                if(grid[i][j] == CellContent.Empty):
                    print("BG")
                    pygame.draw.rect(self.screen, self.BG_COLOR, (self.getleftCoord(j), self.getTopCoord(i), self.cellWidth, self.cellLength))
                elif (grid[i][j] == CellContent.SnakeHead) or (grid[i][j] == CellContent.SnakeBody):
                    pygame.draw.rect(self.screen, self.SNAKE_COLOUR, (self.getleftCoord(j), self.getTopCoord(i), self.cellWidth, self.cellLength))
                    print("SNAKE")
                    
        pygame.display.flip()          
                
            
        
    def getleftCoord(self, x):
        return x * self.cellWidth

    def getTopCoord(self, y):
        return y * self.cellLength
        
if __name__ == '__main__':
    x = GameView((4,4))
    x.render(GameView.grid)
