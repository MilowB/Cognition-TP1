from Util import *
import random

class Agent():

    def __init__(self, strategy):
        self.strategy = strategy
        self.last_action = None
        self.sum_rew = 1

        #Association meilleure action / meilleure recompense
        self.best_action = random.randint(0, 1)
        self.best_reward = -math.inf

    def chooseExperience(self, ite, ite_max):
        threshold = curiosity(ite, ite_max, self.sum_rew)
        epsilon = random.random()

        #print("threshold : " + str(threshold))
        #print("epsilon : " + str(epsilon))
        if epsilon < threshold:
            print("Ceci est une action aleatoire")
            action = random.randint(0, 1)
        else:
            action = self.best_action

        self.last_action = action
        return action


    def get_reward(self, result):
        reward = self.strategy.get_reward(self.last_action, result)
        print("reward  : " + str(reward)) # @debug
        if reward > self.best_reward:
            self.best_reward = reward
            self.best_action = self.last_action
