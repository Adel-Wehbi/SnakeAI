import pygame
from model import CellContent
import enum

class GameView(object):

    grid = [
            [CellContent.SnakeBody, CellContent.Food, CellContent.Food, CellContent.SnakeBody],
            [CellContent.Food, CellContent.SnakeBody, CellContent.Empty, CellContent.Empty],
            [CellContent.Empty, CellContent.Food, CellContent.SnakeBody, CellContent.Empty],
            [CellContent.SnakeBody, CellContent.Food, CellContent.Food, CellContent.SnakeHead]
        ]
    
    BG_COLOR = green = 0, 135, 0
    SNAKE_COLOUR = 135, 0, 0
    FOOD_COLOUR = 255, 51, 0
    SNAKEHEAD_COLOR = 0, 0, 0 

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
                if(grid[i][j] == CellContent.Empty):
                    pygame.draw.rect(self.screen, self.BG_COLOR, (self.getleftCoord(j), self.getTopCoord(i), self.cellWidth, self.cellLength))
                elif (grid[i][j] == CellContent.SnakeBody):
                    pygame.draw.rect(self.screen, self.SNAKE_COLOUR, (self.getleftCoord(j)  + (self.cellWidth*0.05), self.getTopCoord(i) + (self.cellLength*0.05), self.cellWidth*0.9, self.cellLength*0.9))
                elif (grid[i][j] == CellContent.SnakeHead):
                     pygame.draw.rect(self.screen, self.SNAKEHEAD_COLOR, (self.getleftCoord(j)  + (self.cellWidth*0.1), self.getTopCoord(i) + (self.cellLength*0.1), self.cellWidth*0.8, self.cellLength*0.8))
                elif(grid[i][j] == CellContent.Food):
                    center = self.getCenterCoord(j, i)
                    pygame.draw.ellipse(self.screen, self.FOOD_COLOUR, (self.getleftCoord(j) + (self.cellWidth*0.25), self.getTopCoord(i) + (self.cellLength*0.25), (self.cellWidth)/2.0, (self.cellLength)/2.0))
        pygame.display.flip()          
                
            
        
    def getleftCoord(self, x):
        return x * self.cellWidth

    def getTopCoord(self, y):
        return y * self.cellLength

    def getCenterCoord(self, x, y):
        return float(x * self.cellWidth + (self.cellWidth / 2.0)), float(y * self.cellLength + (self.cellLength / 2.0))
        
        
if __name__ == '__main__':
    x = GameView((4,4))
    x.render(GameView.grid)
