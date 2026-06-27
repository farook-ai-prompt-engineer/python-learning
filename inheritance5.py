class Employee:


    def __init__(self,name):
        self.name=name



class AIEngineer(Employee):


    def work(self):
        print(self.name)


person = AIEngineer("farook")


person.work()

