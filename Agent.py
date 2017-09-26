from Util import *
import random

class Agent():

    def __init__(self, strategy):
        self.strategy = strategy
        self.last_action = None
        self.sum_rew = 0

        #Association meilleure action / meilleure recompense
        self.best_action = random.randint(0, 1)
        self.best_reward = -math.inf

    def chooseExperience(self, r, ite, ite_max):
        action = None
        threshold = curiosity(ite, ite_max, sum_rew)
        epsilon = random.random()

        if epsilon < threshold:
            action = random.randint(0, 1)
        else:
            action = self.best_action

        self.last_action = action
        return action


    def get_reward(self, result):
        reward = self.strategy.get_reward(result)
        if reward > self.best_reward:
            self.best_reward = reward
            self.best_action = self.last_action
