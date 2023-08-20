"""
With a class you can essentially design your own datatype
because the data types in python can cover everything
eg (Humans,phones e.t.c)
So a class is just like an overview of what a student datatype is
And an object is the actual student
"""
class Student:

    #the init is basically defining what a student should have
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

