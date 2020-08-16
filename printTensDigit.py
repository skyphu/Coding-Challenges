# Given an integer, print its tens digit

def getTensDigit(number):
    return (str(number // 10)[-1])


print(getTensDigit(1238904))
print(getTensDigit(127839743892))
print(getTensDigit(9))
print(getTensDigit(1234))
