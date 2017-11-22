import random
import math

class Actions():
    def __init__(self, actions = None):
        self._sequence = actions
        self.iterator = 0
        self.reward = 0
        self.weight_reward = 0
        self.trace = []

    def cumul_reward(self, value):
        self.trace.append(value)
        self.reward += value

    def random(self, size):
        self._sequence = []
        for i in range(size):
            rand = random.randint(0, 1)
            rand *= 2
            self._sequence.append(rand)
        return self

    '''
    Objectif : Recup la prochaine action de l'action de haut niveau
    Retour : None si on a déjà parcouru l'Action, Int sinon
    '''
    def next_action(self):
        ret = None
        if self.iterator < len(self._sequence):
            ret = self._sequence[self.iterator]
            self.iterator += 1
        if ret is None:
            print("Erreur : L'action est parcourue jusqu'au bout")
        return ret

    '''
    Objectif : Recup l'action courante
    Retour : None si on a déjà parcouru l'Action, Int sinon
    '''
    def current_action(self):
        ret = self._sequence[self.iterator - 1]
        return ret


    '''
    Retour : False si tous éléments ont été parcouru, True sinon
    '''
    def has_next(self):
        if self.iterator < len(self._sequence):
            return True
        return False

    '''
    Objectif : Recup la prochaine action de l'action de haut niveau
    Retour : None si on a déjà parcouru l'Action, Int sinon
    '''
    def reset_iterator(self):
        self.iterator = 0
        self.trace = []
        avg = 0.0
        for t in self.trace:
            avg += t
        self.reward = ((self.reward * self.weight_reward) + avg) / (self.weight_reward + 1)
        self.weight_reward += 1

    '''
    Objectif : Supprimer l'élément le plus mauvais de la séquence
    Retour : Nouvelle Action modifiée
    '''
    def remove_badest(self):
        if len(self._sequence) > 1:
            min = math.inf
            argmin = None
            for i in range(len(self.trace)):
                if self.trace[i] < min and self.trace[i] < -5:
                    min = self.trace[i]
                    argmin = i
            if argmin is None:
                return None
            print("suppression ", argmin, "ieme element") # @debug
            del self._sequence[argmin]

    '''
    Objectif : Modifier un élément aléatoirement de la séquence
    Retour : Nouvelle Action modifiée
    '''
    def random_modification(self):
        print("trace : ", self.trace)
        action = random.randint(0, 10)
        index = random.randint(0, len(self._sequence) - 1)
        action_to_change = random.randint(0, 1) * 2

        print("ajout ", action_to_change) # @debug
        self._sequence.append(action_to_change)
        
        return Actions(list(self._sequence))

    '''
    Objectif : Agrege deux Actions
    Retour : Nouvelle Action agregée
    '''
    def agregate(self, action):
        seq = []
        while self.has_next():
            seq.append(self.next_action())
        while other.has_next():
            seq.append(action.next_action())
        return Action(list(seq))

    '''Override equal'''
    def __eq__(self, other):
        while self.has_next():
            while other.has_next():
                if self.next_action != other.next_action:
                    return False
        return True

    '''Override to_string'''
    def __str__(self):
        return str(self._sequence)

    '''Override >='''
    def __ge__(self, other):
        if self.reward >= other.reward:
            return True
        return False

    '''Override >'''
    def __gt__(self, other):
        if self.reward > other.reward:
            return True
        return False

    '''Override <'''
    def __lt__(self, other):
        if self > other:
            return False
        return True

    '''Override <='''
    def __lt__(self, other):
        if self.reward <= other.reward:
            return True
        return False

    '''Override !='''
    def __ne__(self, other):
        if self == other:
            return False
        return True