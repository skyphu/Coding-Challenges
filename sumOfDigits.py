from functools import reduce


def sum_of_digits(number):
    total = 0
    for item in str(number):
        total += int(item)
    return total
    # return reduce(lambda a, b: int(a) + int(b), str(number).split())


number = 123
print(sum_of_digits(number))
