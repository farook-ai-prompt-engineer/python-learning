class Employee:

    def work(self):
        print("Employee Working")


class AIEngineer(Employee):

    def work(self):
        print("AI Engineer Working")


person = AIEngineer()

person.work()
