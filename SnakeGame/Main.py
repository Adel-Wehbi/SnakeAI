from GameModel import * 
import pprint

pp = pprint.PrettyPrinter(indent=4)

model = GameModel()
model.initialize()
pp.pprint(model.grid)
