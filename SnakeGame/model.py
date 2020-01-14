import enum

class GameModel():

    DEFAULT_INIT_SNAKE_LEN = 3

    def __init__(self, gridSize):
        self.initSnakeLen = self.DEFAULT_INIT_SNAKE_LEN
        self.gridSize = gridSize

    def init(self):
        gridWidth = self.gridSize[0]
        snakeBody = []
        # we place the snake in the top left starting by the tail
        x = 0
        y = 0
        direction = Direction.Right
        for i in range(self.initSnakeLen):
            # if we reach the edge, we go one row down and start filling backwards
            coord = [x, y]
            snakeBody.append(coord)
            if x == 0:
                if direction == Direction.Left:
                    direction = Direction.Down
                else:
                    direction = Direction.Right
            elif x == gridWidth - 1:
                if direction == Direction.Right:
                    direction = Direction.Down
                else:
                    direction = Direction.Left
            if direction == Direction.Right:
                x += 1
            elif direction == Direction.Left:
                x -= 1
            else:
                y += 1
            # note that we do not handle the erroneous case of snake length being bigger than grid size
        snakeBody.reverse()
        self.snake = Snake(snakeBody, direction)

    def moveSnake(self, growSnake=False):
        '''Moves the snake in the Direction set in the object.
        If grow is True, the snake will grow by one block while moving.'''
        gridWidth = self.gridSize[0]
        gridLength = self.gridSize[1]
        # we only need to determine where the head goes next
        # and then all the other blocks switch places with their previousBlock each
        head = self.snake.body[0]
        previousBlock = head.copy()
        if self.snake.direction == Direction.Right:
            head[0] = (head[0] + 1) % gridWidth 
        elif self.snake.direction == Direction.Up:
            head[1] = head[1] - 1 if head[1] > 0 else gridLength - 1
        elif self.snake.direction == Direction.Left:
            head[0] = head[0] - 1 if head[0] > 0 else gridWidth - 1
        elif self.snake.direction == Direction.Down:
            head[1] = (head[1] + 1) % gridLength
        for i in range(1, len(self.snake)):
            self.snake.body[i], previousBlock = previousBlock, self.snake.body[i]
        # if snake is growing, then we add the last previousBlock as a new block
        if growSnake:
            self.snake.body.append(previousBlock)

    def generateGrid(self):
        '''Returns a grid of CellContent, that shows the position of everything on the grid.'''
        gridWidth = self.gridSize[0]
        gridLength = self.gridSize[1]
        grid = []
        for y in range(gridLength):
            grid.append(list())
            for x in range(gridWidth):
                coord = (x, y)
                if coord in self.snake:
                    if self.snake.isHead(coord):
                        # y first, x second
                        grid[y].append(CellContent.SnakeHead)
                    else:
                        grid[y].append(CellContent.SnakeBody)
                else: 
                    grid[y].append(CellContent.Empty)
        return grid

class Snake():
   
    def __init__(self, initialBody, initialDirection):
        '''Constructs Snake object with initialBody and initialDirection.
        initialBody is a list of coord lists.
        initialDirection is a value of the Enum Direction.'''
        # body has to be made up of lists
        self.body = initialBody
        self.direction = initialDirection

    def isHead(self, coord):
        return self.body[0] == list(coord)

    def __contains__(self, coord):
        if type(coord) in [list, tuple]:
            for part in self.body:
                if part == list(coord):
                    return True
        return False

    def __len__(self):
        '''Overrides len() so that calling len(snake) would return snake body length.'''
        return len(self.body)


class CellContent(enum.Enum):
    '''This enum is used to map the current state into a grid for GameController.'''
    Empty = 0
    SnakeHead = 1
    SnakeBody = 2
    Food = 3

class Direction(enum.Enum):
    Right = 0
    Up = 1
    Left = 2
    Down = 3

