'''Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]'''

from typing import List
def moveZeroes(self, nums: List[int]) -> None:
    
    start=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[start],nums[i]=nums[i],nums[start]
            start+=1