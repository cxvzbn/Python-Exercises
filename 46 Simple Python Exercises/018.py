# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The
# quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
# is a pangram or not.

data_values = ["Write a program that maps a list of words", "ale beka co nie", "The quick brown fox jumps over the lazy dog",
               "normalnie jak u mojego starego", "We promptly judged antique ivory buckles for the next prize",
               "Two driven jocks help fax my big quiz", "A pangram is a sentence that contains all the letters of the English alphabet",
               "Fickle jinx bog dwarves spy math quiz", "hwdp", "Public junk dwarves hug my quartz fox", "no chyba nie wiem co to ma byc"]


def panagram_checker(list_of_sentences):
    for sentence in list_of_sentences:
        alphabet = [chr(letter) for letter in range(97, 123)]
        for letter in list(sentence):
            if letter.lower() in alphabet:
                alphabet.remove(letter.lower())
        if len(alphabet) == 0:
            print("\"" + sentence + "\" -- Is a panagram\n")
        else:
            print("\"" + sentence + "\" -- Is not a panagram\n")


if __name__ == '__main__':
    msg = format("Checking if:\n\"" + "\"\n\"".join(data_values) +
                 "\"\nare panagrams or not.\n")
    panagram_checker(data_values)
