'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104'''

from typing import List
def search(nums: List[int], target: int) -> int:
    l=0
    r=len(nums)-1
    while(l<=r):
        mid=(l+r)//2
        if target==nums[mid]:
            return True
        elif target>nums[mid]:
            l=mid+1
        else:
            r=mid-1
    return False
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for i in matrix:
        if search(i,target):
            return True
    return False