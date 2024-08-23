
class Executive:
    def __init__(self, name, age, company, division, bonus):
        self.name = name
        self.age = age
        self.company = company
        self.division = division
        self.bonus = bonus

    def make_decision(self):
        print(f"Executive {self.name} from {self.company} is making a decision for the {self.division} division.")

    def hold_meeting(self):
        print(f"Executive {self.name} is holding a meeting at {self.company}.")

    def update_info(self, name=None, age=None, company=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if company:
            self.company = company
        print(f"Updated info: {self.name}, {self.age}, {self.company}")
