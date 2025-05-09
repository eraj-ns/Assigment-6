class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          
        self._salary = salary     
        self.__ssn = ssn


emp = Employee("Eraj", 50000, "123-45-6789")

print("Name (Public):", emp.name)

print("Salary (Protected):", emp._salary)

try:
    print("SSN (Private):", emp.__ssn)
except AttributeError as e:
    print("Cannot access __ssn directly:", e)

print("SSN (Accessed via name mangling):", emp._Employee__ssn)
