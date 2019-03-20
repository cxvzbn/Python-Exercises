# Write a program that maps a list of words into a list of integers
# representing the lengths of the correponding words.


def list_of_lenghts(words):
    lenghts = list()
    for word in words:
        i = 0
        for _ in word:
            i += 1
        lenghts.append(i)
    return lenghts


if __name__ == '__main__':
    instance = ["you", "me", "program", "python", "github", "eleven"]
    msg = (
        "Returns the lenght of given words:\n"
        "Instance: {}\n"
        "Output: {}".format(instance, list_of_lenghts(instance))
    )
    print(msg)
