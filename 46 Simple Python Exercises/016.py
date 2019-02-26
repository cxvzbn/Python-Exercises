# Write a function filter_long_words() that takes a list of words and an
# integer n and returns the list of words that are longer than n.


def filter_long_words(words, n):
    words_longer_than_n = list()
    for word in words:
        if len(word) > n:
            words_longer_than_n.append(word)
    return words_longer_than_n


if __name__ == '__main__':
    example_input = [6, ["you", "program", "python", "github", "discourage"]]
    msg = (
        "Returns words longer than n\n"
        "Input: {}\n"
        "Output: {}".format(
            example_input,
            filter_long_words(example_input[1], example_input[0])
        )
    )
    print(msg)
