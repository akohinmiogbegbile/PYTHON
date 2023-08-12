employee_file = open("employees.txt", "r")
#this line allows us to check whether the file is readable
#print(employee_file.readable())
for i in employee_file.readlines():
    print(i)


employee_file.close()