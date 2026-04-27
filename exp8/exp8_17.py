class Department:
    def __init__(self, name):
        self.name      = name
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show(self):
        print(f"Department: {self.name}")
        for e in self.employees:
            print(f"  - {e.name} (Rs.{e.salary})")

class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

dept = Department("Engineering")
dept.add_employee(Employee("Raj", 80000))
dept.add_employee(Employee("Priya", 90000))
dept.show()