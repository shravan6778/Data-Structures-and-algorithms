'''Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.'''
from typing import List
def sortedString(s):
    l=list(s)
    l.sort()
    return "".join(l)
    
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d={}
    
    for i in strs:
        key=sortedString(i)
        if key in d:
            d[key].append(i)
        else:
            d[key]=i
    return list(d.values())


        