'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

The Boyer-Moore Voting Algorithm
The Core Rules
As we iterate through the list, we maintain two variables: a candidate and a count.

If count is 0, we assign the current number as our new candidate and set count to 1.

If the current number matches our candidate, we increment count by 1.

If the current number does not match our candidate, we decrement count by 1.

Step  Current       Action                candidate  count  Explanation
       Number
  1      1    count is 0. New candidate.     1        1         1 steps up as the first candidate.
  2      2    Doesn't match.                 1        0         2 cancels out 1. Back to zero.
  3      3    count is 0. New candidate.     3        1         3 steps up.
  4      3    Matches candidate.             3        2         3 gets a reinforcement.
  5      3    Matches candidate.             3        3         Another 3. The lead grows.
  6      3    Matches candidate.             3        4         3 is looking very strong here!
  7      1    Doesn't match.                 3        3         1 fights back and cancels a 3.
  8      2    Doesn't match.                 3        2         2 attacks. Another 3 goes down.
  9      1    Doesn't match.                 3        1         1 attacks again. The lead is dwindling.
  10     2    Doesn't match.                 3        0         2 wipes out the last remaining 3.
  
'''
from typing import List
def majorityElement(nums: List[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate

#Using HapMap

def majorityElement(self, nums: List[int]) -> int:
    if len(nums)==1:
        return nums[0]
    d={}
    for i in nums:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    max_ele=1
    for key in d:
        if d[key]>max_ele:
            max_ele=d[key]
            maxi=key
    return maxi
