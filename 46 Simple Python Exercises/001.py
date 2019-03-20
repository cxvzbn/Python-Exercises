# Define a function max()that takes two numbers as arguments and returns the
# largest of them. Use the if then­ else construct available in Python.
# (It is true that Python has the max()function built in, but writing it
# yourself is nevertheless a good exercise.)


def max(n, m):
    if n > m:
        return n
    else:
        return m


if __name__ == '__main__':
    instance = [2, 7]
    msg = (
        "Returns the highest number out of two numbers\n"
        "Instance: {}\n"
        "Output: {}".format(instance, max(instance[0], instance[1]))
    )
    print(msg)
