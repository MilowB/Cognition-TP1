from Util import *
import random
from resAction import ResAction


class TotalRecall:
    def __init__(self, strategy, symb):
        self.strategy = strategy
        self.last_action = None
        self.last_reward = None
        self.todo = []
        self.symb = symb
        self.trace = ""
        self.ite = ""
        self.interaction = []
        self.actions = []
        self.babillage= True
        self.inter = None

    def chooseExperience(self, ite, ite_max):

        # babillage
        if len(self.actions) < 10:
            action = random.randint(0, 1)
            self.last_action = action
            return action
        elif True:
            pass
            # double Exploration
        elif True:
            pass

    def get_reward(self, result):
        if self.babillage:
            self.saveOrUpdate(self.last_action,result)
            self.last_reward = self.strategy.get_reward(result, self.last_action)
        else:
            self.last_reward = self.strategy.get_reward(result, self.last_action)
        return self.last_reward

    def memory(self):
        action = self.last_action
        reward = self.last_reward

        self.actions.append(ResAction(action, reward))

    def find_seq(self, vals):
        max = 0
        index = []
        for i in range(0, len(vals)):
            tempsum = vals[i]
            i += 1
            for y in range(i, len(vals)):
                tempsum += vals[y]
                if tempsum > max:
                    max = tempsum
                    index.clear()
                    index.append(i - 1)
                    index.append(y)
                else:
                    break
        result = []
        if len(vals) > 1 and len(index) == 2:
            for i in range(index[0], index[1]):
                result.append(self.actions[i])
        else:
            return []

        return result

    def saveOrUpdate(self, action, res):

        for i in range(0, len(self.interaction)):
            if self.interaction[i].action == action:
                break

        self.interaction[i].maj(action, sum(res))

    def show_trace(self):
        print(self.trace)
        print(self.ite)

    def tracer(self, reward, i):
        if reward > 0:
            mess = '\x1b[0;30;46m'
        else:
            mess = '\x1b[5;30;41m'
        space = ""

        for y in range(0, len(str(i))):
            space += " "

        self.trace += mess + str(self.symb[self.last_action]) + '\x1b[0m' + space
        self.ite += str(i) + " "
