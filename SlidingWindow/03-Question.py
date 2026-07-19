'''Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input: txt = "forxxorfxdofr", pat = "for"
Output: 3
Explanation: for, orf and ofr appears in the txt, hence answer is 3.
Example 2:

Input: txt = "aabaabaa", pat = "aaba"
Output: 4
Explanation: aaba is present 4 times in txt.
Constraints:
1 <= |pat| <= |txt| <= 105
Both strings contain lowercase English letters.
'''
def search(self,pat, txt):
    k = len(pat)
    i, j, total = 0, 0, 0
    pat_count = {}
    for char in pat:
        pat_count[char] = pat_count.get(char, 0) + 1
    count = len(pat_count) 
    while j < len(txt):
        if txt[j] in pat_count:
            pat_count[txt[j]] -= 1
            if pat_count[txt[j]] == 0:
                count -= 1
        if (j - i) + 1 < k:
            j += 1
        elif (j - i) + 1 == k:
            if count == 0:
                total += 1
            if txt[i] in pat_count:
                pat_count[txt[i]] += 1
                if pat_count[txt[i]] == 1:
                    count += 1
            i += 1
            j += 1
            
    return total