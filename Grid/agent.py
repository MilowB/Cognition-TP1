import os, sys, pygame
from originator import *
from careTaker import *
from orientation import *
from random import randint

class Agent:
    def __init__(self, name, begin, color):
        self._name = name
        self.orientation = Orientation.NORTH
        self.num = id(self)
        self.begin = begin
        self.color = color
        self.originator = Originator()
        self.caretaker = CareTaker()
        self.position = None
        self.turtle = pygame.image.load(os.path.join('Images', 'turtle_small.png'))
        self.angle = 0

    def setCurrentPosition(self, position):
        self.position = position

    def savePosition(self, square):
        self.originator.setState(square)
        self.caretaker.add(self.originator.saveStateToMemento())

    def turn(self, orientation):
        diff = abs(self.orientation.value - orientation)
        if diff < 2 or diff == 3:
            self.orientation = Orientation(orientation)

    def goBack(self):
        self.originator.getStateFromMemento(self.caretaker.getLast())

    def getLastPosition(self):
        return self.caretaker.getLast().getState()

    def getCurrentPosition(self):
        return self.position

    def draw(self, screen, xy):
        cste_angle = 90
        new_angle = cste_angle * self.orientation.value
        self.turtle = pygame.transform.rotate(self.turtle, new_angle - self.angle)
        self.angle = new_angle
        screen.blit(self.turtle, xy)