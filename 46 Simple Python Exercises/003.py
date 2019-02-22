# Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)

msg1 = "Please input something to recieve the length of it\n"


def length(user_input):
    i = 0
    for x in list(user_input):
        if x != " ":
            i += 1
    print("Lenght of \"" + user_input + "\" is: " + str(i))

if __name__ == '__main__':
    length(input(msg1))
