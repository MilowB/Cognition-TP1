class Interaction:
    def __init__(self, a, r, w):
        self.action = a
        self.result = r
        self.weight = w
        self.evaporation = 0.95

    def maj(self, res):
        if res < self.result:
            self.weight -= 1
        else:
            self.weight += 1
        self.weight *= self.evaporation
