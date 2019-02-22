# Define a function is_palindrome()that recognizes palindromes (i.e. words that look the same written
# backwards). For example, is_palindrome("radar")should return True.

msg = "Checks if a word is a palindrome\n"


def is_palindrome(word):
    word_list = list(word)
    word_list_reversed = word_list.copy()
    word_list_reversed.reverse()
    if "".join(word_list) == "".join(word_list_reversed):
        return True
    return False

if __name__ == '__main__':
    print(is_palindrome(input(msg)))
