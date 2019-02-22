# Write a function filter_long_words()that takes a list of words and an integer nand returns the list of
# words that are longer than n.

msg1 = "Please input a list of words separated by space to get words longer than n: \n"
msg2 = "Please input a number:\n"


def filter_long_words(words, n):
    words_longer_than_n = list()
    for word in words:
        if len(word) > n:
            words_longer_than_n.append(word)
    return words_longer_than_n


if __name__ == '__main__':
    print(filter_long_words(input(msg1).split(), int(input(msg2))))
