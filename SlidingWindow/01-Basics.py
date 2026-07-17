'''Imagine you have an array
[2, 1, 5, 1, 3, 2]
and you're asked:
Find the maximum sum of any 3 consecutive elements.
Brute Force
2+1+5 = 8
1+5+1 = 7
5+1+3 = 9
1+3+2 = 6
Time Complexity
O(n*k)
because every window recalculates the sum.

Sliding Window Idea
Instead of recalculating everything,

Move the window one step.

Window 1

[2 1 5] 1 3 2
sum = 8

Move right

Remove left element

8 - 2 = 6

Add new right element

6 + 1 = 7

Next window

2 [1 5 1] 3 2
sum = 7

Move again

7 - 1 + 3 = 9

No recalculation.

Time becomes

O(n)
'''
from typing import List
def calMaxKSum(l: List[int], k: int) -> int:
    i,j,sumv,max_sum=0,0,0,0
    while(j<len(l)):
        sumv+=l[j]
        if (j-i)+1 < k:
            j+=1
        elif (j-i)+1==k:
            max_sum=max(max_sum,sumv)
            sumv-=l[i]
            i+=1
            j+=1
    return max_sum

calMaxKSum(l=[2, 1, 5, 1, 3, 2],k=3)

