class Student:
    def __init__(self, name, major, gpa, age, isonProbation ):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.age = age
        self.isonProbation = isonProbation

    def on_honor_role (self):
        if self.gpa >= 3.5:
            return True
        else:
            return False