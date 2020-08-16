# Given a two-digit number, print its left digit, the tens place, and
# its right digit, the ones place.
def tens_and_ones(number):
    print(int(number/10), int(number % 10))


tens_and_ones(79)
