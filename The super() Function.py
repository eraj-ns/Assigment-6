class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

teacher1 = Teacher("Miss Sara", "Mathematics")
teacher1.display_info()
