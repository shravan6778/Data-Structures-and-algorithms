'''Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104'''

from typing import List
def maxArea(self, height: List[int]) -> int:
    left=0
    right=len(height)-1
    max_water=0
    while left<right:
        width=right-left
        current_height=min(height[left],height[right])
        
        max_water=max(max_water,width*current_height)
        
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_water