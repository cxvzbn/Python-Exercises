# Write a function that takes a character (i.e. a string of length 1)
# and returns True if it is a vowel, False otherwise

msg1 = ""


def vowel(user_input):
    vowels = ["a", "e", "i", "u", "o"]
    for character in vowels:
        if user_input in (character, character.upper()):
            return True
    return False

def vowel_output(instance):
    output = ""
    for character in instance:
        if vowel(character):
            output += "{} is a vowel\n".format(character)
        else:
            output += "{} is not a vowel\n".format(character)
    return output


if __name__ == '__main__':
    instance = ["a", "b", "c", "d", "e", "f", "g", "i"]
    msg = (
        "Checks if characters are vowels or not.\n"
        "Instance: {}\n"
        "Output:\n{}".format(instance, vowel_output(instance))
    )
    print(msg)