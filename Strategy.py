class Strategy():

    def __init__(self):
        self.motivation = {}
        self.motivation["11"] = 1
        self.motivation["12"] = 1
        self.motivation["21"] = -1
        self.motivation["22"] = -1
        
    def get_reward(self, action, result):
        command = str(action) + string(result)
        return self.motivation[command]
