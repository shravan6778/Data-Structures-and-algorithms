'''Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''
from typing import List
def runningSum(nums: List[int]) -> List[int]:
    # s=0
    # for i in range(0,len(nums)):
    #     s+=nums[i]
    #     nums[i]=s
    
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]
        
    return nums