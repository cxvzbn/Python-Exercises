# Using the higher order function filter(), define a function
# filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))


if __name__ == "__main__":
    words = [
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
        "Input: {}\n"
        "Output: {}\n".format(words, filter_long_words(words, 5))
    )
    print(msg)
