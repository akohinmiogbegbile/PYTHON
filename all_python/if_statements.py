is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male and are tall")
elif not is_male and not is_tall:
    print("You are no a male an are short")
else:
    print("You are either not a male or tall or both")