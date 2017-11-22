from map import *
from gui import *

class Grid:
    def __init__(self, g, m, a, d, name):
        self.display = d
        self._name = name
        self.action_space = 2
        self.gui = g
        self.map = m
        self.debug = False
        self.agents = a

    '''
    Objectif : Fait executer a l'agent une action
    Param : agent - l'agent qui execute une, action - action que l'agent doit executer
    Retour : résultat du mouvement de l'agent (1 si mur, 2 sinon)
    '''
    def step(self, agent, action):
        #Mise a jour de la pile de cases parcourues
        squareTmp = self.map.agentNumSquare(agent)
        agent.savePosition(squareTmp)
        square = self.map.moveAgent(agent, action)
        #Mise a jour de la position courante
        agent.setCurrentPosition(square)

        if self.display:
            self.gui.update(self.map)
            self.gui.display()

        result = None
        if self._name == "env1":
            result = self.result_for_env1(square, squareTmp, agent)
        else:
            result = self.result_generic_env(square, squareTmp, agent)
        return result
    
    def disableDisplay(self):
        self.display = False

    def enableDisplay(self):
        self.display = True

    '''
    Objectif : @debug
    '''
    def printQvalues(self, qtable):
        self.map.printQvalues(qtable)

    '''
    Objectif : @debug
    '''
    def countAgents(self):
        return self.map.countAgents()

    '''
    Objectif : @debug
    '''
    def squarePosition(self, numSquare):
        return self.map.squarePosition(numSquare)


    '''
    Objectif : indique le bon retour de l'environnement
    '''
    def result_generic_env(self, square, old_square, agent):
        #Si l'agent n'a pas bougé alors il a rencontré un mur
        if square.equal(old_square):
            return 1
        return 2


    '''
    Objectif : indique le bon retour de l'environnement spécifiquement par rapport à l'env1
    qui a des règles un peu particulières sur l'alternance e1 / e2
    '''
    def result_for_env1(self, square, old_square, agent):
        #Regle de l'environnement : alternance e1 / e2 pour retour r2
        #La case objectif bouge pour de manière à faire apprendre à l'agent cette alternance
        if not square.equal(old_square) and self.map.isOnObjective(agent):
            self.map.moveObjOnEmptySquare()
        elif square.equal(old_square) and self.map.isOnObjective(agent):
            pass
        elif square.equal(old_square):
            self.map.moveObjOnEmptySquare()

        #Si l'agent n'a pas bougé alors il a rencontré un mur
        if square.equal(old_square):
            return 1
        return 2