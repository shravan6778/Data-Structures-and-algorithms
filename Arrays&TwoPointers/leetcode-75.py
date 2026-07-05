'''Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]'''

from typing import List
def sortColors(nums: List[int]) -> None:
    left=0
    right=len(nums)-1
    i=0
    
    while i<=right:
        if nums[i]==1:
            i+=1
        elif nums[i]==0:
            nums[i],nums[left]=nums[i],nums[left]
            i+=1
            left+=1
        else:
            nums[i],nums[right]=nums[i],nums[right]
            right-=1
    
        