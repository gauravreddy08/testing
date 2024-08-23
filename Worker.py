
class Worker:
    def __init__(self, name, age, company, department, hourly_rate):
        self.name = name
        self.age = age
        self.company = company
        self.department = department
        self.hourly_rate = hourly_rate

    def clock_in(self):
        print(f"{self.name} clocked in at {self.company}'s {self.department} department.")

    def clock_out(self):
        print(f"{self.name} clocked out from {self.company}'s {self.department} department.")

    def update_info(self, name=None, age=None, company=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if company:
            self.company = company
        print(f"Updated info: {self.name}, {self.age}, {self.company}")

