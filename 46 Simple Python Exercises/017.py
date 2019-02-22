# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
# salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet
# ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote
# sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually
# ignored.

phrases = ["Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
           "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", "Dammit, I'm mad!", "chuj"]


def find_in_list(something, list):
    if something in list:
        return True
    return False


def palindrome_recognizer(list_of_phrases):
    list_of_letters = [chr(letter) for letter in range(97, 123)]
    for phrase in list_of_phrases:
        letters = [letter for letter in list(
            phrase.lower()) if find_in_list(letter, list_of_letters)]
        if letters == list(reversed(letters)):
            print(phrase + " - Is a palindrome\n")
        else:
            print(phrase + " - Is not a palindrome\n")


if __name__ == '__main__':
    palindrome_recognizer(phrases)
