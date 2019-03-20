# Using the higher order function filter(), define a function
# filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))


if __name__ == "__main__":
    instance = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "thirteen"
    ]
    msg = (
        "Returns the longest word\n"
        "Instance: {}\n"
        "Output: {}\n".format(instance, filter_long_words(instance, 5))
    )
    print(msg)
