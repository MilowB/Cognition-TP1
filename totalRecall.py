from Util import *
import random
import math
import time
from resAction import ResAction
from interaction import Interaction


def swap(action, nb):
    of = list(range(0, nb))
    of.remove(action)

    return random.choice(of)


class TotalRecall:
    def __init__(self, strategy, symb):
        self.strategy = strategy
        self.last_action = None
        self.last_reward = None
        self.todo = []
        self.symb = symb
        self.trace = ""
        self.ite = ""
        self.interactions = []
        self.actions = []
        self.babillage = True
        self.inter = None
        self.nbacts = len(symb)
        self.motiv = 0
        self.last = False

    # TODO : More exploration ( other than merge)
    # TODO : find seq ?

    def chooseExperience(self, ite, ite_max):  # TODO : Greatter babillage
        if ite > ite_max - 50:
            time.sleep(0.2)
        # TODO : USE MORE MEMORY
        # babillage
        if len(self.actions) < 40:
            action = random.randint(0, self.nbacts - 1)
            self.last_action = action
            self.inter = Interaction([action], 0, 1)  # TODO : Update if exist
            return action

        else:
            if len(self.todo) == 0:
                threshold = curiosity(ite, ite_max, 1)
                epsilon = random.random()

                if epsilon < threshold:
                    self.whats_next()
                    self.last_action = self.todo.pop(0)
                    # print("DO -----> ",self.last_action)
                    return self.last_action
                else:
                    self.inter = self.purge()
                    self.todo = self.inter.action[:]
                    self.last_action = self.todo.pop(0)
                    # print("PURGE ----> ",self.last_action)
                    return self.last_action
                    # TODO: Increase positivity
            else:
                if len(self.todo) == 1:
                    self.last = True
                self.last_action = self.todo.pop(0)
                # print("TODO ------> ",self.last_action)
                return self.last_action

    def get_reward(self, result):

        self.last_reward = self.strategy.get_reward(result, self.last_action)

        if self.last:

            self.saveOrUpdate(self.inter.action, self.itwas())
            self.last = False
        else:
            self.saveOrUpdate(self.inter.action, self.last_reward)
        self.motiv += self.last_reward
        return self.last_reward

    def memory(self):
        action = self.last_action
        reward = self.last_reward

        self.actions.append(ResAction(action, reward))

    def saveOrUpdate(self, action, res):

        update = False
        for i in range(0, len(self.interactions)):
            if self.interactions[i].action == action:
                self.interactions[i].maj(res)
                update = True
        if not update:
            self.interactions.append(Interaction(action, res, 1))  # TODO : Put inter sum

    def whats_next(self):

        worth = []
        worth.append(self.merge())

        for i in range(0, len(self.interactions)):
            if self.interactions[i].action[0] == self.last_action:
                worth.append(self.interactions[i])

        if random.randint(0, self.nbacts - 1) == 0:
            good = worth[random.randint(0, len(worth)-1)]
        else:
            good = self.max_inter(worth)

        if (len(good.action) > 1):
            self.todo = good.action[1:]
        else:
            # good.action.append(self.last_action)
            self.todo = good.action[:]
        self.inter = good

    def merge(self):  # TODO: FUSION NOT APPEND ?

        r1 = self.interactions[random.randint(0, len(self.interactions) - 1)]
        r2 = self.interactions[random.randint(0, len(self.interactions) - 1)]

        inter = Interaction(r1.action + r2.action, r1.result + r2.result, 1)
        return inter

    def show_inter(self):

        for i in range(0, len(self.interactions)):
            print(self.interactions[i])

    def max_inter(self, inters):
        max = -math.inf
        index = 0

        for i in range(0, len(inters)):
            if int(inters[i].result) * int(inters[i].weight) > float(max):
                max = float(inters[i].result) * float(inters[i].weight)
                index = i
        return inters[index]

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

    def purge(self):  # TODO : Better heuristic
        topur = self.max_inter(self.interactions)
        acts = topur.action[:]

        # Random Purge

        #
        # for i in range(0, int(len(acts) * 0.4)):
        #     index = random.randint(0, len(acts) - 1)
        #     temp = acts[index]
        #     new = random.randint(0, self.nbacts - 1)
        #     if not new == temp:
        #         acts[index] = new
        #     else:
        #         while new == temp:
        #             new = random.randint(0, self.nbacts - 1)
        #         acts[index] = new


        for i in self.subfinder(acts):
            acts[i] = swap(acts[i], self.nbacts)

        return Interaction(acts, 1, 1)

    # GET Last inter result
    def itwas(self):
        total = 0
        for x in self.actions[max(1, len(self.actions) - len(self.inter.action)):]:
            total += x.getResult()
        return total

    def subfinder(self, pattern):
        todo = self.actions[:]
        temp = []
        for i in range(0, len(todo)):
            temp.append(todo[i].getAction())

        nb = 0
        pos = []
        for i in range(0, len(temp)):
            if temp[i] == pattern[0] and temp[i:i + len(pattern)] == pattern:
                pos.append(i)
            nb += 1
        if len(pos) > 0:
            return self.swap_finder(pos, len(pattern))
            # return self.actions[pos[0]:pos[0] + len(pattern)]

        return []

    def swap_finder(self, pos, nb):  # TODO : Not only neg but also low res

        index = []
        result = [0] * (nb - 1)
        for i in range(0, len(pos)):

            for y in range(0, nb - 1):
                result[y] += self.actions[pos[i] + y].getResult()

        for w in range(0, len(result)):
            result[w] = result[w] / nb

            if result[w] < 0:
                index.append(w)

        return index
