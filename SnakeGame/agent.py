import tensorflow as tf
import tensorflow.keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
from operator import add
from model import Direction
import numpy as np
import random
import time
import logging

logging.basicConfig(format='[%(asctime)s] %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger('AGENT')

class Agent():
    
    def __init__(self):
        logger.setLevel(logging.INFO)
        self.reward = 0
        self.learningRate = 0.1 # how much we accept old vs new value
        self.gamma = 0.8 # discount factor
        self.epsilon = 100 # for exploring vs exploiting
        try:
            logger.debug("Loading model from file")
            self.model = load_model("model.h5")
        except:
            logger.debug("No file found, generating new model")
            self.model = self.model()
        self.memory = []

    def model(self):
        model = Sequential()
        model.add(Dense(units=120, activation='relu', input_dim=12))
        model.add(Dropout(0.15))
        model.add(Dense(units=4, activation='softmax'))
        opt = Adam(self.learningRate)
        model.compile(loss='mse', optimizer=opt)
        return model

    def setReward(self, game):
        if game.gameover:
            self.reward = -10
        elif game.growSnake:
            self.reward = 10
        else:
            self.reward = 0
        return self.reward

    def getState(self, game):
        
        state = [
            1 if list(map(add, game.pos, (1, 0))) in game.snake else 0, #danger right
            1 if list(map(add, game.pos, (-1, 0))) in game.snake else 0, # danger left
            1 if list(map(add, game.pos, (0, 1))) in game.snake else 0, # danger down
            1 if list(map(add, game.pos, (0, -1))) in game.snake else 0, # danger up
            1 if game.snake.direction == Direction.Right else 0,
            1 if game.snake.direction == Direction.Left else 0,
            1 if game.snake.direction == Direction.Up else 0,
            1 if game.snake.direction == Direction.Down else 0,
            1 if game.food[0] < game.pos[0] else 0, #food left
            1 if game.food[0] > game.pos[0] else 0, #food right
            1 if game.food[1] < game.pos[1] else 0, #food up
            1 if game.food[1] > game.pos[1] else 0, #food down
        ]

        return  np.asarray(state)

    def save(self, prevState, nextState, action, reward):
        self.memory.append((prevState, nextState, action, reward))

    def get_Q(self, state):
        return self.model.predict(state.reshape((1,12)))

    def batchTrain(self):
        if len(self.memory) > 1000:
            batch = random.sample(self.memory, 1000)
        else:
            batch = self.memory
        for prevState, nextState, action, reward in batch:
            oldStateQValues = self.get_Q(prevState)
            newStateQValues = self.get_Q(nextState)
            oldStateQValues[0][action] = reward + self.gamma * np.amax(newStateQValues)
            self.model.fit(np.array([prevState]), np.array(oldStateQValues), epochs=1, verbose=0)

    def trainShortTerm(self, prevState, nextState, action, reward):
        oldStateQValues = self.get_Q(prevState)
        newStateQValues = self.get_Q(nextState)
        logger.debug(f"old state Q values: {oldStateQValues}")
        logger.debug(f"new state Q values: {newStateQValues}")
        logger.debug(f"action: {action}")
        oldStateQValues[0][action] = reward + self.gamma * np.amax(newStateQValues)
        logger.debug(f"updated Q values: {oldStateQValues}")
        self.model.fit(np.array([prevState]), np.array(oldStateQValues), epochs=1, verbose=0)

    def saveModel(self):
        self.model.save("model.h5")

    
            
                
        
        
        
        

    
        
        
