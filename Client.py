
class Client:
    def __init__(self, name, age, company, budget):
        self.name = name
        self.age = age
        self.company = company
        self.budget = budget

    def sign_contract(self):
        print(f"{self.name} from {self.company} signed a contract with a budget of {self.budget}.")

    def renew_contract(self):
        print(f"{self.name} from {self.company} renewed their contract.")

    def update_info(self, name=None, age=None, company=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if company:
            self.company = company
        print(f"Updated info: {self.name}, {self.age}, {self.company}")
