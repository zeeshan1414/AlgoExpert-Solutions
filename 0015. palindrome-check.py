def isPalindrome(str):
    n = len(str) - 1
    i = 0
    while i < n:
        if str[i] != str[n]:
            return False
        i += 1
        n -= 1
    return True

str = "abccba"
print(isPalindrome(str))