# Define a function sum()and a function multiply()that sums and multiplies
# (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4])should return 10, and multiply([1,# 2, 3, 4])
# should return 24.


def sum_of_numbers(numbers_list):
    i = 0
    for number in numbers_list:
        i += number
    return i


def multiple_of_numbers(numbers_list):
    i = 1
    for number in numbers_list:
        i = i * number
    return i


if __name__ == '__main__':
    instance = [1, 2, 3, 4]
    msg = (
        "Sum and multiple of {} are:\n"
        "Sum: {}\n"
        "Multiple: {}".format(
            instance, 
            sum_of_numbers(instance), 
            multiple_of_numbers(instance)
            )
        )
    print(msg)
