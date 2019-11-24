import pygame
from model import GameModel
from view import GameView
from model import Direction
from agent import Agent
from tensorflow.python.keras.utils import to_categorical
import numpy as np
import time

class GameController(object):

    EVENTS = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
         

    def init_keyboard(self):
        self.view = GameView()
        self.model = GameModel()
        self.model.init()
        self.view.render(self.model.generateGrid())
        while not self.model.gameover: 
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:  
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key in self.EVENTS:
                        if event.key == pygame.K_w:
                            self.model.snake.direction = Direction.Up
                        elif event.key == pygame.K_s:
                            self.model.snake.direction = Direction.Down
                        elif event.key == pygame.K_a:
                            self.model.snake.direction = Direction.Left
                        elif event.key == pygame.K_d:
                            self.model.snake.direction = Direction.Right
                        self.model.moveSnake()
                        self.view.render(self.model.generateGrid())
                        if self.model.gameover:
                            break

    def init_network(self, visualization=False):

        counter = 0
        agent = Agent()
        
        while counter < 100:
            view = GameView()
            model = GameModel()
            model.init()
            view.render(model.generateGrid())

            while not model.gameover:

                prevState = agent.getState(model)
                prediction = agent.model.predict(prevState.reshape((1,12)))
                print(prediction)
                move = Direction(np.argmax(prediction[0]))
                print(move)
                model.snake.direction = move
                model.moveSnake()
                reward = agent.setReward(model)
                nextState = agent.getState(model)
                

                agent.save(prevState, move, nextState, reward, model.gameover)
                if visualization:
                    view.render(model.generateGrid())
                    time.sleep(1)
                    
            counter += 1

        model.save("model.h5")
                                             

        
            
        
        
                    
        
        
            

if __name__ == '__main__':
    x = GameController().init_network()
