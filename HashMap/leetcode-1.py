'''Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]'''

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    d={}
    for i in range(0,len(nums)):
        rem = target - nums[i]
        if rem in d:
            return [d[rem],i]
        d[nums[i]]=i