# Write a function filter_long_words() that takes a list of words and an
# integer n and returns the list of words that are longer than n.


def filter_long_words(words, n):
    words_longer_than_n = list()
    for word in words:
        if len(word) > n:
            words_longer_than_n.append(word)
    return words_longer_than_n


if __name__ == '__main__':
    instance = [6, ["you", "program", "python", "github", "discourage"]]
    msg = (
        "Returns words longer than n\n"
        "Instance: {}\n"
        "Output: {}".format(
            instance,
            filter_long_words(instance[1], instance[0])
        )
    )
    print(msg)
