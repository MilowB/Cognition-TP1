class Env_Dif():
    def __init__(self):
        self.last = None

    #Retourne le resultat de l'expe
    def getResult(self, action):

        if action == self.last:
            self.last = action
            return "1"
        else:
            self.last = action
            return "2"
