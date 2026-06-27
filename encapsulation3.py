class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        print(self.__salary)


person = Employee()

person.get_salary()
