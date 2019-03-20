# Write a function find_longest_word() that takes a list of words and returns
# the length of the longest one. Use only higher order functions.
from functools import reduce


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
        "Returns the lenght of the longest word\n"
        "Instance: {}\n"
        "Output: {}\n".format(instance, reduce(max, list(map(len, instance))))
    )
    print(msg)
