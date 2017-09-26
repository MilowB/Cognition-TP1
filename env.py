class Env():
    def __init__(self, action2result):
        self.action2result = action2result

    def getResult(self, action):
        return self.action2result[str(action)]
