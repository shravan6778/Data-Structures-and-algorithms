'''Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length'''

def maxVowels(s: str, k: int) -> int:
    i,j,max_vowels,count=0,0,0,0
    while j<len(s):
        if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u':
            count+=1
        if (j-i)+1 < k:
            j+=1
        elif (j-i)+1 == k:
            max_vowels=max(max_vowels,count)
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                count-=1
            i+=1
            j+=1
    return max_vowels