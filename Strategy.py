"""
OLD made for first test

class Strategy():


    def __init__(self):
        self.motivation = {}
        self.motivation["01"] = -10
        self.motivation["21"] = -10
        self.motivation["02"] = 5
        self.motivation["22"] = 5
        self.lastAction = None
        
    def get_reward(self, action, result):
        if self.lastAction == action and result != 1:
            return -1
        command = str(action) + str(result)
        self.lastAction = action
        return self.motivation[command]

"""

#TODO: generic class

class Strategy():
    def __init__(self):
        """
        @motivation: concatenation of (result + action)
        """
        self.motivation = {}
        self.motivation["01"] = -1
        self.motivation["02"] = 1
        self.motivation["11"] = -1
        self.motivation["12"] = 1

    def get_reward(self, result, action):
        command = str(action) + str(result)
        return self.motivation[command]
