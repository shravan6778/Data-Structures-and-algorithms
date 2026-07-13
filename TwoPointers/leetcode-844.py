'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".'''

def backspaceCompare(s: str, t: str) -> bool:
    s1=[]
    t1=[]
    for i in list(s):
        if i != '#':
            s.append(i)
        else:
            if len(s)!=0:
                s.pop()
                
    for j in list(j):
        if j!='#':
            t.append(j)
        else:
            if len(t)!=0:
                t.pop()
    
    if len(s1)!=len(t1):
            return False
    if len(s1)==0 and len(t1)==0:
            return True
    
    for i in range(0,len(s1)):
        if s1[i]!=t1[i]:
            return False
    return True