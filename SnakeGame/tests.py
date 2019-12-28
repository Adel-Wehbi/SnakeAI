from unittest import TestCase, main
from unittest.mock import MagicMock, patch
from model import *
from view import GameView


@patch('model.Snake')
class GameModelTest(TestCase):
    
    def setUp(self):
        self.model = GameModel()
        self.model.gridSize = (4, 4)
        self.model.initSnakeLen = 3
        
    def test_init_defaultValues(self, MockSnake):
        self.model.init()
        expectedBody = [[2,0], [1,0], [0,0]] 
        expectedDirection = Direction.Right
        MockSnake.assert_called_once_with(expectedBody, expectedDirection)

    def test_init_snakeEqualToRow(self, MockSnake):
        self.model.initSnakeLen = 4
        self.model.init()
        expectedBody = [
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0]
        ]
        expectedDirection = Direction.Down
        MockSnake.assert_called_once_with(expectedBody, expectedDirection)

    def test_init_snakeBiggerThanRowByOne(self, MockSnake):
        self.model.initSnakeLen = 5
        self.model.init()
        expectedBody = [
            [3, 1],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0]
        ]
        expectedDirection = Direction.Left
        MockSnake.assert_called_once_with(expectedBody, expectedDirection) 

    def test_init_snakeBiggerThanRow(self, MockSnake):
        self.model.initSnakeLen = 6
        self.model.init()
        expectedBody = [
            [2, 1],
            [3, 1],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0]
        ]
        expectedDirection = Direction.Left
        MockSnake.assert_called_once_with(expectedBody, expectedDirection)

    def test_init_snakeEqualToTwoRows(self, MockSnake):
        self.model.initSnakeLen = 8
        self.model.init()
        expectedBody = [
            [0, 1],
            [1, 1],
            [2, 1],
            [3, 1],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0]
        ] 
        expectedDirection = Direction.Down
        MockSnake.assert_called_once_with(expectedBody, expectedDirection)

    def test_init_snakeBiggerThanTwoRowsByOne(self, MockSnake):
        self.model.initSnakeLen = 9
        self.model.init()
        expectedBody = [
            [0, 2],
            [0, 1],
            [1, 1],
            [2, 1],
            [3, 1],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0]
        ]  
        expectedDirection = Direction.Right
        MockSnake.assert_called_once_with(expectedBody, expectedDirection)

    def test_moveSnakeUpwards(self, MockSnake):
        body = [
            [1, 2],
            [0, 2],
            [0, 1],
            [0, 0]
        ]
        direction = Direction.Up
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [1, 1],
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeRightwards(self, MockSnake):
        body = [
            [1, 2],
            [0, 2],
            [0, 1],
            [0, 0]
        ]
        direction = Direction.Right
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [2, 2],
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeDownwards(self, MockSnake):
        body = [
            [1, 2],
            [0, 2],
            [0, 1],
            [0, 0]
        ]
        direction = Direction.Down
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [1, 3],
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeLeftwards(self, MockSnake):
        body = [
            [1, 3],
            [1, 2],
            [0, 2],
            [0, 1],
            [0, 0]
        ]
        direction = Direction.Left
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [0, 3],
            [1, 3],
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeOverRightBorder(self, MockSnake):
        body = [
            [3, 2],
            [2, 2],
            [2, 1],
            [2, 0],
        ]
        direction = Direction.Right
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [0, 2],
            [3, 2],
            [2, 2],
            [2, 1],
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeOverTopBorder(self, MockSnake):
        body = [
            [2, 0],
            [1, 0],
            [1, 1],
            [1, 2]
        ]
        direction = Direction.Up
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [2, 3],
            [2, 0],
            [1, 0],
            [1, 1],
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeOverLeftBorder(self, MockSnake):
        body = [
            [0, 2],
            [0, 1],
            [0, 0],
            [1, 0],
        ]
        direction = Direction.Left
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [3, 2],
            [0, 2],
            [0, 1],
            [0, 0],
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnakeOverBottomBorder(self, MockSnake):
        body = [
            [2, 3],
            [1, 3],
            [1, 2],
            [1, 1],
        ]
        direction = Direction.Down
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake()
        expectedBody = [
            [2, 0],
            [2, 3],
            [1, 3],
            [1, 2],
        ]
        self.assertEqual(expectedBody, body)

    def test_moveSnake_withGrow(self, MockSnake):
        body = [
            [1, 3],
            [1, 2],
            [0, 2],
            [0, 1],
        ]
        direction = Direction.Left
        mockSnake = MagicMock()
        mockSnake.body = body
        mockSnake.__len__.return_value = len(body)
        mockSnake.direction = direction
        self.model.snake = mockSnake
        self.model.moveSnake(True)
        expectedBody = [
            [0, 3],
            [1, 3],
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertEqual(expectedBody, body)

    def test_generateGrid(self, MockSnake):
        body = [
            [3, 3],
            [3, 0],
            [0, 0],
            [0, 3],
            [1, 3]
        ]
        def contains(coord):
            return list(coord) in body
        def isHead(coord):
            return list(coord) == body[0]
        snake = MagicMock()
        snake.body = body
        snake.isHead.side_effect = isHead
        snake.__contains__.side_effect = contains
        snake.__len__.return_value = len(body)
        self.model.snake = snake
        expectedGrid = [
            [CellContent.SnakeBody, CellContent.Empty, CellContent.Empty, CellContent.SnakeBody],
            [CellContent.Empty, CellContent.Empty, CellContent.Empty, CellContent.Empty],
            [CellContent.Empty, CellContent.Empty, CellContent.Empty, CellContent.Empty],
            [CellContent.SnakeBody, CellContent.SnakeBody, CellContent.Empty, CellContent.SnakeHead]
        ]
        self.assertEqual(expectedGrid, self.model.generateGrid())


class SnakeModelTest(TestCase):

    def setUp(self):
        body = [ [1, 1], [0, 1], [0, 0] ]
        self.snake = Snake(body, Direction.Right)

    def test_isHead_true(self):
        coord = (1, 1)
        self.assertTrue(self.snake.isHead(coord))

    def test_isHead_false(self):
        coord = (0, 0)
        self.assertFalse(self.snake.isHead(coord))

    def test_isHead_invalid(self):
        coord = 3
        with self.assertRaises(TypeError):
            self.snake.isHead(coord)

    def test_contains_true(self):
        coord = (0, 1)
        self.assertTrue(coord in self.snake)

    def test_contains_false(self):
        coord = (3, 6)
        self.assertFalse(coord in self.snake)

    def test_contians_invalid(self):
        coord = 3
        self.assertFalse(coord in self.snake)

class GameViewtest(TestCase):

    def setUp(self):
        self.grid = [
            [CellContent.SnakeBody, CellContent.SnakeBody, CellContent.SnakeBody, CellContent.SnakeBody],
            [CellContent.Empty, CellContent.SnakeBody, CellContent.Empty, CellContent.Empty],
            [CellContent.Empty, CellContent.Empty, CellContent.SnakeBody, CellContent.Empty],
            [CellContent.SnakeBody, CellContent.Empty, CellContent.Empty, CellContent.SnakeHead]
        ]

    def test_viewIsRenderedWithoutException(self):
        try:
            view = GameView(gridDimensions=(4,4))
            view.render(self.grid)
        except:
            self.fail("Instantiating view and rendering grid raised an exception")
    


if __name__ == '__main__':
    main()
