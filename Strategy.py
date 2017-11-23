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

class Strategy():
    def __init__(self, motivation):
        """
        @_motivation: concatenation of (action + result)
        but here we do not care about action, we only need the result to give a reward to the agent
        """
        self._motivation = motivation


    def get_reward(self, result, action):
        command = str(action) + str(result)
        return self._motivation[command]
