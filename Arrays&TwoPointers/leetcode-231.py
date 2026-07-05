'''Example 1:

Input: n = 1
Output: true
Explanation: 2^0 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 2^4 = 16'''

def isPowerOfTwo(n: int) -> bool:
    if n==0:
        return False
    while n%2==0:
        n//=2
    return n==1


        

