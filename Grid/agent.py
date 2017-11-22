from originator import *
from careTaker import *
from random import randint

class Agent:
    def __init__(self, name, begin, color):
        self._name = name
        self.num = id(self)
        self.begin = begin
        self.color = color
        self.originator = Originator()
        self.caretaker = CareTaker()
        self.position = None

    def setCurrentPosition(self, position):
        self.position = position

    def savePosition(self, square):
        self.originator.setState(square)
        self.caretaker.add(self.originator.saveStateToMemento())

    def goBack(self):
        self.originator.getStateFromMemento(self.caretaker.getLast())

    def getLastPosition(self):
        return self.caretaker.getLast().getState()

    def getCurrentPosition(self):
        return self.position
