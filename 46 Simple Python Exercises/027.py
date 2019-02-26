# Write a program that maps a list of words into a list of integers
# representing the lengths of the correponding words. Write it in three
# different ways:
#
# 1) using a for­loop,
# 2) using the higher order function map(),
# 3) using list comprehensions

if __name__ == "__main__":

    words = ["one", "two", "three", "four", "five", "six"]

    # 1)

    print("First way:\n")

    for word in words:
        i = 0
        for letters in word:
            i += 1
        print("{0} has {1} characters".format(word, str(i)))

    # 2)

    print("\nSecond way: \n")

    print(list(map(len, words)))

    # 3)

    print("\nThird way: \n")

    lengths = [len(lenght) for lenght in words]
    print(lengths)
