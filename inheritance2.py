class Employee:

    def work(self):
        print("Employee Working")


class AIEngineer(Employee):

    def deploy(self):
        print("Deploy Model")


person = AIEngineer()

person.work()
person.deploy()
