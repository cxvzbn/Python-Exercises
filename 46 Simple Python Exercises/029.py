# Using the higher order function filter(), define a function filter_long_words()that takes a list of
# words and an integer nand returns the list of words that are longer than n.


def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))


if __name__ == "__main__":
    words = ["jeden", "dwa", "trzy", "cztery", "piec",
             "szesc", "dwadziesciaosiem", "czterdziescijeden"]
    print(filter_long_words(words, 5))
