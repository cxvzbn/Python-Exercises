# Represent a small bilingual lexicon as a Python dictionary in the following
# fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
# "new":"nytt", "year":"år"} and use it to translate your Christmas cards from
# English into Swedish. Use the higher order function map() to write
# a function translate() that takes a list of English words and returns a list
# of Swedish words.


def translate(english_words):
    dt = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "ar"
    }
    return " ".join(map(
        lambda word: dt[word] if word in dt else word , english_words.split()
        ))


if __name__ == "__main__":
    instance = "merry christmas and happy new year"
    msg = (
        "Returns translation using map()\n"
        "Instance: {}\n"
        "Output: {}\n".format(instance, translate(instance))
    )
    print(msg)
