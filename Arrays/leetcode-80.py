'''Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

from typing import List
def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums)<=2:
        return nums
    start=2
    for i in range(2,len(nums)):
        if nums[i]!=nums[start-2]:
            nums[start]=nums[i]
            start+=1
    return nums
