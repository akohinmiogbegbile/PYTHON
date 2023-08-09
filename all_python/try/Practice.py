#Calculator
user = print("Hi which operator would you like to use today? ")
print("+ (Addition)\n- (Subtraction)\n/ (Division)\n* (Multiplication)")
ans= input()
if ans == "+":
    print("you have selected addition")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = num1 + num2
    print(result)
elif ans == "-":
    print("you have selected subtraction")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = num1 - num2
    print(result)
elif ans == "/":
    print("you have selected division")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = num1 / num2
    print(result)
elif ans == "*":
    print("you have selected multiplication")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = num1 * num2
    print(result)

else:
    print("INVALID RESPONSE")

#madlibs

name = input("Enter a Name: ")
age = input("Enter a number: ")
country = input("Enter a country ")
sport = input("Enter a sport: ")
num = input("Enter a number: ")
name2 = input("Enter Previous Name: ")
name3 = input("Enter ongoing name: ")
female = input("Enter a name: ")



print("There was a guy named " + name)
print("He was " + age + " years old")
print("He lived in " + country)
print("His favourite sport was " + sport)
print("Two girls liked " + name2)
print("But " + name3 + " only liked one girl")
print("The girl was " + female)
print("That is all for now")

#functions
def dinner(name):
    print("We will have mac n' cheese for dinner " + name+ " and thats final")

dinner("jesse")

#todo #write a code to find the even numbers from 0-30
#while loops
i = 1000
while i <=1000:
    print(i)
    i = i + 10
print(i)
i = 100
while i <=100:
    print(i)
    i = i+2
print(i)

print("---------------------------------")
#exponential function
def power_raising (base_num, power_num):
    res = 1
    for i in range(power_num):
        res = res * base_num
    return res
print(power_raising(3,3))




