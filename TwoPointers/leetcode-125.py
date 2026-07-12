'''Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''

def isAlphaNumeric(s: str) -> bool:
    x=ord(s)
    if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
        return True
    return False
    
def isPalindrome(s: str) -> bool:
    s=s.lower()
    i=0
    j=len(s)-1
    while i<j:
        if not isAlphaNumeric(s[i]):
            i+=1
        elif not isAlphaNumeric(s[j]):
            j-=1
        elif s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True