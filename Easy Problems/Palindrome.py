# Input: n = 12321
# Output: True
# Explanation: 12321 is a palindrome number because it reads same  forward and backward.

# Input: n = 1234
# Output:  False
# Explanation: 1234 is not a palindrome number because it does not read the same forward and backward.

#[Expected Approach] - By Reversing The Number
def isPalindrome(n):
    reverse = 0
    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return (reverse == abs(n))

#[Alternate Approach] - Using Number as String
def isPalindromeAlternate(n):
    s = str(abs(n))
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

n = 12321
if isPalindrome(n) == True:
    print("True")
else:
    print("False")
    
if isPalindromeAlternate(n) == True:
    print("True")
else:
    print("False")