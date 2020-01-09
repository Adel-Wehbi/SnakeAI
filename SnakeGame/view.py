import pygame
from model import CellContent
import enum

class GameView(object):
    
    BG_COLOR = green = 0, 135, 0
    SNAKE_COLOUR = 135, 0, 0
    FOOD_COLOUR = 255, 51, 0
    SNAKEHEAD_COLOR = 0, 0, 0
    SNAKEHEAD_OFFSET = 0.1
    SNAKEBODY_OFFSET = 0.05
    FOOD_OFFSET = 0.25

    def __init__(self, gridDimensions, windowSize=(540, 540)):
        #Grid dimensions in number of cells
        self.width = gridDimensions[0]
        self.height = gridDimensions[1]
        #grid dimensions in pixels
        self.windowSize=windowSize
        #grid cell dimensions in pixels
        self.cellWidth = windowSize[0]/self.width
        self.cellHeight = windowSize[1]/self.height

    def render(self, grid):
        self.screen = pygame.display.set_mode(self.windowSize)
        self.screen.fill(self.BG_COLOR)
        
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == CellContent.SnakeBody:
                    pygame.draw.rect(self.screen, self.SNAKE_COLOUR, (self.getleftCoord(j, self.SNAKEBODY_OFFSET), self.getTopCoord(i, self.SNAKEBODY_OFFSET), self.cellWidth*(1 - 2.0*self.SNAKEBODY_OFFSET), self.cellHeight*(1 - 2.0*self.SNAKEBODY_OFFSET)))
                elif grid[i][j] == CellContent.SnakeHead:
                     pygame.draw.rect(self.screen, self.SNAKEHEAD_COLOR, (self.getleftCoord(j, self.SNAKEHEAD_OFFSET), self.getTopCoord(i, self.SNAKEHEAD_OFFSET), self.cellWidth*(1 - 2.0*self.SNAKEHEAD_OFFSET), self.cellHeight*(1 - 2.0*self.SNAKEHEAD_OFFSET)))
                elif grid[i][j] == CellContent.Food:
                    pygame.draw.ellipse(self.screen, self.FOOD_COLOUR, (self.getleftCoord(j, self.FOOD_OFFSET), self.getTopCoord(i, self.FOOD_OFFSET), (self.cellWidth)/2.0, (self.cellHeight)/2.0))
        pygame.display.flip()          
                
            
        
    def getleftCoord(self, x, offset):
        '''Computes the left side coordinate of a rectangle. Offset parameter will shift it
            to the right by a percentage of the cell width '''
        return x * self.cellWidth + (self.cellWidth*offset)

    def getTopCoord(self, y, offset):
        '''Computes the top side coordinate of a rectangle.
           Offset parameter will shift it down by a percentage of the cell height'''
        return y * self.cellHeight + (self.cellHeight*offset)
        
