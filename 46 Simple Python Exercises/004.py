# Write a function that takes a character (i.e. a string of length 1) and returns Trueif it is a vowel, False
# otherwise

msg1 = "Please enter a character to check if it's a vowel: \n"


def vowel(user_input):
    vowels = ["a", "e", "i", "u", "o"]
    for character in vowels:
        if user_input in (character, character.upper()):
            return " is a vowel"
    return " is not a vowel"

if __name__ == '__main__':
    random_input = ["a", "b", "c", "d", "e", "f", "g", "i"]
    for character in random_input:
        print(character + vowel(character))
    
