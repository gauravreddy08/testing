
class Employee:
    def __init__(self, name, age, company, position, salary):
        self.name = name
        self.age = age
        self.company = company
        self.position = position
        self.salary = salary

    def promote(self):
        print(f"Promoting {self.name} to a higher position in {self.company}.")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} received a raise of {amount}.")

    def update_info(self, name=None, age=None, company=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if company:
            self.company = company
        print(f"Updated info: {self.name}, {self.age}, {self.company}")
