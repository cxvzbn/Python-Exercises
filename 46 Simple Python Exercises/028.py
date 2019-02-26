# Write a function find_longest_word() that takes a list of words and returns
# the length of the longest one. Use only higher order functions.
from functools import reduce


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
        "Returns the lenght of the longest word\n"
        "Input: {}\n"
        "Output: {}\n".format(words, reduce(max, list(map(len, words))))
    )
    print(msg)
