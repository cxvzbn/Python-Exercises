# Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I
# saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no
# basil", "Satan, oscillate my metallic sonatas", "I roamed under it as
# a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit,
# I'm mad!". Note that punctuation, capitalization, and spacing are usually
# ignored.


def find_in_list(something, list):
    if something in list:
        return True
    return False


def palindrome_recognizer(list_of_phrases):
    output = ""
    list_of_letters = [chr(letter) for letter in range(97, 123)]
    for phrase in list_of_phrases:
        letters = [letter for letter in
                   phrase.lower() if find_in_list(letter, list_of_letters)]
        if letters == reversed(letters):
            output += "'{}' is a palindrome\n".format(phrase)
        else:
            output += "'{}' is not a palindrome\n".format(phrase)
    return output


if __name__ == '__main__':
    instance = [
        "Go hang a salami I'm a lasagna hog.",
        "Was it a rat I saw?",
        "Step on no pets",
        "Sit on a potato pan, Otis",
        "Lisa Bonet ate no basil",
        "Satan, oscillate my metallic sonatas",
        "I roamed under it as a tired nude Maori",
        "Rise to vote sir",
        "Dammit, I'm mad!",
        "ahhah"
    ]
    msg = (
        "Returns if a sentence is a palindrome\n"
        "Instance: {}\n"
        "Output: \n{}".format(instance, palindrome_recognizer(instance))
    )
    print(msg)
