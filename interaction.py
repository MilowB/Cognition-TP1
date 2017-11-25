class Interaction:
    def __init__(self, a, r, w):
        self.action = a
        self.result = r
        self.weight = w
        self.evaporation = 0.90
        self.nb = 1
        self.sum = 0

    def maj(self, res):
        self.nb += 1
        self.sum += res

        self.weight += 1
        self.weight *= self.evaporation
        self.result = self.sum/self.nb

    def __str__(self) -> str:
        return str(self.action) + " | " + str(self.result) + " | " + str(self.weight)
