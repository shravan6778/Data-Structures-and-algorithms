'''Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.'''

from typing import List
def maxSubArray(self, nums: List[int]) -> int:
    cur_sum=0
    max_sum=nums[i]
    for i in range(0,len(nums)):
        cur_sum+=nums[i]
        if cur_sum>max_sum:
            max_sum=cur_sum
        if cur_sum<0:
            cur_sum=0
    return max_sum
        