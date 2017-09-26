class Strategy():

    def __init__(self):
        self.motivation = {}
        self.motivation["01"] = 1
        self.motivation["02"] = 1
        self.motivation["11"] = -1
        self.motivation["12"] = -1
        
    def get_reward(self, action, result):
        command = str(action) + str(result)
        return self.motivation[command]
