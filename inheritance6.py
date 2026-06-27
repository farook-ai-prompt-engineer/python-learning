class Employee:

    def __init__(self, name):
        self.name = name


class AIEngineer(Employee):

    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

    def show(self):
        print(self.name)
        print(self.skill)


person = AIEngineer("farook", "Python")

person.show()
