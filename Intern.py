
class Intern:
    def __init__(self, name, age, company, school, duration):
        self.name = name
        self.age = age
        self.company = company
        self.school = school
        self.duration = duration

    def work_on_project(self):
        print(f"Intern {self.name} from {self.school} is working on a project at {self.company}.")

    def attend_meeting(self):
        print(f"Intern {self.name} is attending a meeting at {self.company}.")

    def update_info(self, name=None, age=None, company=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if company:
            self.company = company
        print(f"Updated info: {self.name}, {self.age}, {self.company}")
