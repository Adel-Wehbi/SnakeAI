import pygame
from model import GameModel
from view import GameView
from model import Direction
from agent import Agent
import numpy as np
import time
import random
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(format='[%(asctime)s] %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger('CONTROLLER')

class GameController(object):

    EVENTS = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]

    def init_keyboard(self):
        self.view = GameView(gridDimensions=(10,10))
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
                        
    def plot_seaborn(self, array_counter, array_score):
        sns.set(color_codes=True)
        ax = sns.regplot(np.array([array_counter])[0], np.array([array_score])[0], color="b", x_jitter=.1, line_kws={'color':'green'})
        ax.set(xlabel='games', ylabel='score')
        plt.show()

    def init_network(self, visualization=False):

        logger.setLevel(logging.INFO)

        counter = 0
        agent = Agent()

        game_scores = []
        game_counts = []

        logger.info("Training...")
        
        while counter < 150:

            logger.debug("//////////////Game: " + str(counter) +"//////////////")
            
            view = GameView(gridDimensions=(10,10))
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
                logging.debug("////////END TURN//////////")
                time.sleep(1)
            
            while not model.gameover:

                randomTurn = False

                prevState = agent.getState(model)

                agent.epsilon  = 80 - counter

                if random.randint(0, 200) < agent.epsilon:
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
                    logger.debug("////////END TURN//////////")
                    time.sleep(1)
                    
            logger.info("Game: " + str(counter) + " | Score: " + str(model.score))
            game_scores.append(model.score)
            game_counts.append(counter)
            counter += 1
            agent.batchTrain()
        logger.debug("Training Complete")
        self.plot_seaborn(game_counts, game_scores)
        agent.saveModel()
                                             

        
            
        
        
                    
        
        
            

if __name__ == '__main__':
    x = GameController().init_network()
