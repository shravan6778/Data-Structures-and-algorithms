'''Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false'''

def isAnagram(s: str, t: str) -> bool:
    freq={}
    for i in s:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    for j in t:
        if j in freq:
            freq[i]=freq[i]-1
        else:
            return False
    
    for k in freq.values():
        if k!=0:
            return False
    return True