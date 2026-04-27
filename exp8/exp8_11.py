class Father:
    def skills(self):
        print("Father: Coding, Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child : Gaming, Music")

c = Child()
c.skills()