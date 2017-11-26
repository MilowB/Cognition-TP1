class Interaction:
    def __init__(self, a, r, w):
        self.action = a
        self.result = r
        self.weight = w
        self.evaporation = 0.9
        self.nb = 1
        self.sum = 0
        self.proclivity = self.result * self.weight

    def maj(self, res): #Todo: is avg ok ?
        self.nb += 1
        self.sum += res

        self.weight += 1
        self.result = self.sum/self.nb
        self.proclivity = self.result * self.weight

    def evaporate(self):
        self.weight *= self.evaporation

    '''
    Objectif : Indique si une interaction est un sous ensemble de l'interaction passée en param
    Param : Interaction
    Retour : True si l'interaction est un sous ensemble de celle pasée en param, False sinon
    '''
    def is_subinteraction(self, interaction):
        if len(self.action) > len(interaction.action):
            return False
        ret = True
        for i in range(len(self.action)):
            if self.action[i] != interaction.action[i]:
                ret = False
        return ret

    '''
    Objectif : Fusionne deux interactions
    Param : Interaction à fusionner
    Retour : Interaction - Nouvelle interaction
    '''
    def merge(self, interaction):
        acts = []
        for a in self.action:
            acts.append(a)
        for a in interaction.action:
            acts.append(a)
        
        result = self.result + interaction.result
        weight = max(self.weight, interaction.weight)
        return Interaction(acts, result, weight)

    def size(self):
        return len(self.action)

    def __str__(self) -> str:
        return str(self.action) + " | " + str(self.result) + " | " + str(self.weight)