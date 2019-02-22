# Write a function find_longest_word()that takes a list of words and returns the length of the longest
# one. Use only higher order functions.
from functools import reduce


if __name__ == "__main__":
    
    words = ["jeden", "dwa", "trzy", "cztery", "piec", "szesc", "dwadziesciaosiem", "czterdziescijeden"] 

    print(reduce(max, list(map(len, words))))
