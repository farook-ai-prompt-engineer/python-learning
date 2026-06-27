class AIModel:

    def __init__(self, accuracy):
        self.accuracy = accuracy

    def deploy(self):
        if self.accuracy >= 90:
            print("Deploy Model")
        else:
            print("Improve Model")


model = AIModel(85)

model.deploy()
