'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2'''

#Brute Force O(n^2)
def subarraySum(nums: List[int], k: int) -> int:
    result = 0
    for i in range(len(nums)):
        sums = 0
        for j in range(i, len(nums)):
            sums += nums[j]
            if sums == k:
                result += 1
    return result

#Optimized O(n)
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    result=0
    current_sum=0
    prefix_sum=0
    
    for i in nums:
        current_sum+=i
        
        if (current_sum-k) in prefix_sum:
            result+=prefix_sum[current_sum-k]
        
        if current_sum in prefix_sum:
            prefix_sum[current_sum]+=1
        else:
            prefix_sum[current_sum]
            
    return result
