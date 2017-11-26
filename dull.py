from Util import *
import random
from interaction import Interaction


def swap(action, nb):
    of = list(range(0, nb))
    if action in of:
        of.remove(action)

    return random.choice(of)


class DullAgent:
    def __init__(self, strategy, symb):
        self.strategy = strategy
        self.last_action = None
        self.actions = []
        self.inters = []
        self.iter = None
        self.results = []
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

        elif self.last_reward < 0:

            if len(self.todo) == 0:
                if self.iter is not None:
                    self.iter.maj(sum(self.vals[len(self.vals) - len(self.iter.action):]))
                if random.randint(0, 25) > 1:
                    self.todo = self.what_happend()

                    if len(self.todo) == 0:
                        print("--------- RAND ---------------")
                        self.last_action = swap(self.last_action, self.nbacts - 1)
                else:
                    print("--------- RAND Explo ---------------")
                    print(self.last_action)
                    seqs = [random.randrange(0, self.nbacts, 1) for _ in range(random.randint(1,self.nbacts-1*2))]
                    temp = self.testint(seqs)

                    if temp is None:

                        self.iter = Interaction(seqs[:], 0, 1)
                        self.inters.append(self.iter)

                    else:
                        self.iter = temp
                    self.todo = self.iter.action[:]
                    self.last_action = self.todo.pop(0)
            else:
                self.last_action = self.todo.pop(0)
            return self.last_action

        elif len(self.todo) > 0:
            self.last_action = self.todo.pop(0)
            return self.last_action
        else:
            if self.iter is not None:
                self.iter.maj(sum(self.vals[len(self.vals) - len(self.iter.action):]))
            return self.last_action

    def get_reward(self, result):
        self.last_result = result
        self.last_reward = self.strategy.get_reward(result, self.last_action)
        self.motiv += self.last_reward
        self.ev()
        return self.last_reward

    def memory(self):
        action = self.last_action
        reward = self.last_reward

        self.actions.append(action)
        self.vals.append(reward)
        self.results.append(self.last_result)

    def what_happend(self):
        nb = len(self.symb)
        seqs = []
        vas = -math.inf

        if len(self.actions) > 2 * nb + 1:
            lasts = self.actions[len(self.actions) - nb + 1:]
            inds = self.subfinder(lasts)

            for i in inds:
                found = False
                temp = []
                tempi = 0
                y = 0

                while len(self.actions) - 3 > i + nb + y and (y == nb or self.vals[i + nb + y - 1] < 0):
                    temp.append(self.actions[i + nb + y])
                    potit = self.testint(seqs)

                    if potit is None:
                        tempi += self.vals[i + nb + y] -(0.5 * len(seqs))
                    else:
                        tempi += potit.proclivity -(0.5 * len(seqs))
                    y += 1

                    if self.vals[i + nb + y - 1] > 0:
                        found = True


                        # = pour prendre la dernière -> plus de chance d'être mieux
                if found:
                    if tempi >= vas and tempi > -100:
                        seqs = temp[:]
                        vas = tempi

            if len(seqs) > 0:
                temp = self.testint(seqs)

                if temp is None:

                    self.iter = Interaction(seqs[:], 0, 1)
                    self.inters.append(self.iter)

                else:
                    self.iter = temp

            elif random.randint(0, 1) == 0:

                seqs = [random.randrange(0, self.nbacts, 1) for _ in range(random.randint(1,self.nbacts-1*2))]
                temp = self.testint(seqs)

                if temp is None:

                    self.iter = Interaction(seqs[:], vas, 1)
                    self.inters.append(self.iter)

                else:
                    self.iter = temp

        return seqs

    ''' Test if int exist in mem'''

    def testint(self, acts):

        for i in range(0, len(self.inters) - 1):

            if self.inters[i].action == acts:
                return self.inters[i]
        return None

    def subfinder(self, pattern):
        todo = self.actions[:]
        nb = 0
        pos = []
        for i in range(0, len(todo)):
            if todo[i] == pattern[0] and todo[i:i + len(pattern)] == pattern:
                pos.append(i)
            nb += 1
        if len(pos) > 1:
            return pos[:-1]
        else:
            return []

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

    '''
    Objectif :  @debug
    '''

    def print_interactions(self, max=False):
        print("----------------------------------")
        for i in self.inters:
            if max:
                if i.result > 0:
                    print(i)
            else:
                print(i)
        print("----------------------------------")

    def ev(self):

        for it in self.inters:
            it.evaporate()
