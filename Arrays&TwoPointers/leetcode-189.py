'''Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]'''

from typing import List
def reverse(nums: List[int], start: int, end: int) -> None:
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
    
def rotate(nums: List[int], k: int) -> None:
    n=len(nums)
    k=k%n
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    #Brute Force O(n^2)
    # for l in range(k):
    #     i=len(nums)-1
    #     j=len(nums)-2

    #     while i>0:
    #         nums[i],nums[j]=nums[j],nums[i]
    #         i-=1
    #         j-=1
        