class Employee:


    def __init__(self, name):
        self.name = name



class AIEngineer(Employee):


    def __init__(self, name, project):
        super().__init__(name)
        self.project = project


    def deploy(self):
        print(self.name)
        print(self.project)




engineer = AIEngineer(
        "farook",
        "AI Monitoring"
    )


engineer.deploy()

