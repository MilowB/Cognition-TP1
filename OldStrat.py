class OldStrategy():
    def __init__(self):
        self.motivation = {}
        self.motivation["10"] = 1
        self.motivation["20"] = -1
        self.motivation["11"] = 1
        self.motivation["21"] = -1

    def get_reward(self, action, result):

        command = str(action) + str(result)
        self.lastAction = action
        return self.motivation[command]