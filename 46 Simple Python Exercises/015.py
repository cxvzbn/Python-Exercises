# Write a function find_longest_word() that takes a list of words and returns
# the length of the longest one.

msg = "Please write words to find the lenght of the longest one:\n"

# using from exerc 2


def max_of_any(numbers):
    int_typed = [int(x) for x in numbers]
    int_typed.sort(reverse=True)
    return int_typed[0]


def find_longest_word(words):
    lenghts = list()
    for word in words:
        i = 0
        for _ in list(word):
            i += 1
        lenghts.append(i)
    return max_of_any(lenghts)

if __name__ == '__main__':
    print(find_longest_word(input(msg).split()))
