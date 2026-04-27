class Employee:
    company_name = "TechCorp"   # class variable (shared)

    def __init__(self, name, salary):
        self.name = name        # instance variable (unique)
        self.salary = salary

e1 = Employee("Bob", 50000)
e2 = Employee("Carol", 60000)

print(Employee.company_name)   # TechCorp
print(e1.name, e1.salary)      # Bob 50000
print(e2.name, e2.salary)      # Carol 60000

Employee.company_name = "NewCorp"
print(e1.company_name)         # NewCorp (class var updated)