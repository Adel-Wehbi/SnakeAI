import pygame
from model import CellContent
import enum

class GameView(object):
    
    BG_COLOR = green = 0, 135, 0
    SNAKE_COLOUR = 135, 0, 0
    FOOD_COLOUR = 255, 51, 0
    SNAKEHEAD_COLOR = 0, 0, 0 

    def __init__(self, gridDimensions=(10, 10), gridSize=(540, 540)):
        #Grid dimensions in number of cells
        self.width = gridDimensions[0]
        self.height = gridDimensions[1]
        #grid dimensions in pixels
        self.gridSize=gridSize
        #grid cell dimensions in pixels
        self.cellWidth = gridSize[0]/self.width
        self.cellHeight = gridSize[1]/self.height

    def render(self, grid):
        self.screen = pygame.display.set_mode(self.gridSize)
        self.screen.fill(self.BG_COLOR)
        
        for i in range(self.height):
            for j in range(self.width):
                if(grid[i][j] == CellContent.Empty):
                    pygame.draw.rect(self.screen, self.BG_COLOR, (self.getleftCoord(j,0), self.getTopCoord(i,0), self.cellWidth, self.cellHeight))
                elif (grid[i][j] == CellContent.SnakeBody):
                    pygame.draw.rect(self.screen, self.SNAKE_COLOUR, (self.getleftCoord(j, 0.05), self.getTopCoord(i, 0.05), self.cellWidth*0.9, self.cellHeight*0.9))
                elif (grid[i][j] == CellContent.SnakeHead):
                     pygame.draw.rect(self.screen, self.SNAKEHEAD_COLOR, (self.getleftCoord(j, 0.1), self.getTopCoord(i, 0.1), self.cellWidth*0.8, self.cellHeight*0.8))
                elif(grid[i][j] == CellContent.Food):
                    pygame.draw.ellipse(self.screen, self.FOOD_COLOUR, (self.getleftCoord(j, 0.25), self.getTopCoord(i, 0.25), (self.cellWidth)/2.0, (self.cellHeight)/2.0))
        pygame.display.flip()          
                
            
        
    def getleftCoord(self, x, offset):
        '''Computes the left side coordinate of a rectangle. Offset parameter will shift it
            to the right by a percentage of the cell width '''
        return x * self.cellWidth + (self.cellWidth*offset)

    def getTopCoord(self, y, offset):
        '''Computes the top side coordinate of a rectangle.
           Offset parameter will shift it down by a percentage of the cell cell height'''
        return y * self.cellHeight + (self.cellHeight*offset)
        
        
if __name__ == '__main__':
    x = GameView((8,8))
    x.render(GameView.grid)
