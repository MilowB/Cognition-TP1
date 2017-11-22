import collections
import numpy as np

class Reader:
    def __init__(self):
        self.action_n = 4
        self.config = {
            "init_mean" : 0.0,      # Initialize Q values with this mean
            "init_std" : 0.0,       # Initialize Q values with this standard deviation
            "learning_rate" : 0.05,
            "eps": 0.00,            # Epsilon in epsilon greedy policies
            "discount": 0.90,
            "n_iter": 5000
        }

        self.qtable = None
        self.rewtable = None


    '''
    Objectif : lit un fichier de qtable
    Param : String - nom du fichier a lire
    Return : Qtable prete a etre utilisee
    '''
    def read(self, name):
        self.qtable = (collections.defaultdict(lambda: self.config["init_std"] * np.random.randn(self.action_n) + self.config["init_mean"]))
        self.rewtable = (collections.defaultdict(lambda: self.config["init_std"] * np.random.randn(1) + self.config["init_mean"]))
        file = open(name, "r")

        lines = file.readlines()

        for line in lines:
            arr = line.split()
            num = arr[0]
            cpt = -1
            for val in arr:
                if cpt >= 0:
                    if cpt == 4:
                        self.rewtable[str(num)] = val
                    else:
                        self.qtable[str(num)][cpt] = val
                cpt += 1
        
        file.close()
        return self.qtable, self.rewtable