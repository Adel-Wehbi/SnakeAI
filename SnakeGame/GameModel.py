import enum

class GameModel(object):

    class CellContent(enum.Enum):
        Empty = 0
        SnakeHead = 1
        SnakeBody = 2

    DEFAULT_GRID_SIZE = width, length = 10, 10
    DEFAULT_INIT_SNAKE_LEN = 3

    def __init__(self):
        self.gridSize = self.DEFAULT_GRID_SIZE
        self.initSnakeLen = self.DEFAULT_INIT_SNAKE_LEN

    def init(self):
        # start with an empty grid
        self.grid = [list([self.CellContent.Empty] * self.gridSize[0]) for x in range(self.gridSize[1])]
        coord = [0,0]
        for i in range(self.initSnakeLen - 1):
            self.grid[coord[0]][coord[1]] = self.CellContent.SnakeBody
            # lay out the snake horizontally at the top left
            coord[1] += 1
        self.grid[coord[0]][coord[1]] = self.CellContent.SnakeHead
