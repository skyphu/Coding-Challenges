# Given an integer greater than nine, print its last two digits

def lastTwoDigits(number):
    if (number > 9):
        return(str(number)[-2:])
    return number


print(lastTwoDigits(1234))
print(lastTwoDigits(10))
print(lastTwoDigits(1279387943))
print(lastTwoDigits(9))
