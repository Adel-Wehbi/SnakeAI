from model import GameModel
from view import GameView

import time

class GameController():

    DEFAULT_GRID_SIZE = (10, 10)
    DEFAULT_WINDOW_SIZE = (540, 540)

    def __init__(self, tick=None, grid=None, window=None, view=True):
        '''Creates the GameController object.
        The tick variable is in seconds.
        If no tick is passed, controller will tick the game when requested.
        If no grid is passed, default grid size will be used.
        If no window [size] is passed, default window size will be used.
        If view is set to False, the view will not be instantiated.'''
        self.tick = tick
        grid = grid if grid else self.DEFAULT_GRID_SIZE
        window = window if window else self.DEFAULT_WINDOW_SIZE
        self.model = GameModel(grid)
        # create the initial state of the game
        self.model.init()
        if view:
            self.view = GameView(grid, window)
            # render the initial state
            self.view.render(self.model.generateGrid())

    def start(self):
        '''Starts the game.
        Starts updating the state automatically if a tick value has been provided.'''
        if self.tick:
            while True:
                # will have to look into multi-threading here
                pass

    def update(self):
        '''Updates the game state and re-renders the view.
        Checks for win/lose conditions.'''
        self.model.update()
        self.view.render(self.model.generateGrid())
