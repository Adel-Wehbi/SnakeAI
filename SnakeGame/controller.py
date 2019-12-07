import pygame
from model import GameModel
from view import GameView
from model import Direction
from agent import Agent
import numpy as np
import time
import random

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
        agent = Agent(logging=False)

        print("Training...")
        
        while counter < 1000:

            print("//////////////Game: " + str(counter) +"//////////////")
            
            view = GameView()
            model = GameModel()
            model.init()
            
            if visualization:
                view.render(model.generateGrid())
                time.sleep(1)

            action = 0
            prevState = agent.getState(model)
            model.moveSnake()
            nextState = agent.getState(model)
            reward = agent.setReward(model)
            agent.save(prevState, nextState, action, reward)
            agent.trainShortTerm(prevState, nextState, action, reward)

            if visualization:
                view.render(model.generateGrid())
                print("////////END TURN//////////")
                time.sleep(1)
            
            while not model.gameover:

                randomTurn = False

                
                prevState = agent.getState(model)

                if random.randint(0, 200) <= (agent.epsilon - counter/2):
                    action = random.randint(0, 3)
                    randomTurn = True
                else:
                    prediction = agent.model.predict(prevState.reshape((1,12)))
                    action = np.argmax(prediction[0])
                move = Direction(action)
                model.snake.direction = move
                model.moveSnake()
                reward = agent.setReward(model)
                nextState = agent.getState(model)
                agent.save(prevState, nextState, action, reward)
                agent.trainShortTerm(prevState, nextState, action, reward)
                
                if visualization:
                    view.render(model.generateGrid())
                    print("Prediction: " + str((prediction if not randomTurn else "Random Move")))
                    print("Move: " + str(move))
                    print("Action: " + str(action))
                    print("////////END TURN//////////")
                    time.sleep(1)
                    
                    
            
            print("Game: " + str(counter) + " | Score: " + str(model.score))
            counter += 1

        agent.batchTrain()
        print("Training Complete")
        agent.saveModel()
                                             

        
            
        
        
                    
        
        
            

if __name__ == '__main__':
    x = GameController().init_network(True)
