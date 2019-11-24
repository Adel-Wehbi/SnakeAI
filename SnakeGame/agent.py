import tensorflow as tf
import tensorflow.keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.optimizers import Adam
import numpy as np
from operator import add
from model import Direction
import numpy as np
import random

class Agent():
    
    def __init__(self):
        self.reward = 0
        self.learningRate = 0.1 # how much we accept old vs new value
        self.gamma = 0.8 # discount factor
        self.epsilon = 0 # for exploring vs exploiting
        self.model = self.model()
        self.memory = []
        

    def model(self):
        model = Sequential()
        model.add(Dense(units=120, activation="relu", input_dim=12))
        model.add(Dense(units=4, activation='softmax'))
        opt = Adam(self.learningRate)
        model.compile(loss='mse', optimizer=opt)
        return model

    def setReward(self, game):
        if game.gameover:
            selfreward = -10
        elif game.growSnake:
            self.reward = 10
        else:
            self.reward = 0
        return self.reward

    def getState(self, game):
        
        state = [
            1 if list(map(add, game.pos, (1, 0))) in game.snake else 0,
            1 if list(map(add, game.pos, (-1, 0))) in game.snake else 0,
            1 if list(map(add, game.pos, (0, 1))) in game.snake else 0,
            1 if list(map(add, game.pos, (0, -1))) in game.snake else 0,
            1 if game.snake.direction == Direction.Right else 0,
            1 if game.snake.direction == Direction.Left else 0,
            1 if game.snake.direction == Direction.Up else 0,
            1 if game.snake.direction == Direction.Down else 0,
            1 if game.food[0] < game.pos[0] else 0, #food left
            1 if game.food[0] > game.pos[0] else 0, #food right
            1 if game.food[1] < game.pos[1] else 0, #food down
            1 if game.food[1] < game.pos[1] else 0, #food up
            
        ]
        return  np.asarray(state)

    def save(self, state, action, nextState, reward, terminal):
        self.memory.append((state, action, nextState, reward, terminal))

    def batchTrain(self):
        if len(memory) > 100:
            batch = random.sample(self.memory, 1000)
        else:
            batch = self.memory
        for state, action, nextState, reward, terminal in batch:
            action_arr = np.zeros(4)
            action_arr[action] = 1
            target = reward
            if not terminal:
                target = reward + self.gamma * np.amax(self.model.predict(nextState.reshape((1,12)))[0])
            target_fit = self.model.fit(np.array([state]), target_fit, epochs=1, verbose=0)
            target_fit[0][np.argmax(action_arr)] = taget
            self.model.fit(np.array([state]), target_fit, epochs=1, verbose=0)
        
            
                
        
        
        
        

    
        
        
