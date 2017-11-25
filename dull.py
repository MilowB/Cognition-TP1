from Util import *
import random


def swap(action, nb):
    print(action)
    of = list(range(0, nb))
    of.remove(action)

    return random.choice(of)


class DullAgent:
    def __init__(self, strategy, symb):
        self.strategy = strategy
        self.last_action = None
        self.actions = []
        self.results=[]
        self.vals = []
        self.todo = []
        self.best_seq = []
        self.symb = symb
        self.motiv = 0
        self.nbacts = len(symb)
        self.trace = ""
        self.ite = ""

    def chooseExperience(self, ite, ite_max):

        if len(self.actions) == 0:
            self.last_action = random.randint(0, self.nbacts - 1)
            return self.last_action
        elif self.last_reward <0:
            self.last_action = swap(self.last_action, self.nbacts - 1)
            return self.last_action
        else:
            return self.last_action

    def get_reward(self, result):
        self.last_result = result
        self.last_reward = self.strategy.get_reward(result, self.last_action)
        self.motiv += self.last_reward
        return self.last_reward

    def memory(self):
        action = self.last_action
        reward = self.last_reward

        self.actions.append(action)
        self.vals.append(reward)
        self.results.append(self.last_result)

    ''' -------------------- Debug & Display --------------------'''

    def show_trace(self):
        print(self.trace)
        print(self.ite)

    def pres(self):
        print("Salut, ", end="")
        if len(self.todo) > 0:
            print("j'ai ", end="")
            print('\x1b[6;30;42m' + str(self.todo) + '\x1b[0m', end="")
            print("a faire.")
        print("Mon historique est de : " + str(self.actions))
        print("pour : " + str(self.vals))

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
