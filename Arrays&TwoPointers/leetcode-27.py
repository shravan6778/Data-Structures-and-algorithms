'''Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

from typing import List
def removeElement(nums: List[int], val: int) -> int:
    start=0
    for i in range(0,len(nums)):
        if nums[i]!=val:
            nums[start]=nums[i]
            start+=1
    return start