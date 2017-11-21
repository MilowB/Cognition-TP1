import random

class SequenceModifier:
    def __init__(self, sequence):
        self._sequence = list(sequence)
        self.nb_actions = 3

    def _random_action(self):
        return random.randint(0, self.nb_actions)

    def random_modification(self):
        action = self._random_action()
        index = random.randint(0, len(self._sequence) - 1)
        action_to_change = random.randint(0, 1)
        action_to_change *= 2
        #Supprimer
        if action == 0:
            del self._sequence[index]
        #Modifier
        elif action == 1:
            self._sequence[index] = action_to_change
        #Ajouter
        elif action == 2:
            self._sequence.insert(index, action_to_change)
        return self._sequence