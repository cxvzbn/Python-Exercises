# A pangram is a sentence that contains all the letters of the English
# alphabet at least once, for example: The quick brown fox jumps over the lazy
# dog. Your task here is to write a function to check a sentence to see if it
# is a pangram or not.

phrases = [
    "Write a program that maps a list of words",
    "Yeah thats good",
    "The quick brown fox jumps over the lazy dog",
    "I like trains",
    "We promptly judged antique ivory buckles for the next prize",
    "Two driven jocks help fax my big quiz",
    "Fickle jinx bog dwarves spy math quiz",
    "Twitchtv is a fun entertaiment website",
    "Public junk dwarves hug my quartz fox",
    "Netflix is the best"
]


def panagram_checker(list_of_sentences):
    output = ""
    for sentence in list_of_sentences:
        alphabet = [chr(letter) for letter in range(97, 123)]
        for letter in sentence:
            if letter.lower() in alphabet:
                alphabet.remove(letter.lower())
        if len(alphabet) == 0:
            output += "'{}' is a panagram\n".format(sentence)
        else:
            output += "'{}' is not a panagram\n".format(sentence)
    return output


if __name__ == '__main__':
    msg = (
        "Returns if a sentence is a panagram\n"
        "Input: {}\n"
        "Output: \n{}".format(phrases, panagram_checker(phrases))
    )
    print(msg)

