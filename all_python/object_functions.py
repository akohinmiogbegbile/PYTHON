""" class functions are essentially a function that we can use inside of a class and it can either
    modify the objects of the class or give specific informations about the object
"""
from Student import Student
student1 = Student("Inmi", "Computer Science", 3.9 , 16 , False)
student2 = Student("John", "Law", 3.3 , 18 , True)


print(student1.on_honor_role())
print(student2.on_honor_role())