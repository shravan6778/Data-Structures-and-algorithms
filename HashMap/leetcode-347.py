'''Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]'''

from typing import List
import heapq
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    heap=[]
    for num,freq in d.items():
        heapq.heappush(heap,(freq,num))
        if len(heap)>k:
            heapq.heappop(heap)
    
    l=[]
    for freq,num in heap:
        l.append(num)
    return l