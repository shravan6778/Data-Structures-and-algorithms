'''Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false'''

def validPalindrome(s: str) -> bool:
    i=0
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            skip_left=s[i+1:j+1]
            skip_right=s[i:j]
            return skip_left==skip_left[::-1] or skip_right==skip_right[::-1]
    return True
