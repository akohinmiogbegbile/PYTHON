"""
r - reading a file
w - writing to files (Overwrites existing files, can also be used to create new files)
a - appending to files
"""
employee_file = open("employees1.txt", "a")
employee_file.write("\nElvis - Customer assistant")
employee_file.write("Yakub' - Accountant")
employee_file.close()
