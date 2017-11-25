class Executer():
    def __init__(self, interaction):
        self.iterator = 0
        self._interaction = interaction
    
        '''
    Objectif : Recup la prochaine action de l'action de haut niveau et incremente l'iterateur
    Retour : None si on a déjà parcouru l'Action, Int sinon
    '''
    def next_action(self):
        ret = None
        if self.iterator < len(self._interaction):
            ret = self._interaction[self.iterator]
            self.iterator += 1
        if ret is None:
            print("Erreur : L'action est parcourue jusqu'au bout")
        return ret

    '''
    Objectif : Recup l'action courante
    Retour : None si on a déjà parcouru l'Action, Int sinon
    '''
    def current_action(self):
        ret = self._interaction[self.iterator - 1]
        return ret


    '''
    Retour : False si tous éléments ont été parcouru, True sinon
    '''
    def has_next(self):
        if self.iterator < len(self._interaction):
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
