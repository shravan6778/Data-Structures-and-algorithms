'''Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.'''

from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    for i in d.values():
        if i>=2:
            return True
    return False