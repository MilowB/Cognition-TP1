from Util import *
import math
import time
from interaction import Interaction
from colormap import *
from executer import *
import itertools
import random

def swap(action, nb):
    of = list(range(0, nb))
    of.remove(action)

    return random.choice(of)


'''
Résultat cohérent et correct pour tous les env présents excepté env1
'''
class CartesianAgent:
    def __init__(self, strategy, symb):
        self.strategy = strategy
        self._symb = symb
        self._memory = []
        self._interactions = []
        self._actions = self.allActions(len(self._symb))
        self._executer = None
        self._lastAction = None
        self._lastActs = None
        self._lastReward = None
        self.sumReward = 0
        self._bestAction = None
        self._epsilon = 1
        self._trace = []

    '''
    Objectif :  Choisi la prochaine action à faire
    Param : Int - itération en cours, Int - nb total d'itérations
    Retour : Int - action
    '''
    def chooseExperience(self, ite, ite_max):
        action = None
        
        
        #print(self._epsilon)
        if (self._executer is None or not self._executer.has_next()) and len(self._interactions) >= len(self._actions):
            r = random.random()
            acts = None
            
            if curiosity(ite, ite_max) - 0.05 > r:
                acts = self.heuristicRandom()
            else:
                acts = self.heuristicGreedy()
            if not acts is None:
                self._executer = Executer(acts.action)
                self._lastActs = acts
                self.find_combinaison(self._lastActs)
            self._epsilon = curiosity(ite, ite_max) #pas très efficace
        elif self._executer is None or not self._executer.has_next():
            acts = self.heuristicDiversification()
            if not acts is None:
                self._executer = Executer(acts.action)
                self._lastActs = acts
                self.find_combinaison(self._lastActs)
        if not self._executer is None and self._executer.has_next():
            action = self._executer.next_action()

        self._lastAction = action
        return action

    '''
    0bjectif : Rechercher une interaction s'enchainant bien avec l'interaction passée en param
    Param : Interacion
    Retour : Interacion - qui obtient une bonne proclivité enchainée avec l'interaction en param
    '''
    def find_combinaison(self, interaction):
        #Parcours de la mémoire pour rechercher les bonnes interactions
        for i in range(len(self._memory) - 1):
            if self._memory[i] == interaction and self._memory[i + 1].proclivity > 0 and interaction.proclivity > 0:
                if self._memory[i] != self._memory[i + 1]:
                    valence = max(self._memory[i].result, self._memory[i + 1].result)
                    self.addInteractions(interaction.merge(self._memory[i + 1]), valence, False)
                


    '''
    Objectif :  @debug
    '''
    def print_interactions(self, max = False):
        print("----------------------------------")
        for i in self._interactions:
            if max:
                if i.result > 0:
                    print(i)
            else:
                print(i)
        print("----------------------------------")

    '''
    Objectif :  Voir nom de méthode
    '''
    def apply_evaporation(self):
        for i in self._interactions:
            i.evaporate()

    '''
    Objectif :  Recevoir la récompense
    '''
    def get_reward(self, result):
        self._lastReward = self.strategy.get_reward(result, self._lastAction)
        #garde une trace des récompenses pour plotter le résultat
        self._trace.append(self._lastReward)
        self.sumReward += self._lastReward
        #Met à jour les valeurs de la dernière interaction faite si elle est finie
        if not self._executer.has_next():
            self._memory.append(self._lastActs)
            self.updateInteraction(self._lastActs, self.sumReward)
            #Si l'interaction était un bon enchainement avec l'autre les merge
            last_index = len(self._memory) - 1
            #if self._memory[last_index - 1].proclivity > 0:
            if self._memory[last_index].proclivity > 0 and self._memory[last_index - 1].proclivity > 0:
                if self._memory[last_index - 1] != self._memory[last_index]:
                    self.addInteractions(self._memory[last_index - 1].merge(self._memory[last_index]), self.sumReward, False)

                
            self.sumReward = 0

        return self._lastReward


    '''
    Objectif : Modifie la valence et le poids de l'interaction
    '''
    def updateInteraction(self, interaction, valence):
        interaction.maj(valence)
        self.apply_evaporation()


    '''
    Objectif : AJoute une interaction seulement si elle n'est pas deja présente
    Param : actions a ajouter, Bool - True si actions = [actions], False si actions = Interaction
    '''
    def addInteractions(self, actions, valence, type = True):
        if not type:
            if not self.exist_interaction(actions, type):
                self._interactions.append(actions)
        else:
            if not self.exist_interaction(actions, type):
                #Bootstrap de l'interaction avec des valeurs connues
                new_interaction = Interaction(actions, valence, 1)
                self._interactions.append(new_interaction)

    '''
    Objectif : Chercher une valence permettant de bootstrap l'interaction cible
    Param : Interaction que l'on veut bootstrap
    Retour : Int - valence, None si aucune sous chaine trouvée
    '''
    def bootstrap(self, interaction):
        #Le but est de recherche la plus grande sous chaine interactionnelle possible avec l'interaction
        #passée en param pour avoir un bootstrap plus précis
        lng_max = 0
        argmax = None
        for inter in self._interactions:
            if inter.is_subinteraction(interaction):
                lng = inter.size()
                if lng > lng_max:
                    lng_max = lng
                    argmax = inter
        if argmax is None:
            return None
        return argmax.result


    '''
    Objectif : Choisi les actions au hasard
    Retour : Interaction - aléatoire
    '''
    def heuristicMinWeight(self):
        min = math.inf
        argmin = None
        for interaction in self._interactions:
            val = interaction.weight
            if val < min:
                min = val
                argmin = interaction
        return argmin


    '''
    Objectif : Choisi les actions au hasard
    Retour : Interaction - aléatoire
    '''
    def heuristicRandom(self):
        inter = self._interactions[random.randint(0, len(self._interactions) - 1)]
        return inter

    '''
    Objectif : Choisi les actions au hasard
    Retour : Interaction - aléatoire
    '''
    def heuristicPseudoRandom(self):
        inter = self._interactions[random.randint(0, len(self._interactions) - 1)]
        while inter.proclivity > 0:
            inter = self._interactions[random.randint(0, len(self._interactions) - 1)]
        return inter


    '''
    Objectif : Choisi les actions les plus rentables
    Retour : Interaction - de la plus forte valence
    '''
    def heuristicGreedy(self):
        max = -math.inf
        argmax = None
        for interaction in self._interactions:
            val = interaction.proclivity
            if val > max:
                max = val
                argmax = interaction
        self._bestAction = argmax
        return argmax

    '''
    Objectif : Choisi les actions absentes d'interaction pour tester toutes les suites d'actions possible
    Retour : Booleen - True si action absente d'interaction, False sinon
    '''
    def heuristicDiversification(self):
        for actions in self._actions:
            if not self.exist_interaction(actions):
                inter = Interaction(actions, 0, 1)
                valence = self.bootstrap(inter)
                if not valence is None:
                    inter.result = valence
                self._interactions.append(inter)
                return inter
        return None

    '''
    Objectif : Indique si la liste d'actions existe dans une interaction
    Retour : Booleen - True si la liste d'actions est dans la liste d'interaction, False sinon
    '''
    def exist_interaction(self, actions, type = True):
        if not type:
            actions = actions.action
        found = False
        for interaction in self._interactions:
            if len(actions) == len(interaction.action):
                allOk = True
                for i in range(len(actions)):
                    if actions[i] != interaction.action[i]:
                        allOk = False
                        break
                if allOk:
                    found = True
                    break             
        return found
                
    '''
    Objectif : Genere un produit cartésien des données passées en param
    Retour : Tableau de tuples
    '''
    def cartesian(self, data, size):
        d = []
        for i in range(size):
            d.append(data)

        return set(itertools.product(*d))
        
    '''
    Objectif : Genere toutes les actions possibles en fonction des symboles dispo
    Retour : Tableau d'actions
    '''
    def allActions(self, size):
        actions = set()
        tutor = set()
        for i in range(len(self._symb)):
            tutor.add(i)
        for k in range(size + 1):
            for j in range(size):
                acts = self.cartesian(tutor, k)
                for act in acts:
                    actions.add(act)
        #Suppression tuple vide
        actions = [t for t in actions if t != ()]
        return actions

    '''
    Objectif : Genere la trace
    '''
    def generate_colormap(self):
        v_min = min(self._trace)
        v_max = max(self._trace)
        transformed = []
        for value in self._trace:
            new_value = rescale(value, v_min, v_max, [0, 1])
            transformed.append(new_value)

        colormap = ColorMap(self._trace)
        colormap.build()