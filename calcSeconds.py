# Given two timestamps of the same day: a number of hours, minutes and seconds
# for both of the timestamps, calculate how many seconds passed between them

def difference_in_seconds(hr1, min1, sec1, hr2, min2, sec2):
    return abs(((hr1 * 3600) + (min1 * 60) + sec1) - ((hr2 * 3600) + (min2 * 60) + sec2))


print(difference_in_seconds(1, 1, 1, 2, 2, 2))
print(difference_in_seconds(1, 2, 30, 1, 3, 20))
