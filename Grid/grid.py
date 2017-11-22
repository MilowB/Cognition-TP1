from map import *
from gui import *

class Grid:
    def __init__(self, g, m, a, d):
        self.display = d
        self._name = "Grid"
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

        #Regle de l'environnement : alternance e1 / e2 pour retour r2
        #La case objectif bouge pour de manière à faire apprendre à l'agent cette alternance
        if not square.equal(squareTmp) and self.map.isOnObjective(agent):
            self.map.moveObjOnEmptySquare()            
        elif square.equal(squareTmp) and self.map.isOnObjective(agent):
            pass
        elif square.equal(squareTmp):
            self.map.moveObjOnEmptySquare()

        if self.display:
            self.gui.update(self.map)
            self.gui.display()

        #Si l'agent n'a pas bougé alors il a rencontré un mur
        if square.equal(squareTmp):
            return 1
        return 2
    
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