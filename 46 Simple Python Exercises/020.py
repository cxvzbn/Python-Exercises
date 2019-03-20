# Represent a small bilingual lexicon as a Python dictionary in the following
# fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
# "new":"nytt", "year":"år"} and use it to translate your Christmas cards from
# English into Swedish. That is, write a function translate() that takes
# a list of English words and returns a list of Swedish words


def translate(english_words):
    dictionary = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "ar"
    }

    translation = ""
    for word in english_words.split():
        if word in dictionary:
            translation += dictionary[word]
        else:
            translation += word
        translation += " "
    return translation



if __name__ == "__main__":
    instance = "merry christmas and happy new year"
    msg = (
        "Returns translation from swedish to english using dictionaries\n"
        "Instance: {}\n"
        "Output: {}\n".format(instance, translate(instance))
    )
    print(msg)