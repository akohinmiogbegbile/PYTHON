#first we want to translate from basic english to Inmi's language and the rules to this language is any vowels
#should be converted into a "g"
""" inmi's language
 vowels -> g
 ------------
 dog -> dgg
 cat -> cgt
"""
def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

