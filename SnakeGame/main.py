from GameModel import * 
from GameView import *
import pprint

pp = pprint.PrettyPrinter(indent=4)

# just trying out

model = GameModel()
model.init()
pp.pprint(model.grid)

view = GameView()
view.init()
input()
