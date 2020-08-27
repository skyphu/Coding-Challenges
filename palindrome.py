def isPalindrome(word):
    return True if word.capitalize() == word[::-1].capitalize() else False


print(isPalindrome("girafarig"))
print(isPalindrome("mat"))
