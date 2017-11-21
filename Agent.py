import random
import math
from Util import *
from sequence import *
from Actions import *
 
class AgentDev():
    def __init__(self, strategy):
        self.historic = []
        self.sequence = None
        self.ObjectSequence = None
        self.strategy = strategy
        self.last_actions = None
        self.best_actions = Actions().random(1)
        self.in_test = None
        self.best_reward = -math.inf
        self.sum_rew = 0

        #mode
        self.greedy = True

    def chooseExperience(self, result, ite, ite_max):
        threshold = curiosity(ite, ite_max, self.sum_rew)
        epsilon = random.random()

        action = None
        if epsilon < threshold:
            action = Actions().random(1)
        else:
            if not self.in_test is None and not self.in_test.has_next():
                if self.in_test > self.best_actions:
                    print(self.best_actions.reward, " < ", self.in_test.reward)
                    self.best_actions = self.in_test
                    self.best_actions.reset_iterator()
                    self.greedy = False
                else:
                    self.greedy = True
            if not self.best_actions.has_next():
                self.in_test = self.best_actions.random_modification()
                self.best_actions.reset_iterator()
            todo = self.best_actions
            if not self.greedy:
                todo = self.in_test
            action = todo

        self.last_actions = action
        
        ret = action.next_action()
        return ret

    def get_reward(self, result):
        reward = self.strategy.get_reward(self.last_actions.current_action(), result)
        self.sum_rew += reward
        self.historic.append([self.last_actions, reward])

        self.last_actions.cumul_reward(reward)
        print("self.best_actions : ", self.best_actions, ", reward : ", self.best_actions.reward)


        if not self.last_actions is None and not self.last_actions.has_next():
            self.last_actions.remove_badest()

        if reward > self.best_reward:
            self.best_actions = self.last_actions
            self.best_reward = reward

