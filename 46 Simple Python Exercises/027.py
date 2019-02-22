# Write a program that maps a list of words into a list of integers representing the lengths of the correponding
# words. Write it in three different ways: 1) using a for­loop, 2) using the higher order function map(), and 3)
# using list comprehensions.

if __name__ == "__main__":

    words = ["jeden", "dwa", "trzy", "cztery", "piec", "szesc"] 

    # 1)

    print("Pierwszy sposób:\n")

    for word in words:
        i = 0
        for letters in list(word):
            i += 1
        print("{0} ma {1} znaków".format(word, str(i)))

    # 2)

    print("\nDrugi sposób: \n")

    print(list(map(len, words)))

    # 3)

    print("\nTrzeci sposób: \n")

    lengths = [len(lenght) for lenght in words]
    print(lengths)
