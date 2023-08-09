# a for loop is a special type of loop in python which allows us to loop over different collections of items


for letter in "Akoh Inmi":
    print(letter)

friends = ["Sam", "Joseph", "Shenum"]
for names in friends:
    print(names)

for i in range(10):
    print(i)
print("------------------------------------")

for i in range(3,10):
    print(i)
print("------------------------------------")
for i in range(len(friends)):
    print(friends[i])

for i in range(5):
    if i == 0:
        print("first iteration")
    else:
        print("Not first")