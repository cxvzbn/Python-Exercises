# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}and
# use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
# = that takes a list of English words and returns a list of Swedish words


def translate(english_words):
    dictionary = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "år"
    }


"""    for word in english_words.split():
        for n, translation in enumerate(swedish_to_english):
            if word == translation[0]:
                translated += translation[1] + " "
                break
            elif n == len(swedish_to_english) - 1:
                translated += word + " """

    for word in english_words.split():
        if word in dictionary:
            


if __name__ == "__main__":
    print(translate("merry christmas and happy new year"))
