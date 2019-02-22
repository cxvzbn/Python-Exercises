# Write a program that maps a list of words into a list of integers representing the lengths of the correponding
# words.

msg = "Please write words separated by space to get their lenght:\n"


def list_of_lenghts(words):
    lenghts = list()
    for word in words:
        i = 0
        for _ in list(word):
            i += 1
        lenghts.append(i)
    return lenghts

if __name__ == '__main__':
    print(list_of_lenghts(input(msg).split()))
