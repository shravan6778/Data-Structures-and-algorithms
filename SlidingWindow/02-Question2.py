''' First Negative Integer In Every Window Of Size K
Problem statement
You have been given an array of integers 'ARR' and an integer ‘K’. You need to find the first negative integer in each window of size ‘K’.

Note :
If a window does not contain a negative integer, then print 0 for that window.
For example :
If N = 9, arr[ ] = {-10, 20, -30, -40, 50, 60, -70, 80, 90} and K = 3

then the output will be
{-10 -30 -30 -40 -70 -70 -70}
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10^2
1 <= N <= 10^3
-10^4 <= data <= 10^4
1 <= K <= N

Where ‘N’ is the size of the array, “data” is the value of the element of the array 'ARR' and ‘K’ is the window size.

Time Limit: 1 sec
Sample Input 1:
1
9
-10 20 -30 -40 50 60 -70 80 90
3
Sample Output 1:
-10 -30 -30 -40 -70 -70 -70
Explanation For Sample Input 1:
Here the first negative integer in the window  of size K = 3 is [-10, -30, -30, -40, -70, -70, -70]
Sample Input 2:
1
6
-10 20 30 -40 -50 60
2
Sample Output 2:
-10 0 -40 -40 -50 
Explanation For Sample Input 2:
Here the first negative integer in the window  of size 'K' is [-10, 0, -40, -40, -50]'''

from collections import deque
from typing import List
def firstNegativeInteger(l: List[int], k: int) -> List[int]:
    n = len(l)
    result = []
    neg_indices = deque()
    for i in range(k):
        if l[i] < 0:
            neg_indices.append(i)
    for i in range(k, n):
        if neg_indices:
            result.append(l[neg_indices[0]])
        else:
            result.append(0)
        while neg_indices and neg_indices[0] <= i - k:
            neg_indices.popleft()
            
        if l[i] < 0:
            neg_indices.append(i)
    #Record the answer for the LAST window
    if neg_indices:
        result.append(l[neg_indices[0]])
    else:
        result.append(0)
        
    return result