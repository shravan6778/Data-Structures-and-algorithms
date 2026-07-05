'''Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

from typing import List
def removeDuplicates(nums: List[int]) -> int:
    start=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[start]:
            start+=1
            nums[start]=nums[i]
    return start

        