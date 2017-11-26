from Util import *
import random
import time

class SmartAgent:
    def __init__(self, strategy, mem, symb):
        self.strategy = strategy
        self.last_action = None
        self.sum_rew = 1
        self.actions = []
        self.vals = []
        self.todo = []
        self.best_seq = []
        self.mem = mem
        self.symb = symb
        self.trace = ""
        self.ite = ""
        self.nb_actions = len(symb)

    def chooseExperience(self, ite, ite_max):
        if ite > ite_max - 50:
            time.sleep(0.2)
        if len(self.actions) < self.mem:
            action = random.randint(0, self.nb_actions - 1)
            self.last_action = action
            return action
        else:
            if len(self.todo) == 0:
                threshold = curiosity(ite, ite_max)
                epsilon = random.random()

                if epsilon < threshold:
                    action = random.randint(0, self.nb_actions - 1)
                    self.last_action = action
                    return action
                else:
                    self.todo = self.find_seq(self.vals)
                    if len(self.todo) == 0:
                        action = random.randint(0, self.nb_actions - 1)
                    else:
                        action = self.todo.pop(0)
                    self.last_action = action
                    return action
            else:
                action = self.todo.pop(0)
                self.last_action = action
                return action

    def get_reward(self, result):
        self.last_reward = self.strategy.get_reward(result, self.last_action)
        return self.last_reward

    def memory(self):
        action = self.last_action
        reward = self.last_reward

        self.actions.append(action)
        self.vals.append(reward)

        if len(self.actions) > self.mem:
            self.actions.pop(0)

        if len(self.vals) > self.mem:
            self.vals.pop(0)

    #Trouve la plus grande sequence positive
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
        if len(result) > len(self.best_seq) and sum(result) > sum(self.best_seq):
            self.best_seq = result[:]
        return result


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
